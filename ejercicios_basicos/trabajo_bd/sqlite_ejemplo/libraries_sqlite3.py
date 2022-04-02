"""_summary_

    Working with libreries SQLite3 and contextlib to implement contextmanager

"""

from contextlib import contextmanager
import sqlite3
from typing import Generator

@contextmanager
def connect_db() -> Generator:
    try:
        conn: sqlite3.Connection = sqlite3.connect('movies.db')
        conn.row_factory = sqlite3.Row
        yield conn.cursor()
    except Exception as e:
        print(f"Error in: {e}")
    finally:
        conn.commit()
        conn.close()

if __name__ == '__main__':
    movies: list = [
        ('The Godfather', 'Francis Ford Coppola', 'crime', '1972'),
        ('The Shawshank Redemption', 'Frank Darabont', 'drama', '1994'),
        ('The Godfather: Part II', 'Francis Ford Coppola', 'crime', '1974'),
        ('Pulp Fiction', 'Quentin Tarantino', 'crime', '1994'),
        ('The Good, the Bad and the Ugly', 'Sergio Leone', 'western', '1967'),
    ]
    
    with connect_db() as cursor:
        cursor.execute("CREATE TABLE movies (title TEXT, director TEXT, genre TEXT, year TEXT)")
        cursor.executemany("INSERT INTO movies VALUES (?, ?, ?, ?)", movies)
        movies: list = cursor.execute("SELECT * FROM movies")
        first = movies.fetchall()[0]
        print(dict(first))
    