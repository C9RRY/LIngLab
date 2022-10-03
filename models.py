import sqlite3


database_path = 'ling_lab2.sqlite3'


def create_user():
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users( "
                   "id serial primary key NO NULL, "
                   "user_name varchar(50) UNIQUE, "
                   "password varchar(50)")
    conn.commit()


def create_dictionary():
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE dictionary( "
                   "id serial primary key NO NULL, "
                   "word varchar(250), "
                   "translation varchar(250) NO NULL UNIQUE, "
                   "pronounce filefield ")
    conn.commit()


def create_vocabulary():
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE vocabulary( "
                   "id serial primary key NO NULL, "
                   "user_id INTEGER, "
                   "word_id INTEGER, "
                   "progress VARCHAR(10) DEFAULT '*', "
                   "progress_write BOOLEAN, "
                   "progress_read BOOLEAN, "
                   "progress_audition BOOLEAN, "
                   "progress_repeat BOOLEAN, "
                   "FOREIGN KEY('user_id') REFERENCES 'users'('id'), "
                   "FOREIGN KEY('word_id') REFERENCES 'dictionary'('id') ")
    conn.commit()


if __name__ == "__main__":
    pass

