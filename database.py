import sqlite3


database_path = 'ling_lab.sqlite3'


def get_user_info(user_id):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    result = cursor.execute(f"SELECT * FROM users "
                               f"WHERE id = '{user_id}'")
    user_info = [rows for rows in result]
    return user_info[0]


def check_word_id(translation):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    res = cursor.execute(f"SELECT id FROM dictionary "
                         f"WHERE translation = '{translation}'")
    words_list = [rows for rows in res]
    return words_list


def my_vocab(user_id):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    res = cursor.execute(f"SELECT d.word, d.translation, d.pronounce, v.progress "
                         "FROM dictionary as d "
                         "INNER JOIN vocabulary as v "
                         "ON d.id = v.word_id "
                         "INNER JOIN users as u "
                         "ON v.user_id = u.id "
                         f"WHERE u.id = {user_id}")
    vocab_list = [rows for rows in res]
    return vocab_list


def find_translation(word):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    res = cursor.execute(f"SELECT * FROM dictionary "
                         f"WHERE word = '{word}'")
    words_list = [rows for rows in res]
    return words_list


def add_word_to_user(user_id, word_id):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    cursor.execute(f"INSERT INTO vocabulary(user_id, word_id) "
                   f"VALUES ({user_id}, {word_id})")
    conn.commit()


def save_to_dict(word, translate):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    try:
        cursor.execute(f"INSERT INTO dictionary(word, translation) "
                       f"VALUES ('{word}', '{translate}')")
    except Exception as exc:
        print(f'except in cursor {exc}')
        cursor.execute(f'INSERT INTO dictionary(word, translation) '
                       f'VALUES ("{word}", "{translate}")')
    conn.commit()


def save_to_dict_and_vocab(user_id, word, translate):
    save_to_dict(word, translate)
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    res = cursor.execute(f"SELECT id FROM dictionary "
                         f"WHERE translation = '{translate}'")
    words_list = [rows for rows in res]

    cursor.execute(f"INSERT INTO vocabulary(user_id, word_id) "
                   f"VALUES ('{user_id}', '{words_list[-1][0]}')")
    conn.commit()


def change_the_progress(translation, user, progress):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    word_list = check_word_id(translation)
    for word in word_list:
        word = word[0]
        cursor.execute(f"UPDATE vocabulary "
                       f"SET progress = '{progress}' "
                       f"WHERE user_id = {user} and word_id = {word}")

    conn.commit()


def delete_from_vocab(translation, user):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    word_list = check_word_id(translation)
    for word in word_list:
        word = word[0]
        cursor.execute(f"DELETE FROM vocabulary "
                       f"WHERE user_id = {user} and word_id = {word}")
    conn.commit()


if __name__ == "__main__":
    save_to_dict_and_vocab(1, "home", 'lsfasf')

