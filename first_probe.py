from playsound import playsound
from pydub import AudioSegment
from pathlib import Path
import requests


word = 'i love my bike'
file_path = 'audio/'
word_list = word.split(' ')
if len(word_list) == 1:
    my_file = Path(f'{file_path}{word}.mp3')
    if my_file.is_file():
        playsound(f'{file_path}{word}.mp3')
    else:
        url = f'https://ssl.gstatic.com/dictionary/static/sounds/oxford/{word}--_us_1.mp3'
        r = requests.get(url, allow_redirects=True, timeout=1)
        if r:
            open(f'{file_path}{word}.mp3', 'wb').write(r.content)
            playsound(f'{file_path}{word}.mp3')
else:
    for word in word_list:
        my_file = Path(f'{file_path}{word}.mp3')
        if my_file.is_file():
            playsound(f'{file_path}{word}.mp3')
        else:
            url = f'https://ssl.gstatic.com/dictionary/static/sounds/oxford/{word}--_us_1.mp3'
            r = requests.get(url, allow_redirects=True, timeout=1)
            if r:
                open(f'{file_path}{word}.mp3', 'wb').write(r.content)
                playsound(f'{file_path}{word}.mp3')
