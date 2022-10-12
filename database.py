import sqlite3
from datetime import date


database_path = 'ling_lab.sqlite3'


def save_to_print_session(user_id, time,  count, error, format_time):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    error_percent = (str(error / (error + count) * 100)[:4] if error + count != 0 else '0') + '%'
    speed = str(count / time * 60)[:3] if time != 0 else "0"
    current_date = date.today()
    current_date = current_date.strftime("%d/%m/%Y")
    cursor.execute(f"INSERT INTO print_sessions(user_id, date, write_time, write_speed, symbols_count, errors_count) "
                   f"VALUES ({user_id}, '{current_date}', '{format_time}', '{speed}', {count}, '{error_percent}')")
    conn.commit()


def delete_record(record_id, user):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    cursor.execute(f"DELETE FROM print_sessions "
                   f"WHERE user_id = {user} and id = {record_id}")
    conn.commit()


def get_print_sessions(user_id):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    result = cursor.execute(f"SELECT * FROM print_sessions "
                            f"WHERE user_id = '{user_id}'")
    user_info = [rows for rows in result]
    return user_info


def get_user_list():
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    result = cursor.execute("SELECT id, user_name "
                            " FROM users ")
    user_list = [rows for rows in result]
    return user_list


def get_user_info(user_id):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    result = cursor.execute(f"SELECT * FROM users "
                            f"WHERE id = '{user_id}'")
    user_info = [rows for rows in result]
    return user_info[0]


def new_user(user):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute("UPDATE users "
                   "SET is_current = 'False' ")
    cursor.execute(f"INSERT INTO users (user_name, is_current) "
                   f"VALUES ('{user}', 'True')")
    conn.commit()


def log_out():
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute("UPDATE users "
                   "SET is_current = 'False' ")
    cursor.execute("UPDATE users "
                   "SET is_current = 'True' "
                   "WHERE id = '1'")
    conn.commit()


def check_current_user():
    user_dict = {}
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    result = cursor.execute("SELECT id, user_name, progress, text, font_size, current_position, lesson_time, "
                            "font, text_filter, custom_filter, custom_filter_is_enabled, length_slider "
                            "FROM users "
                            "WHERE is_current = 'True' ").fetchall()

    if result:
        current_user = result[0]
        user_dict['id'], user_dict['user_name'], user_dict['progress'], user_dict['text'],\
        user_dict['font_size'], user_dict['current_position'], user_dict['lesson_time'], user_dict['font'],\
        user_dict['text_filter'], user_dict['custom_filter'], user_dict['custom_filter_is_enabled'], \
        user_dict['length_slider'] = current_user[0],current_user[1], current_user[2], current_user[3], current_user[4],\
        current_user[5], current_user[6], current_user[7], current_user[8], current_user[9], current_user[10],\
        current_user[11]
        return user_dict
    else:
        user_dict['id'], user_dict['user_name'], user_dict['progress'], user_dict['text'], \
        user_dict['font_size'], user_dict['current_position'] = 0, '', 0, '', 22, 0
        return user_dict


def pin_user(user):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute("UPDATE users "
                   "SET is_current = 'False' ")
    cursor.execute(f"UPDATE users "
                   f"SET is_current = 'True' "
                   f"WHERE user_name = '{user}' ")
    conn.commit()


def check_word_id(translation):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    res = cursor.execute(f"SELECT id FROM dictionary "
                         f"WHERE translation = '{translation}'")
    words_list = [rows for rows in res]
    return words_list


def update_user_info(column, value, user_id):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute(f"UPDATE users "
                   f"SET {column} = '{value}' "
                   f"WHERE id = {user_id} ")
    conn.commit()


def my_vocab(user_id):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    res = cursor.execute(f"SELECT d.word, d.translation, d.pronounce, v.progress "
                         "FROM dictionary as d "
                         "INNER JOIN vocabulary as v "
                         "ON d.id = v.word_id "
                         "INNER JOIN users as u "
                         "ON v.user_id = u.id "
                         f"WHERE u.id = '{user_id}'")
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
    check_current_user()

