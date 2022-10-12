from playsound import playsound
from pathlib import Path
import requests
from database import save_to_dict, find_translation

audio_file_path = 'audio/'


def book_vocabulary_count(book):
    text = cut_bad_symbols(book)
    word_list = text.split(' ')
    word_list = set(word_list)
    return len(word_list)


def get_word_in_text_count(path):
    text = open_text_file(path)
    count = text.split(' ')


def dictionary_updater(text):
    text = cut_bad_symbols(text)
    word_list = text.split(' ')
    word_list = set(word_list)
    for word in word_list:
        # word = word.lower()
        try:
            translated = translate(word)
            print(word, translated)
            if word in find_translation(word):
                print('to skip')
                continue
            save_to_dict(word, translated)
        except:
            print('except in utils')


def leave_good_symbols(text, filters):
    text = text.replace('__', ' ')
    text = text.replace('\n', ' ')
    text = text.replace('  ', ' ')
    new_text = ''
    if filters != 'full text':
        for symbol in text:
            if filters == 'letter only' or filters == 'letter and digit':
                if symbol.isalpha() or symbol == ' ':
                    new_text += symbol
            if filters == 'letter and digit' or filters == 'symbols only':
                if symbol.isdigit():
                    new_text += symbol
            if filters == 'symbols only':
                if not symbol.isalpha():
                    new_text += symbol
        return new_text
    return text


def cut_bad_symbols(work_text, filters):
    bad_symbols = filters
    for symbol in bad_symbols:
        work_text = work_text.replace(symbol, '')
        work_text = work_text.replace(symbol, '')
    return work_text


def translate(word):
    import translators as ts
    output = ts.google(word, from_language='en', to_language='uk')
    return output


def current_word(current_position, text):
    stop_symbol = ' ,.-!?":;()'
    how_long_to_end = len(text) - current_position
    if how_long_to_end > 2:
        word = text[current_position]
    else:
        word = text = '  '
    right_correction = 1
    left_correction = 1
    while True:
        if len(text) <= current_position + right_correction:
                break
        if text[current_position] not in stop_symbol:
            if text[current_position + right_correction] not in stop_symbol:
                word += text[current_position + right_correction]
                right_correction += 1
            elif text[current_position - left_correction] not in stop_symbol:
                word = text[current_position - left_correction] + word
                left_correction += 1
            else:
                break
        else:
            break
    return word.lower()


def open_text_file(file_path):
    try:
        with open(file_path) as work_text:
            text = work_text.read()
            return text
    except Exception as exc:
        return 'select text file in settings!'


def get_and_play_audio(word):
    word = word.lower()
    word_list = word.split(' ')
    if len(word_list) == 1:
        my_file = Path(f'{audio_file_path}{word}.mp3')
        if my_file.is_file():
            playsound(f'{audio_file_path}{word}.mp3')
        else:
            url = f'https://ssl.gstatic.com/dictionary/static/sounds/oxford/{word}--_us_1.mp3'
            r = requests.get(url, allow_redirects=True, timeout=1)
            if r:
                open(f'{audio_file_path}{word}.mp3', 'wb').write(r.content)
                playsound(f'{audio_file_path}{word}.mp3')
    else:
        for word in word_list:
            my_file = Path(f'{audio_file_path}{word}.mp3')
            if my_file.is_file():
                playsound(f'{audio_file_path}{word}.mp3')
            else:
                url = f'https://ssl.gstatic.com/dictionary/static/sounds/oxford/{word}--_us_1.mp3'
                r = requests.get(url, allow_redirects=True, timeout=1)
                if r:
                    open(f'{audio_file_path}{word}.mp3', 'wb').write(r.content)
                    playsound(f'{audio_file_path}{word}.mp3')


if __name__ == "__main__":
    dictionary_updater(open_text_file(2))
