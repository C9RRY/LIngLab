import sqlite3


database_path = 'ling_lab2.sqlite3'


def create_user():
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute(f"CREATE TABLE users" )
    conn.commit()


if __name__ == "__main__":
    create_database()
