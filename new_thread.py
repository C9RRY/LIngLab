from PyQt5.QtCore import QThread, pyqtSignal
from pynput import keyboard
import subprocess


class KeyboardThread(QThread):
    def __init__(self, mainwindow):
        super(KeyboardThread, self).__init__()
        self.mainwindow = mainwindow
        self.current_key = ''

    def on_press(self, key):
        capslock_status = subprocess.getoutput("xset q | grep Caps | tr -s ' ' | cut -d ' ' -f 5")
        try:
            self.current_key = str(key.char)
        except AttributeError:
            current = key.value.char
            if current:
                self.current_key = current
        if capslock_status == 'on':
            self.current_key = self.current_key.upper()
        self.mainwindow.print_key(self.current_key)

    def on_release(self, key):
        if key == keyboard.Key.esc:
            return False

    def run(self):
        with keyboard.Listener(
                on_press=self.on_press,
                on_release=self.on_release) as listener:
            listener.join()

# ...or, in a non-blocking fashion:
# listener = keyboard.Listener(
#     on_press=on_press,
#     on_release=on_release)
# listener.start()

#
#
# class Timerthread(QThread):
#     signal = pyqtSignal(str)
#
#     def __init__(self, limit):
#         super(Timerthread, self).__init__()
#         self.limit_seconds = limit
#
#     def run(self):
#         i = self.limit_seconds
#         while i > 0:
#             self.signal.emit(str(i))
#             time.sleep(1)
#             i -= 1
#             print(i)
#         self.signal.emit('time is up')
#
#


