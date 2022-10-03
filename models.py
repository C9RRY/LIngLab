import sqlite3


database_path = 'ling_lab.sqlite3'


def create_user():
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users( "
                   "id serial NOT NULL, "
                   "user_name varchar(50) UNIQUE, "
                   "password varchar(50), "
                   "PRIMARY KEY (id))")
    conn.commit()


def create_dictionary():
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE dictionary( "
                   "id serial PRIMARY KEY NOT NULL, "
                   "word VARCHAR(250), "
                   "translation VARCHAR(250) NOT NULL UNIQUE, "
                   "pronounce FILEFIELD) ")
    conn.commit()


def create_vocabulary():
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE vocabulary( "
                   "id serial PRIMARY KEY NOT NULL, "
                   "user_id INTEGER, "
                   "word_id INTEGER, "
                   "progress VARCHAR(10) DEFAULT '*', "
                   "progress_write BOOLEAN, "
                   "progress_read BOOLEAN, "
                   "progress_audition BOOLEAN, "
                   "progress_repeat BOOLEAN, "
                   "FOREIGN KEY('user_id') REFERENCES 'users'('id'), "
                   "FOREIGN KEY('word_id') REFERENCES 'dictionary'('id') ) ")
    conn.commit()


if __name__ == "__main__":
    create_user()
    create_dictionary()
    create_vocabulary()
