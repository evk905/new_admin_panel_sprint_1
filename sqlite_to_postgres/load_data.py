import os

from dotenv import load_dotenv

from utils_dataclasses import Genre, Filmwork, Person, GenreFilmwork, PersonFilmwork
from data_from_sqlite import fetch_data_from_database
from insert_postgres import save_data_to_postgres
from context_manager import sqlite_conn_context, pg_conn_context

load_dotenv()

dataclass_tables_sqlite = {
    Filmwork: "film_work",
    Genre: "genre",
    GenreFilmwork: "genre_film_work",
    Person: "person",
    PersonFilmwork: "person_film_work",
}


def load_from_sqlite(sqlite_conn, pg_conn):
    """Основной метод загрузки данных из SQLite в Postgres"""
    for dt, table in dataclass_tables_sqlite.items():
        data_from_sqlite = next(fetch_data_from_database(sqlite_conn, dt, table, batch_size=1000))

        save_data_to_postgres(data_from_sqlite, pg_conn, dt)


if __name__ == '__main__':

    dsn = {
        "dbname": os.getenv("DB_NAME", "movies_database"),
        "user": os.getenv("DB_USER", "app"),
        "password": os.getenv("DB_PASSWORD", "123qwe"),
        "host": os.getenv("DB_HOST", "localhost"),
        "port": os.getenv("DB_PORT", 5432),
    }

    db_path = os.getenv("SQLITE_DB_PATH", "db.sqlite")

    with sqlite_conn_context(db_path) as sqlite_conn:
        with pg_conn_context(**dsn) as pg_conn:
            load_from_sqlite(sqlite_conn, pg_conn)