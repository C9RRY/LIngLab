from playsound import playsound
from pathlib import Path
import requests
from PyQt5.QtCore import QThread, pyqtSignal
import time
from pynput import keyboard
import translators as ts
from database import save_to_dict, find_translation

audio_file_path = 'audio/'


def book_vocabulary_count(book):
    text = cut_bad_symbols(book)
    word_list = text.split(' ')
    word_list = set(word_list)
    return len(word_list)


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


def cut_bad_symbols(work_text):
    bad_symbols = ' ,.-!?:;()"'
    for symbol in bad_symbols:
        work_text = work_text.replace(f'{symbol}', ' ')
        work_text = work_text.replace(f'{symbol}', ' ')
    return work_text


def translate(word):
    ouput = ts.google(word, from_language='en', to_language='uk')
    return ouput


def current_word(current_position, text):
    stop_symbol = ' ,.-!?":;()'
    word = text[current_position]
    right_correction = 1
    left_correction = 1
    while True:
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
    with open(file_path) as work_text:
        text = work_text.read()
        print("text extracted")
        return text


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
