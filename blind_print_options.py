from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BlindPrintSettings(object):
    def setupUi(self, BlindPrintSettings, BlindPrint, get_text, user):
        self.get_text = get_text
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
        BlindPrintSettings.setCentralWidget(self.centralwidget)

        self.retranslateUi(BlindPrintSettings)
        QtCore.QMetaObject.connectSlotsByName(BlindPrintSettings)

    def retranslateUi(self, BlindPrintSettings):
        _translate = QtCore.QCoreApplication.translate
        BlindPrintSettings.setWindowTitle(_translate("BlindPrintSettings", "MainWindow"))
        self.toolButton_file_change.setText(_translate("BlindPrintSettings", "..."))
        self.label.setText(_translate("BlindPrintSettings", f"{self.file_name_for_label}"))
        self.push_button_translate_it.setText(_translate("BlindPrintSettings", "Add words to dictionary"))
        self.radioButton.setText(_translate("BlindPrintSettings", "letter only"))
        self.radioButton_2.setText(_translate("BlindPrintSettings", "letter and digit"))
        self.radioButton_3.setText(_translate("BlindPrintSettings", "full text"))
        self.radioButton_4.setText(_translate("BlindPrintSettings", "symbols only"))
        self.label_2.setText(_translate("BlindPrintSettings", " Download text file"))
        self.pushButton.setText(_translate("BlindPrintSettings", "Back"))
        self.label_3.setText(_translate("BlindPrintSettings", " words"))
        self.checkBox.setText(_translate("BlindPrintSettings", "cut custom symbols"))

    def open_file(self, BlindPrintSettings):
        self.file_path = QtWidgets.QFileDialog.getOpenFileName(filter='*.txt')[0]
        if len(self.file_path) > 15:
            self.file_name_for_label = self.file_path[:10] + ' ... ' + self.file_path[-20:]
        else:
            self.file_name_for_label = self.file_path[1:]
        self.retranslateUi(BlindPrintSettings)

    def close_and_submit(self, BlindPrintSettings, BlindPrint):
        self.get_text(self.file_path, BlindPrint)
        BlindPrintSettings.close()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BlindPrintSettings = QtWidgets.QMainWindow()
    ui = Ui_BlindPrintSettings()
    ui.setupUi(BlindPrintSettings)
    BlindPrintSettings.show()
    sys.exit(app.exec_())
