from PyQt5 import QtCore, QtGui, QtWidgets
from database import update_user_info, check_current_user, get_print_sessions, delete_record


class Ui_BlindPrintSettings(object):
    def setupUi(self, BlindPrintSettings, BlindPrint, get_text, font_change, update_user, user):
        user = check_current_user()
        self.update_user = update_user
        self.user_id = user['id']
        self.font = user['font']
        self.font_size = user['font_size']
        self.text_filter = user['text_filter']
        self.custom_filter = user['custom_filter']
        self.custom_filters_is_enabled = user['custom_filter_is_enabled']
        self.font_change = font_change
        self.get_text = get_text
        self.file_path = user['text']
        self.current_position = user['current_position']

        BlindPrintSettings.setObjectName("BlindPrintSettings")
        BlindPrintSettings.resize(341, 490)
        BlindPrintSettings.setStyleSheet("background-color: rgb(102, 111, 108);")
        self.centralwidget = QtWidgets.QWidget(BlindPrintSettings)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 341, 491))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(13, 20, 311, 380))
        self.tableWidget.setStyleSheet("color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setColumnWidth(0, 85)
        self.tableWidget.setColumnWidth(1, 55)
        self.tableWidget.setColumnWidth(2, 55)
        self.tableWidget.setColumnWidth(3, 50)
        self.tableWidget.setColumnWidth(4, 20)
        self.tableWidget.setColumnWidth(5, 20)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.delete_pinned = QtWidgets.QPushButton(self.tab)
        self.delete_pinned.clicked.connect(lambda: self.delete_record(BlindPrintSettings))
        self.delete_pinned.setGeometry(QtCore.QRect(247, 410, 81, 27))
        self.delete_pinned.setStyleSheet("background-color: rgb(152, 106, 68);")
        self.delete_pinned.setObjectName("delete_pinned")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(250, 330, 71, 27))
        self.lineEdit_3.setStyleSheet("background-color: rgb(71, 94, 87);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.radioButton = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton.setChecked(True if self.text_filter == 'letter only' else False)
        self.radioButton.setGeometry(QtCore.QRect(30, 170, 110, 25))
        self.radioButton.setObjectName("radioButton")
        self.fontComboBox = QtWidgets.QFontComboBox(self.tab_2)
        self.fontComboBox.setGeometry(QtCore.QRect(20, 20, 181, 27))
        self.fontComboBox.setStyleSheet("background-color: rgb(218, 188, 154);")
        self.fontComboBox.setObjectName("fontComboBox")
        self.push_button_translate_it = QtWidgets.QPushButton(self.tab_2)
        self.push_button_translate_it.clicked.connect(lambda: self.set_current_position(BlindPrintSettings))
        self.push_button_translate_it.setGeometry(QtCore.QRect(10, 330, 171, 27))
        self.push_button_translate_it.setStyleSheet("background-color: rgb(181, 131, 90);")
        self.push_button_translate_it.setObjectName("push_button_translate_it")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setText(self.custom_filter if self.custom_filter != 'None' else None)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 280, 291, 27))
        self.lineEdit_2.setStyleSheet("background-color: rgb(71, 94, 87);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.checkBox = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox.setGeometry(QtCore.QRect(20, 250, 171, 25))
        self.checkBox.setStyleSheet("color: rgb(246, 245, 244);")
        self.checkBox.setObjectName("checkBox")
        self.lcdNumber = QtWidgets.QLCDNumber(self.tab_2)
        self.lcdNumber.setDigitCount(7)
        self.lcdNumber.setGeometry(QtCore.QRect(30, 380, 71, 31))
        self.lcdNumber.setObjectName("lcdNumber")
        self.toolButton = QtWidgets.QToolButton(self.tab_2,
                                                            clicked=lambda: self.open_file(BlindPrintSettings))
        self.toolButton.setGeometry(QtCore.QRect(20, 120, 31, 31))
        self.toolButton.setStyleSheet("background-color: rgb(205, 171, 143);")
        self.toolButton.setObjectName("toolButton")
        self.radioButton_4 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_4.setChecked(True if self.text_filter == 'symbols only' else False)
        self.radioButton_4.setGeometry(QtCore.QRect(170, 200, 110, 25))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_2 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_2.setChecked(True if self.text_filter == 'letter and digit' else False)
        self.radioButton_2.setGeometry(QtCore.QRect(170, 170, 141, 25))
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(110, 390, 67, 19))
        self.label_3.setObjectName("label_3")
        self.radioButton_3 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_3.setChecked(True if self.text_filter == 'full text' else False)
        self.radioButton_3.setGeometry(QtCore.QRect(30, 200, 110, 25))
        self.radioButton_3.setObjectName("radioButton_3")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(70, 130, 221, 21))
        self.label.setStyleSheet("background-color: rgb(71, 94, 87);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 191, 19))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.tab_2)
        self.comboBox.setGeometry(QtCore.QRect(200, 20, 51, 27))
        self.comboBox.setStyleSheet("background-color: rgb(218, 188, 154);")
        self.comboBox.setObjectName("comboBox")
        for font in range(8, 12):
            self.comboBox.addItem(str(font))
        for font in range(12, 30, 2):
            self.comboBox.addItem(str(font))
        for font in range(30, 50, 6):
            self.comboBox.addItem(str(font))
        for font in range(50, 80, 12):
            self.comboBox.addItem(str(font))
        self.comboBox.setCurrentText(str(self.font_size))
        self.fontComboBox.setCurrentText(self.font)
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.clicked.connect(lambda: self.close_and_submit(BlindPrintSettings, BlindPrint))
        self.pushButton.setGeometry(QtCore.QRect(240, 410, 88, 27))
        self.pushButton.setStyleSheet("background-color: rgb(152, 106, 68);")
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tab_2, "")
        BlindPrintSettings.setCentralWidget(self.centralwidget)

        self.retranslateUi(BlindPrintSettings)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(BlindPrintSettings)

    def retranslateUi(self, BlindPrintSettings):
        _translate = QtCore.QCoreApplication.translate
        BlindPrintSettings.setWindowTitle(_translate("BlindPrintSettings", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("BlindPrintSettings", "date"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("BlindPrintSettings", "temp"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("BlindPrintSettings", "errors"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("BlindPrintSettings", "time"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("BlindPrintSettings", "id"))
        self.delete_pinned.setText(_translate("BlindPrintSettings", "Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("BlindPrintSettings", "Statistic"))
        self.radioButton.setText(_translate("BlindPrintSettings", "letter only"))
        self.push_button_translate_it.setText(_translate("BlindPrintSettings", "set current position"))
        self.checkBox.setText(_translate("BlindPrintSettings", "cut custom symbols"))
        self.toolButton.setText(_translate("BlindPrintSettings", "..."))
        self.radioButton_4.setText(_translate("BlindPrintSettings", "symbols only"))
        self.radioButton_2.setText(_translate("BlindPrintSettings", "letter and digit"))
        self.label_3.setText(_translate("BlindPrintSettings", " words"))
        self.radioButton_3.setText(_translate("BlindPrintSettings", "full text"))
        self.label.setText(_translate("BlindPrintSettings", self.file_path))
        self.label_2.setText(_translate("BlindPrintSettings", " Download text file"))
        self.pushButton.setText(_translate("BlindPrintSettings", "Back"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("BlindPrintSettings", "Options"))
        self.comboBox.setCurrentText(str(self.font_size))
        self.lcdNumber.display(self.current_position)
        self.insert_into()

    def insert_into(self):
        records = get_print_sessions(self.user_id)
        row = 0
        self.tableWidget.setRowCount(len(records))

        for record in records:
            item = QtWidgets.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
            item.setCheckState(QtCore.Qt.CheckState.Unchecked)

            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(record[2]))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(record[4]))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(record[6]))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(record[3]))
            self.tableWidget.setItem(row, 4, item)
            self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(record[0])))
            row += 1

    def delete_record(self, BlindPrint):
        for row in range(self.tableWidget.rowCount()):
            if self.tableWidget.item(row, 4).checkState() == QtCore.Qt.CheckState.Checked:
                delete_record(self.tableWidget.item(row, 5).text(), self.user_id)
        self.insert_into()
        self.retranslateUi(BlindPrint)

    def set_current_position(self, BlindPrintSettings):
        if self.lineEdit_3.text():
            try:
                self.current_position = int(self.lineEdit_3.text())
            except:
                pass
            update_user_info('current_position', self.current_position, self.user_id)
        self.retranslateUi(BlindPrintSettings)

    def open_file(self, BlindPrintSettings):
        file_path = QtWidgets.QFileDialog.getOpenFileName(filter='*.txt')[0]
        if self.file_path == file_path:
            pass
        else:
            self.file_path = file_path
            self.current_position = 0
            update_user_info('current_position', self.current_position, self.user_id)
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
        self.text_filter = self.check_text_filters()
        update_user_info('text_filter', self.text_filter, self.user_id)
        if self.checkBox.isChecked():
            self.custom_filter = self.lineEdit_2.text()
            update_user_info('custom_filter_is_enabled', self.custom_filters_is_enabled, self.user_id)
        else:
            self.custom_filter = None
        update_user_info('custom_filter', self.custom_filter, self.user_id)
        self.font = self.fontComboBox.currentText()
        self.font_size = self.comboBox.currentText()
        font = QtGui.QFont(self.font, int(self.font_size))
        self.font_change(font)
        self.get_text(self.file_path, BlindPrint, self.text_filter, self.custom_filter, self.current_position)
        # font = self.fontComboBox.currentFont()

        update_user_info('font', self.font, self.user_id)
        update_user_info('font_size', self.font_size, self.user_id)
        self.update_user()
        BlindPrintSettings.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BlindPrintSettings = QtWidgets.QMainWindow()
    ui = Ui_BlindPrintSettings()
    ui.setupUi(BlindPrintSettings)
    BlindPrintSettings.show()
    sys.exit(app.exec_())
