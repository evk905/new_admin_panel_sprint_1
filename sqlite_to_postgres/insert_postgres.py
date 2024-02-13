from dataclasses import astuple, fields
from utils_dataclasses import Genre, Filmwork, Person, GenreFilmwork, PersonFilmwork


dataclass_tables_pg = {
    Filmwork: "content.film_work",
    Genre: "content.genre",
    GenreFilmwork: "content.genre_film_work",
    Person: "content.person",
    PersonFilmwork: "content.person_film_work",
}


def save_data_to_postgres(data_from_sqlite, pg_conn, dt):
    column_names = [field.name for field in fields(dt)]
    column_names_str = ",".join(column_names)
    col_count = ", ".join(["%s"] * len(column_names))

    with pg_conn as conn:
        with conn.cursor() as cursor:
            bind_values = ','.join(
                cursor.mogrify(f"({col_count})", astuple(data)).decode('utf-8') for data in data_from_sqlite)
            table_name = dataclass_tables_pg[dt]
            query = (f'INSERT INTO {table_name} ({column_names_str}) VALUES {bind_values} '
                     f' ON CONFLICT (id) DO NOTHING'
                     )

            cursor.execute(query)
            conn.commit()