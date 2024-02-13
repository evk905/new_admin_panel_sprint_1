import sqlite3
import psycopg2
from psycopg2.extras import DictCursor
from contextlib import contextmanager


db_path = 'db.sqlite'


@contextmanager
def sqlite_conn_context(db_path: str):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()


@contextmanager
def pg_conn_context(**kwargs):
    conn = psycopg2.connect(**kwargs, cursor_factory=DictCursor)
    try:
        yield conn
    finally:
        conn.close()