from PyQt5 import QtCore, QtGui, QtWidgets
from new_thread import KeyboardThread
from utils import open_text_file, current_word, get_and_play_audio
from blind_print_options import Ui_BlindPrintSettings


class Ui_BlindPrint(object):
    def show_main(self, main_window, current_window):
        main_window.show()
        current_window.hide()

    def open_new_windows(self, ui_name, BlindPrint, get_text):
        self.window = QtWidgets.QMainWindow()
        self.ui = ui_name
        self.ui.setupUi(self.window, BlindPrint, get_text, self.user)
        self.window.show()
        # MainWindow.hide()

    def setupUi(self, BlindPrint, MainWindow, user):
        self.BlindPrint = BlindPrint
        self.current_position = 4000

        self.print_text = 'START'
        self.current_word = ' '
        self.timer = QtCore.QTimer()
        # self.timer.timeout.connect(self.print_key)
        self.thread = KeyboardThread
        self.user = user
        BlindPrint.setObjectName("BlindPrint")
        BlindPrint.resize(818, 458)
        BlindPrint.setStyleSheet("background-color: rgb(102, 111, 108);")
        self.centralwidget = QtWidgets.QWidget(BlindPrint)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(218, 188, 154);")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 9, 9, 1, 4)
        spacerItem = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 12, 8, 1, 1)
        self.push_button_back = QtWidgets.QPushButton(self.centralwidget,
                                                  clicked=lambda: self.show_main(MainWindow, BlindPrint))
        self.push_button_back.setStyleSheet("background-color: rgb(181, 131, 90);")
        self.push_button_back.setObjectName("push_button_back")
        self.gridLayout.addWidget(self.push_button_back, 13, 12, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 12, 10, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(15, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout.addItem(spacerItem2, 4, 10, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 12, 12, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(-1, 1, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButton.setStyleSheet("background-color: rgb(134, 94, 60);")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 1, 5, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 1, 10, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 1, 7, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 58, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 1, 0, 1, 2)
        self.push_button_pronounce = QtWidgets.QPushButton(self.centralwidget)
        self.push_button_pronounce.setFocusPolicy(QtCore.Qt.TabFocus)
        self.push_button_pronounce.clicked.connect(self.pronounce)
        self.push_button_pronounce.setStyleSheet("background-color: rgb(152, 106, 68);")
        self.push_button_pronounce.setObjectName("push_button_pronounce")
        self.gridLayout_2.addWidget(self.push_button_pronounce, 1, 4, 1, 1)
        self.profileOpenButton = QtWidgets.QPushButton(self.centralwidget)
        self.profileOpenButton.setFocusPolicy(QtCore.Qt.TabFocus)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.profileOpenButton.sizePolicy().hasHeightForWidth())
        self.profileOpenButton.setSizePolicy(sizePolicy)
        self.profileOpenButton.setMinimumSize(QtCore.QSize(80, 30))
        self.profileOpenButton.setMaximumSize(QtCore.QSize(100, 30))
        self.profileOpenButton.setStyleSheet("background-color: rgb(181, 131, 90);")
        self.profileOpenButton.setObjectName("profileOpenButton")
        self.gridLayout_2.addWidget(self.profileOpenButton, 1, 12, 1, 1)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setMinimumSize(QtCore.QSize(50, 50))
        self.lcdNumber_2.setStyleSheet("background-color: rgb(71, 94, 87);\n"
                                       "border-color: rgb(102, 111, 108);")
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.gridLayout_2.addWidget(self.lcdNumber_2, 1, 8, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem7, 1, 6, 1, 1)
        self.tool_button = QtWidgets.QToolButton(self.centralwidget,
                                                 clicked=lambda: self.open_new_windows(
                                                     Ui_BlindPrintSettings(), BlindPrint, self.get_text))
        self.tool_button.setStyleSheet("background-color: rgb(181, 131, 90);")
        self.tool_button.setObjectName("tool_button")
        self.gridLayout_2.addWidget(self.tool_button, 1, 11, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 2, 1, 11)
        self.label_current_word = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_current_word.setFont(font)
        self.label_current_word.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_current_word.setAlignment(QtCore.Qt.AlignCenter)
        self.label_current_word.setObjectName("label_current_word")
        self.gridLayout.addWidget(self.label_current_word, 1, 7, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(280, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 12, 7, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 12, 9, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 4, 12, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
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
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem11, 10, 12, 1, 1)
        BlindPrint.setCentralWidget(self.centralwidget)
        self.retranslateUi(BlindPrint)
        self.timer.start(100)
        QtCore.QMetaObject.connectSlotsByName(BlindPrint)
        self.keyboard_thread = KeyboardThread(mainwindow=self)
        self.keyboard_thread.start()

    def retranslateUi(self, BlindPrint):
        _translate = QtCore.QCoreApplication.translate
        BlindPrint.setWindowTitle(_translate("BlindPrint", "MyLearn"))
        self.push_button_back.setText(_translate("BlindPrint", "Back"))
        self.pushButton.setText(_translate("BlindPrint", "Add to vocab"))
        self.push_button_pronounce.setText(_translate("BlindPrint", "Pronounce"))
        self.profileOpenButton.setText(_translate("BlindPrint", "Profile"))
        self.tool_button.setText(_translate("BlindPrint", "..."))
        self.label_current_word.setText(_translate("BlindPrint", "Current"))
        self.label_2.setText(_translate("BlindPrint", self.print_text[self.current_position: self.current_position + 35]))
        self.label.setText(_translate("BlindPrint", self.print_text[self.current_position - 35: self.current_position]))

    def print_key(self, value):
        self.label_current_word.setText(self.current_word)
        if value == self.print_text[self.current_position]:
            self.label.setText(self.print_text[self.current_position - 30: self.current_position + 1])
            self.label_2.setText(self.print_text[self.current_position + 1: self.current_position + 35])
            self.current_position += 1
            self.current_word = current_word(self.current_position, self.print_text)
                                 #current position
    def get_text(self, path, BlindPrint):
        is self.current_position
        self.print_text = open_text_file(path)[self.current_position - 30:]
        self.retranslateUi(BlindPrint)

    def pronounce(self):
        get_and_play_audio(self.current_word)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BlindPrint = QtWidgets.QMainWindow()
    ui = Ui_BlindPrint()
    ui.setupUi(BlindPrint)
    BlindPrint.show()
    sys.exit(app.exec_())
