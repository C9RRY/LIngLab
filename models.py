import sqlite3


database_path = 'ling_lab.sqlite3'


def create_user():
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users( "
                   "id INTEGER PRIMARY KEY, "
                   "user_name VARCHAR(50) UNIQUE, "
                   "password VARCHAR(50))")
    conn.commit()


def create_dictionary():
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE dictionary( "
                   "id INTEGER PRIMARY KEY , "
                   "word VARCHAR(250), "
                   "translation VARCHAR(250) NOT NULL UNIQUE,"
                   "collection VARCHAR(50), "
                   "pronounce FILEFIELD) ")
    conn.commit()


def create_vocabulary():
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE vocabulary( "
                   "id INTEGER PRIMARY KEY, "
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


def create_all():
    try:
        create_user()
        create_dictionary()
        create_vocabulary()
    except:
        pass


if __name__ == "__main__":
    create_all()
