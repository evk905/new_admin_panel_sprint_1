from dataclasses import fields


def fetch_data_from_database(sqlite_conn, dt, table, batch_size=1000):
    with sqlite_conn as conn:
        curs = conn.cursor()

        field_names = [field.name for field in fields(dt)]
        fields_str = ", ".join(field_names)
        query = f"SELECT {fields_str} FROM {table};"
        curs.execute(query)

        while results := curs.fetchmany(batch_size):
            yield [dt(*element) for element in results]