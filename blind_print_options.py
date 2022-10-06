from PyQt5 import QtCore, QtGui, QtWidgets
from database import update_user_info, check_current_user

class Ui_BlindPrintSettings(object):
    def setupUi(self, BlindPrintSettings, BlindPrint, get_text, font_change, user):
        user = check_current_user()
        self.user_id = user['id']
        self.font_size = user['font_size']
        self.text_filter = user['text_filter']
        self.custom_filter = user['custom_filter']
        self.font_change = font_change
        self.get_text = get_text
        self.file_path = user['text']
        BlindPrintSettings.setObjectName("BlindPrintSettings")
        BlindPrintSettings.resize(352, 464)
        BlindPrintSettings.setStyleSheet("background-color: rgb(102, 111, 108);")
        self.centralwidget = QtWidgets.QWidget(BlindPrintSettings)
        self.centralwidget.setObjectName("centralwidget")
        self.toolButton_file_change = QtWidgets.QToolButton(self.centralwidget,
                                                            clicked=lambda: self.open_file(BlindPrintSettings))
        self.toolButton_file_change.setGeometry(QtCore.QRect(20, 120, 31, 31))
        self.toolButton_file_change.setStyleSheet("background-color: rgb(205, 171, 143);")
        self.toolButton_file_change.setObjectName("toolButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.file_name_for_label = 'file path'
        self.label.setGeometry(QtCore.QRect(70, 130, 250, 21))
        self.label.setStyleSheet("background-color: rgb(71, 94, 87);")
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 330, 171, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.fontComboBox = QtWidgets.QFontComboBox(self.centralwidget)
        self.fontComboBox.setGeometry(QtCore.QRect(20, 20, 181, 27))
        self.fontComboBox.setStyleSheet("background-color: rgb(218, 188, 154);")
        self.fontComboBox.setObjectName("fontComboBox")
        self.push_button_translate_it = QtWidgets.QPushButton(self.centralwidget)
        self.push_button_translate_it.setGeometry(QtCore.QRect(10, 330, 171, 27))
        self.push_button_translate_it.setStyleSheet("background-color: rgb(181, 131, 90);")
        self.push_button_translate_it.setObjectName("push_button_translate_it")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 280, 291, 27))
        self.lineEdit_2.setStyleSheet("background-color: rgb(71, 94, 87);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(30, 170, 110, 25))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(170, 170, 141, 25))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setChecked(True)
        self.radioButton_3.setGeometry(QtCore.QRect(30, 200, 110, 25))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(170, 200, 110, 25))
        self.radioButton_4.setObjectName("radioButton_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 191, 19))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.clicked.connect(lambda: self.close_and_submit(BlindPrintSettings, BlindPrint))
        self.pushButton.setGeometry(QtCore.QRect(240, 410, 88, 27))
        self.pushButton.setStyleSheet("background-color: rgb(152, 106, 68);")
        self.pushButton.setObjectName("pushButton")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(30, 380, 71, 31))
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 390, 67, 19))
        self.label_3.setObjectName("label_3")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(20, 250, 171, 25))
        self.checkBox.setStyleSheet("color: rgb(246, 245, 244);")
        self.checkBox.setObjectName("checkBox")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(200, 20, 51, 27))
        self.comboBox.setStyleSheet("background-color: rgb(218, 188, 154);")
        self.comboBox.setObjectName("comboBox")
        for font in range(8, 12):
            self.comboBox.addItem(str(font))
        for font in range(12, 30, 2):
            self.comboBox.addItem(str(font))
        for font in range(30, 50, 6):
            self.comboBox.addItem(str(font))
        BlindPrintSettings.setCentralWidget(self.centralwidget)

        self.retranslateUi(BlindPrintSettings)
        QtCore.QMetaObject.connectSlotsByName(BlindPrintSettings)

    def retranslateUi(self, BlindPrintSettings):
        _translate = QtCore.QCoreApplication.translate
        BlindPrintSettings.setWindowTitle(_translate("BlindPrintSettings", "MainWindow"))
        self.toolButton_file_change.setText(_translate("BlindPrintSettings", "..."))
        self.label.setText(_translate("BlindPrintSettings", self.file_path))
        self.push_button_translate_it.setText(_translate("BlindPrintSettings", "PASS"))
        self.radioButton.setText(_translate("BlindPrintSettings", "letter only"))
        self.radioButton_2.setText(_translate("BlindPrintSettings", "letter and digit"))
        self.radioButton_3.setText(_translate("BlindPrintSettings", "full text"))
        self.radioButton_4.setText(_translate("BlindPrintSettings", "symbols only"))
        self.label_2.setText(_translate("BlindPrintSettings", " Download text file"))
        self.pushButton.setText(_translate("BlindPrintSettings", "Back"))
        self.label_3.setText(_translate("BlindPrintSettings", " PASS"))
        self.checkBox.setText(_translate("BlindPrintSettings", "cut custom symbols"))
        self.comboBox.setCurrentText(str(self.font_size))
        self.lcdNumber.display('PASS')

    def open_file(self, BlindPrintSettings):

        self.file_path = QtWidgets.QFileDialog.getOpenFileName(filter='*.txt')[0]
        update_user_info('text', self.file_path, self.user_id)
        if len(self.file_path) > 15:
            self.file_name_for_label = self.file_path[:10] + ' ... ' + self.file_path[-20:]
        else:
            self.file_name_for_label = self.file_path[1:]
        self.retranslateUi(BlindPrintSettings)

    def check_text_filters(self):
        if self.radioButton.isChecked():
            return 'letter only'
        if self.radioButton_2.isChecked():
            return 'letter and digit'
        if self.radioButton_3.isChecked():
            return 'full text'
        if self.radioButton_4.isChecked():
            return 'symbols only'

    def close_and_submit(self, BlindPrintSettings, BlindPrint):
        if self.file_path:
            self.text_filter = self.check_text_filters()
            update_user_info('text_filter', self.text_filter, self.user_id)
            if self.checkBox.isChecked():
                self.custom_filter = self.lineEdit_2.text()
                update_user_info('custom_filter', self.custom_filter, self.user_id)
                filters_list = [symbol for symbol in self.custom_filter]
                filters_set = set(filters_list)
                self.get_text(self.file_path, BlindPrint, self.text_filter, filters_set)
            else:
                self.get_text(self.file_path, BlindPrint, self.text_filter)
        font = self.fontComboBox.currentFont()
        self.font_size = self.comboBox.currentText()
        update_user_info('font_size', self.font_size, self.user_id)
        font.setPointSize(int(self.font_size))
        self.font_change(font)
        BlindPrintSettings.close()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BlindPrintSettings = QtWidgets.QMainWindow()
    ui = Ui_BlindPrintSettings()
    ui.setupUi(BlindPrintSettings)
    BlindPrintSettings.show()
    sys.exit(app.exec_())
