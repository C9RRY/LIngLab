from PyQt5 import QtCore, QtGui, QtWidgets
from new_thread import KeyboardThread, TimerThread
from utils import open_text_file, current_word, get_and_play_audio, leave_good_symbols, cut_bad_symbols
from blind_print_options import Ui_BlindPrintSettings
from pause_menu import Ui_PauseMenu
from database import update_user_info


class Ui_BlindPrint(object):
    def show_main(self, main_window, current_window):
        main_window.show()
        current_window.hide()

    def open_new_windows(self, ui_name, BlindPrint, get_text):
        self.window = QtWidgets.QMainWindow()
        self.ui = ui_name
        self.ui.setupUi(self.window, BlindPrint, get_text, self.font_change, self.user)
        self.window.show()

    def open_pause_menu(self, print_count, print_error, time):
        self.window2 = QtWidgets.QMainWindow()
        self.ui2 = Ui_PauseMenu()
        self.ui2.setupUi(self.window2, print_count, print_error, time)
        self.window2.show()

    def setupUi(self, BlindPrint, MainWindow, user):
        self.user = user
        self.user_id = user['id']
        self.BlindPrint = BlindPrint
        self.current_position = user['current_position']
        self.print_text = 'START '
        self.current_word = ' '
        self.timer = QtCore.QTimer()
        self.lesson_time = user['lesson_time']
        self.font_size = user['font_size']
        self.font = user['font']
        self.file_path = user['text']
        self.text_filter = user['text_filter']
        self.custom_filters = user['custom_filter']
        self.custom_filters_is_enabled = user['custom_filter_is_enabled']
        self.correct_print_count = 0
        self.print_errors = 0
        self.current_lesson_time = 0
        self.pause_status = False

        BlindPrint.setObjectName("BlindPrint")
        BlindPrint.resize(838, 523)
        BlindPrint.setStyleSheet("background-color: rgb(102, 111, 108);")
        self.centralwidget = QtWidgets.QWidget(BlindPrint)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(15, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout.addItem(spacerItem, 4, 10, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 12, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 12, 10, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 12, 7, 1, 1)
        self.push_button_back = QtWidgets.QPushButton(self.centralwidget,
                                                  clicked=lambda: self.show_main(MainWindow, BlindPrint))
        self.push_button_back.setFocusPolicy(QtCore.Qt.NoFocus)
        self.push_button_back.setStyleSheet("background-color: rgb(134, 94, 60);")
        self.push_button_back.setObjectName("push_button_back")
        self.gridLayout.addWidget(self.push_button_back, 14, 12, 1, 1)
        self.label_current_word = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_current_word.setFont(font)
        self.label_current_word.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_current_word.setAlignment(QtCore.Qt.AlignCenter)
        self.label_current_word.setObjectName("label_current_word")
        self.gridLayout.addWidget(self.label_current_word, 1, 7, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 12, 8, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(218, 188, 154);")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 9, 9, 1, 4)
        spacerItem5 = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 12, 12, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 12, 5, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem7, 10, 12, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(True)
        font.setKerning(False)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("color: rgb(92, 101, 98);")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 9, 0, 1, 9)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(-1, 1, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem8, 2, 12, 1, 1)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setMinimumSize(QtCore.QSize(50, 50))
        self.lcdNumber_2.setStyleSheet("background-color: rgb(71, 94, 87);\n"
                                       "border-color: rgb(102, 111, 108);")
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.gridLayout_2.addWidget(self.lcdNumber_2, 2, 10, 1, 1)
        self.tool_button = QtWidgets.QToolButton(self.centralwidget,
                                                 clicked=lambda: self.open_new_windows(
                                                     Ui_BlindPrintSettings(), BlindPrint, self.get_text))
        self.tool_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tool_button.setStyleSheet("background-color: rgb(134, 94, 60);")
        self.tool_button.setObjectName("tool_button")
        self.gridLayout_2.addWidget(self.tool_button, 2, 13, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem9, 2, 8, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 58, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem10, 2, 0, 1, 2)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.comboBox.setMinimumSize(QtCore.QSize(40, 40))
        self.comboBox.setMaximumSize(QtCore.QSize(45, 16777215))
        self.comboBox.setStyleSheet("background-color: rgb(152, 106, 68);")
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_2.addWidget(self.comboBox, 2, 11, 1, 1)
        self.push_button_pronounce = QtWidgets.QPushButton(self.centralwidget)
        self.push_button_pronounce.setFocusPolicy(QtCore.Qt.NoFocus)
        self.push_button_pronounce.clicked.connect(self.pronounce)
        self.push_button_pronounce.setStyleSheet("background-color: rgb(205, 171, 143);")
        self.push_button_pronounce.setObjectName("push_button_pronounce")
        self.gridLayout_2.addWidget(self.push_button_pronounce, 2, 4, 1, 1)
        self.profileOpenButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.profileOpenButton.sizePolicy().hasHeightForWidth())
        self.profileOpenButton.setSizePolicy(sizePolicy)
        self.profileOpenButton.setMinimumSize(QtCore.QSize(80, 30))
        self.profileOpenButton.setMaximumSize(QtCore.QSize(100, 30))
        self.profileOpenButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.profileOpenButton.setStyleSheet("background-color: rgb(134, 94, 60);")
        self.profileOpenButton.setObjectName("profileOpenButton")
        self.gridLayout_2.addWidget(self.profileOpenButton, 2, 14, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem11, 2, 7, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton.setStyleSheet("background-color: rgb(181, 131, 90);")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 2, 5, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_2.setStyleSheet("background-color: rgb(134, 94, 60);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 2, 6, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 2, 1, 11)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem12, 12, 9, 1, 1)
        self.verticalWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout.addWidget(self.verticalWidget, 13, 9, 1, 1)
        self.pushButton_start_lesson = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start_lesson.clicked.connect(self.lesson_start)
        self.pushButton_start_lesson.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_start_lesson.setStyleSheet("background-color: rgb(181, 131, 90);")
        self.pushButton_start_lesson.setObjectName("pushButton_start_lesson")
        self.gridLayout.addWidget(self.pushButton_start_lesson, 14, 9, 1, 1)
        self.pushButton_stop_lesson = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_stop_lesson.clicked.connect(self.lesson_stop)
        self.pushButton_stop_lesson.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_stop_lesson.setStyleSheet("background-color: rgb(152, 106, 68);")
        self.pushButton_stop_lesson.setObjectName("pushButton_stop_lesson")
        self.gridLayout.addWidget(self.pushButton_stop_lesson, 14, 10, 1, 1)
        BlindPrint.setCentralWidget(self.centralwidget)

        for minutes in range(5, 31, 5):
            self.comboBox.addItem(str(minutes))
        self.comboBox.setCurrentText(str(self.lesson_time))
        self.time_thread = TimerThread(mainwindow=self)
        QtCore.QMetaObject.connectSlotsByName(BlindPrint)
        self.keyboard_thread = KeyboardThread(mainwindow=self)
        self.get_text(self.file_path, BlindPrint, self.text_filter, self.custom_filters)

    def retranslateUi(self, BlindPrint):
        _translate = QtCore.QCoreApplication.translate
        BlindPrint.setWindowTitle(_translate("BlindPrint", "MyLearn"))
        self.push_button_back.setText(_translate("BlindPrint", "Back"))
        self.label.setText(_translate("BlindPrint", self.print_text[self.current_position - 35: self.current_position]))
        self.label.setFont(QtGui.QFont(self.font, self.font_size))
        self.label_2.setText(_translate("BlindPrint", self.print_text[self.current_position: self.current_position + 35]))
        self.label_2.setFont(QtGui.QFont(self.font, self.font_size))
        self.label.setText(_translate("BlindPrint", ""))
        self.tool_button.setText(_translate("BlindPrint", "..."))
        self.push_button_pronounce.setText(_translate("BlindPrint", "Pronounce"))
        self.profileOpenButton.setText(_translate("BlindPrint", "Profile"))
        self.pushButton.setText(_translate("BlindPrint", "Add to vocab"))
        self.pushButton_2.setText(_translate("BlindPrint", "Translate"))
        self.pushButton_start_lesson.setText(_translate("BlindPrint", "Start"))
        self.pushButton_stop_lesson.setText(_translate("BlindPrint", "Stop"))

    def lesson_start(self):
        self.keyboard_thread.start()
        self.keyboard_thread.pause_off()
        self.time_thread.pause_off(self.comboBox.currentText())
        update_user_info('lesson_time', self.comboBox.currentText(), self.user_id)

    def lesson_stop(self):
        if not self.pause_status:
            self.open_pause_menu(self.correct_print_count, self.print_errors, self.current_lesson_time)
        if self.pause_status:
            self.window2.close()
        self.pause_status = True
        self.time_thread.pause_thr()
        update_user_info('current_position', self.current_position, self.user_id)

    def post_stop(self):
        self.correct_print_count = 0
        self.print_errors = 0
        self.keyboard_thread.pause_thr()

    def keyboard_stop(self):
        self.keyboard_thread.pause_thr()

    def send_to_lcd(self, time):
        self.current_lesson_time = time
        time_minutes = str(time // 60)
        if len(time_minutes) == 1:
            time_minutes = '0' + time_minutes
        time_seconds = str(time % 60)
        if len(time_seconds) == 1:
            time_seconds = '0' + time_seconds
        formate_time = time_minutes + ':' + time_seconds
        self.lcdNumber_2.display(formate_time)
        self.format_lesson_time = formate_time

    def print_key(self, value):
        self.pause_status = False
        self.time_thread.start()
        self.time_thread.pause_off(self.comboBox.currentText())
        self.label_current_word.setText(self.current_word)
        if len(self.print_text) <= self.current_position:
            self.print_text, self.current_position = "The_End", 0
            self.lesson_stop()
        elif value == self.print_text[self.current_position]:
            self.correct_print_count += 1
            if self.current_position > 30:
                self.label.setText(self.print_text[self.current_position - 23: self.current_position + 1])
                self.label_2.setText(self.print_text[self.current_position + 1: self.current_position + 35])
            else:
                self.label.setText(self.print_text[:self.current_position + 1])
                self.label_2.setText(self.print_text[self.current_position + 1: self.current_position + 35])
            self.current_position += 1
        else:
            if value != '':
                self.print_errors += 1
        print(self.correct_print_count, self.print_errors)
        self.current_word = current_word(self.current_position, self.print_text)

    def get_text(self, path, BlindPrint, filters, custom_filters, current_position=None):
        if custom_filters == 'None':
            custom_filters = None
        if current_position:
            self.current_position = current_position
        print_text = open_text_file(path)
        self.print_text = leave_good_symbols(print_text, filters)
        if custom_filters:
            update_user_info('custom_filter_is_enabled', 1, self.user_id)
            filters_list = [symbol for symbol in custom_filters]
            filters_set = set(filters_list)
            self.print_text = cut_bad_symbols(self.print_text, filters_set)
        else:
            update_user_info('custom_filter_is_enabled', 0, self.user_id)
        self.retranslateUi(BlindPrint)

    def pronounce(self):
        get_and_play_audio(self.current_word)

    def font_change(self, font):
        self.label.setFont(font)
        self.label_2.setFont(font)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BlindPrint = QtWidgets.QMainWindow()
    ui = Ui_BlindPrint()
    ui.setupUi(BlindPrint)
    BlindPrint.show()
    sys.exit(app.exec_())
