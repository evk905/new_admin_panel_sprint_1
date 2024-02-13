from utils_dataclasses import Genre, Filmwork, Person, GenreFilmwork, PersonFilmwork
from data_from_sqlite import fetch_data_from_database
from insert_postgres import save_data_to_postgres
from context_manager import sqlite_conn_context, pg_conn_context

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
        data_from_sqlite = fetch_data_from_database(sqlite_conn, dt, table, batch_size=10)

        save_data_to_postgres(data_from_sqlite, pg_conn, dt)


if __name__ == '__main__':
    dsn = {
        'dbname': 'movies_database',
        'user': 'app',
        'password': '123qwe',
        'host': 'localhost',
        'port': 5432,
        'options': '-c search_path=content',
    }

    db_path = 'db.sqlite'
    with sqlite_conn_context(db_path) as sqlite_conn:
        with pg_conn_context(**dsn) as pg_conn:
            load_from_sqlite(sqlite_conn, pg_conn)