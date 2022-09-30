from playsound import playsound
from pydub import AudioSegment
from pathlib import Path
import requests
from PyQt5.QtCore import QThread, pyqtSignal
import time


audio_file_path = 'audio/'


class Timerthread(QThread):
    signal = pyqtSignal(str)

    def __init__(self, limit):
        super(Timerthread, self).__init__()
        self.limit_seconds = limit

    def run(self):
        i = self.limit_seconds
        while i > 0:
            self.signal.emit(str(i))
            time.sleep(1)
            i -= 1
            print(i)
        self.signal.emit('time is up')


def get_and_play_audio(word):
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
    a = Timerthread(10).run()