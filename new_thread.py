from PyQt5.QtCore import QThread, pyqtSignal
from pause_menu import Ui_PauseMenu
from pynput import keyboard
import subprocess
import time


class KeyboardThread(QThread):
    def __init__(self, mainwindow):
        super(KeyboardThread, self).__init__()
        self.mainwindow = mainwindow
        self.current_key = ''
        self.pause_thread = False

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
        if self.pause_thread == False:
            self.mainwindow.print_key(self.current_key)

    def on_release(self, key):
        if key == keyboard.Key.esc:
            return False

    def run(self):
        with keyboard.Listener(
                on_press=self.on_press,
                on_release=self.on_release) as listener:
            listener.join()

    def pause_thr(self):
        self.pause_thread = True

    def pause_off(self):
        self.pause_thread = False


class TimerThread(QThread):
    def __init__(self, mainwindow):
        super(TimerThread, self).__init__()
        self.mainwindow = mainwindow
        self.current_key = ''
        self.pause_thread = False
        self.seconds = 0
        self.clean_timer_if_press_stop = False
        self.send_to_lcd = mainwindow.send_to_lcd
        self.stop_time = 10
        self.lesson_stop = mainwindow.lesson_stop

    def run(self):
        while self.pause_thread == False:
            if self.seconds % self.stop_time == 0 and self.seconds != 0:
                self.lesson_stop()
            self.send_to_lcd(self.seconds)
            time.sleep(1)
            self.seconds += 1

    def pause_thr(self):
        self.pause_thread = True
        if self.clean_timer_if_press_stop == True:
            self.seconds = 0
            self.send_to_lcd(self.seconds)
        self.clean_timer_if_press_stop = True

    def pause_off(self, stop):
        self.stop_time = int(stop) * 60
        self.pause_thread = False
        self.clean_timer_if_press_stop = False

