import sqlite3


database_path = 'ling_lab.sqlite3'


def create_user():
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users( "
                   "id INTEGER PRIMARY KEY, "
                   "user_name VARCHAR(50) UNIQUE, "
                   "is_current BOOLEAN, "
                   "progress INTEGER DEFAULT O, "
                   "lesson_time INTEGER DEFAULT 10, "
                   "text VARCHAR(250) DEFAULT '', "
                   "current_position INTEGER DEFAULT 0, "
                   "text_filter VARCHAR(50) DEFAULT 'full text', "
                   "custom_filter VARCHAR(50), "
                   "custom_filter_is_enabled BOOLEAN DEFAULT FALSE, "
                   "font VARCHAR(100) DEFAULT 'Times', "
                   "font_size INTEGER DEFAULT 22, "
                   "password VARCHAR(50))")

    cursor.execute("INSERT INTO users (user_name, is_current, font, font_size) "
                   "VALUES ('Public', 'True', 'Serif', 22)")
    conn.commit()


def create_dictionary():
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE dictionary( "
                   "id INTEGER PRIMARY KEY , "
                   "word VARCHAR(250), "
                   "translation VARCHAR(250) NOT NULL, "
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


def create_print_sessions():
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE print_sessions( "
                   "id INTEGER PRIMARY KEY, "
                   "user_id INTEGER, "
                   "date VARCHAR(10), "
                   "write_time INTEGER, "
                   "write_speed VARCHAR(19), "
                   "symbols_count INTEGER, "
                   "errors_count INTEGER, "
                   "FOREIGN KEY('user_id') REFERENCES 'users'('id') ) ")
    conn.commit()


def create_all():
    try:
        create_user()
        create_dictionary()
        create_vocabulary()
        create_print_sessions()
    except:
        pass


if __name__ == "__main__":
    create_all()
