from dataclasses import fields


def fetch_data_from_database(sqlite_conn, dt, table, batch_size=10):
    with sqlite_conn as conn:
        curs = conn.cursor()

        data = []

        field_names = [field.name for field in fields(dt)]
        fields_str = ", ".join(field_names)
        query = f"SELECT {fields_str} FROM {table};"
        curs.execute(query)

        while True:
            results = curs.fetchmany(batch_size)
            if not results:
                break
            dt_data = [dt(*element) for element in results]
            data.extend(dt_data)

    return data