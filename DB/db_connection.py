import os
import psycopg2
from dotenv import load_dotenv
from contextlib import contextmanager

load_dotenv()

@contextmanager
def get_cursor():
    conn = None
    cursor = None

    conn = psycopg2.connect(
        host=os.getenv("HOST"),
        database=os.getenv("DATABASE_NAME"),
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD_DB"),
        port=os.getenv("PORT")
    )
    print("✅Database connected successfully...")

    cursor = conn.cursor()

    print("✅Cursor object created successfully...")

    try:
        yield cursor
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        if conn is not None:
            conn.close()
            print("✅ Database connection Closed successfully...")
        if cursor is not None:
            cursor.close()
            print("✅ Cursor object Closed successfully...")



# Explore below:
# 1) contextlib , 2) contextmanager, 3) generator for cursor, how above code is actually working.