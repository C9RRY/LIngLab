from PyQt5 import QtCore, QtGui, QtWidgets
from add_word import Ui_add_to_vocab
from database import my_vocab, change_the_progress, delete_from_vocab
from utils import get_and_play_audio


class Ui_Vocabulary(object):

    def setupUi(self, Vocabulary, MainWindow, user):
        # self.timer = QtCore.QTimer()
        # self.timer.timeout.connect(self.insert_into)
        self.Vocabulary = Vocabulary
        self.user = user
        Vocabulary.setObjectName("Vocabulary")
        Vocabulary.resize(599, 464)
        Vocabulary.setStyleSheet("background-color: rgb(205, 171, 143);")
        self.central_widget = QtWidgets.QWidget(Vocabulary)
        self.central_widget.setObjectName("central_widget")
        self.gridLayout = QtWidgets.QGridLayout(self.central_widget)
        self.gridLayout.setObjectName("gridLayout")
        self.push_button_delete_word = QtWidgets.QPushButton(self.central_widget, clicked=self.delete_word)
        self.push_button_delete_word.setStyleSheet("background-color: rgb(237, 51, 59);")
        self.push_button_delete_word.setObjectName("push_button_delete_word")
        self.gridLayout.addWidget(self.push_button_delete_word, 2, 3, 1, 1)
        self.table_words_widget = QtWidgets.QTableWidget(self.central_widget)
        self.table_words_widget.setStyleSheet("background-color: rgb(205, 171, 143);")
        self.table_words_widget.setObjectName("table_words_widget")
        self.table_words_widget.setColumnCount(4)
        self.table_words_widget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        item.setFont(font)
        item.setBackground(QtGui.QColor(181, 131, 90))
        self.table_words_widget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        item.setFont(font)
        item.setBackground(QtGui.QColor(152, 106, 68))
        self.table_words_widget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        item.setFont(font)
        item.setBackground(QtGui.QColor(134, 94, 60))
        self.table_words_widget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(134, 94, 60))
        self.table_words_widget.setHorizontalHeaderItem(3, item)
        self.table_words_widget.horizontalHeader().setCascadingSectionResizes(False)
        self.gridLayout.addWidget(self.table_words_widget, 3, 0, 1, 3)
        self.grid_layout1 = QtWidgets.QGridLayout()
        self.grid_layout1.setContentsMargins(-1, 1, -1, -1)
        self.grid_layout1.setObjectName("grid_layout1")
        spacerItem = QtWidgets.QSpacerItem(20, 58, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.grid_layout1.addItem(spacerItem, 2, 0, 1, 1)
        self.lcd_words_count = QtWidgets.QLCDNumber(self.central_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcd_words_count.sizePolicy().hasHeightForWidth())
        self.lcd_words_count.setSizePolicy(sizePolicy)
        self.lcd_words_count.setMinimumSize(QtCore.QSize(100, 50))
        self.lcd_words_count.setSmallDecimalPoint(False)
        self.lcd_words_count.setDigitCount(5)
        self.lcd_words_count.setProperty("intValue", 0)
        self.lcd_words_count.setObjectName("lcd_words_count")
        self.grid_layout1.addWidget(self.lcd_words_count, 2, 4, 1, 1)
        self.profile_open_button = QtWidgets.QPushButton(self.central_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.profile_open_button.sizePolicy().hasHeightForWidth())
        self.profile_open_button.setSizePolicy(sizePolicy)
        self.profile_open_button.setMinimumSize(QtCore.QSize(80, 30))
        self.profile_open_button.setMaximumSize(QtCore.QSize(100, 30))
        self.profile_open_button.setObjectName("profile_open_button")
        self.grid_layout1.addWidget(self.profile_open_button, 2, 6, 1, 1)
        self.label_word_size = QtWidgets.QLabel(self.central_widget)
        self.label_word_size.setObjectName("label_word_size")
        self.grid_layout1.addWidget(self.label_word_size, 2, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.grid_layout1.addItem(spacerItem1, 2, 5, 1, 1)
        self.gridLayout.addLayout(self.grid_layout1, 0, 1, 1, 3)
        self.vertical_layout = QtWidgets.QVBoxLayout()
        self.vertical_layout.setObjectName("vertical_layout")
        self.microfone_button = QtWidgets.QToolButton(self.central_widget)
        self.microfone_button.setObjectName("microfone_button")
        self.vertical_layout.addWidget(self.microfone_button)
        spacerItem2 = QtWidgets.QSpacerItem(25, 9, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.vertical_layout.addItem(spacerItem2)
        self.gridLayout.addLayout(self.vertical_layout, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 3, 3, 1, 1)
        self.push_button_zero_out_progres = QtWidgets.QPushButton(self.central_widget, clicked=self.set_zero_progress)
        self.push_button_zero_out_progres.setStyleSheet("background-color: rgb(246, 97, 81);")
        self.push_button_zero_out_progres.setObjectName("push_button_zero_out_progres")
        self.gridLayout.addWidget(self.push_button_zero_out_progres, 1, 3, 1, 1)
        self.push_button_back = QtWidgets.QPushButton(self.central_widget)
        self.push_button_back.clicked.connect(MainWindow.show)
        self.push_button_back.clicked.connect(Vocabulary.close)
        self.push_button_back.setObjectName("push_button_back")
        self.gridLayout.addWidget(self.push_button_back, 4, 3, 1, 1)
        self.push_button_save_word = QtWidgets.QPushButton(self.central_widget, clicked=self.open_new_windows)
        self.push_button_save_word.clicked.connect(self.open_new_windows)
        self.push_button_save_word.setStyleSheet("background-color: rgb(181, 131, 90);")
        self.push_button_save_word.setObjectName("push_button_save_word")
        self.gridLayout.addWidget(self.push_button_save_word, 1, 2, 1, 1)

        self.lineEdit = QtWidgets.QLineEdit(self.central_widget)
        self.lineEdit.setStyleSheet("background-color: rgb(205, 171, 143);")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 2)
        self.comboBox = QtWidgets.QComboBox(self.central_widget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 2, 0, 1, 2)
        Vocabulary.setCentralWidget(self.central_widget)
        self.retranslateUi(Vocabulary)
        # self.timer.start(1000)
        QtCore.QMetaObject.connectSlotsByName(Vocabulary)

    def open_new_windows(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_add_to_vocab()
        self.ui.setupUi(self.window, self.Vocabulary, self.user, self.lineEdit.text(), lambda: self.insert_into())
        self.window.show()

    def retranslateUi(self, Vocabulary):
        _translate = QtCore.QCoreApplication.translate
        Vocabulary.setWindowTitle(_translate("Vocabulary", "Translate"))
        self.push_button_delete_word.setText(_translate("Vocabulary", "Delete"))
        item = self.table_words_widget.horizontalHeaderItem(0)
        item.setText(_translate("Vocabulary", "word"))
        item = self.table_words_widget.horizontalHeaderItem(1)
        item.setText(_translate("Vocabulary", "translate"))
        item = self.table_words_widget.horizontalHeaderItem(2)
        item.setText(_translate("Vocabulary", "progress"))
        self.profile_open_button.setText(_translate("Vocabulary", "Profile"))
        self.label_word_size.setText(_translate("Vocabulary", "Current vocabulary size"))
        self.microfone_button.setText(_translate("Vocabulary", "..."))
        self.push_button_zero_out_progres.setText(_translate("Vocabulary", "Zero out progress"))
        self.push_button_back.setText(_translate("Vocabulary", "Back"))
        self.push_button_save_word.setText(_translate("Vocabulary", "Save to vocab"))
        self.insert_into()

        # clicked word in the table
        self.table_words_widget.cellClicked.connect(self.selected_rows)

    def selected_rows(self, row, col):
        if col == 0:
            get_and_play_audio(self.table_words_widget.item(row, 0).text())

        # insert data into word_table
    def insert_into(self):
        words = my_vocab(1)
        row = 0
        self.table_words_widget.setRowCount(len(words))
        self.lcd_words_count.display(self.table_words_widget.rowCount())
        for word in words:
            item = QtWidgets.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
            item.setCheckState(QtCore.Qt.CheckState.Unchecked)

            self.table_words_widget.setItem(row, 0, QtWidgets.QTableWidgetItem(word[0]))
            self.table_words_widget.setItem(row, 1, QtWidgets.QTableWidgetItem(word[1]))
            self.table_words_widget.setItem(row, 2, QtWidgets.QTableWidgetItem(word[3]))
            self.table_words_widget.setItem(row, 3, item)
            row += 1

    def set_zero_progress(self):
        for row in range(self.table_words_widget.rowCount()):
            if self.table_words_widget.item(row, 3).checkState() == QtCore.Qt.CheckState.Checked:
                change_the_progress(self.table_words_widget.item(row, 1).text(), self.user, '*')
        self.insert_into()

    def delete_word(self):
        for row in range(self.table_words_widget.rowCount()):
            if self.table_words_widget.item(row, 3).checkState() == QtCore.Qt.CheckState.Checked:
                delete_from_vocab(self.table_words_widget.item(row, 1).text(), self.user)
        self.insert_into()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Vocabulary = QtWidgets.QMainWindow()
    ui = Ui_Vocabulary()
    ui.setupUi(Vocabulary)
    Vocabulary.show()
    sys.exit(app.exec_())
