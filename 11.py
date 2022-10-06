from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PauseMenu(object):
    def setupUi(self, PauseMenu, print_count, print_error, time, func_stop):
        self.print_count = print_count
        self.print_error = print_error
        self.time = time
        PauseMenu.setObjectName("PauseMenu")
        PauseMenu.resize(240, 175)
        PauseMenu.setStyleSheet("background-color: rgb(71, 94, 87);")
        self.centralwidget = QtWidgets.QWidget(PauseMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_continue = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: PauseMenu.close())
        self.pushButton_continue.setGeometry(QtCore.QRect(20, 130, 88, 27))
        self.pushButton_continue.setStyleSheet("background-color: rgb(154, 153, 150);")
        self.pushButton_continue.setObjectName("pushButton_continue")
        self.pushButton_break = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_break.clicked.connect(lambda: func_stop())
        self.pushButton_break.clicked.connect(PauseMenu.close)

        self.pushButton_break.setGeometry(QtCore.QRect(130, 130, 88, 27))
        self.pushButton_break.setStyleSheet("background-color: rgb(154, 153, 150);")
        self.pushButton_break.setObjectName("pushButton_break")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.display(str((self.print_count + self.print_error) / 100 * self.print_error)+'% ')
        self.lcdNumber.setGeometry(QtCore.QRect(140, 90, 61, 23))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.display(str(self.print_count / self.time)[:4]+'% ')
        self.lcdNumber_2.setGeometry(QtCore.QRect(140, 50, 61, 23))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_3.display(str(self.print_count))
        self.lcdNumber_3.setGeometry(QtCore.QRect(140, 10, 61, 23))
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.label_printed = QtWidgets.QLabel(self.centralwidget)
        self.label_printed.setGeometry(QtCore.QRect(30, 10, 67, 21))
        self.label_printed.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_printed.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_printed.setObjectName("label_printed")
        self.label_speed = QtWidgets.QLabel(self.centralwidget)
        self.label_speed.setGeometry(QtCore.QRect(30, 50, 67, 21))
        self.label_speed.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_speed.setObjectName("label_speed")
        self.label_errors = QtWidgets.QLabel(self.centralwidget)
        self.label_errors.setGeometry(QtCore.QRect(30, 90, 67, 21))
        self.label_errors.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_errors.setObjectName("label_errors")
        PauseMenu.setCentralWidget(self.centralwidget)

        self.retranslateUi(PauseMenu)
        QtCore.QMetaObject.connectSlotsByName(PauseMenu)

    def retranslateUi(self, PauseMenu):
        _translate = QtCore.QCoreApplication.translate
        PauseMenu.setWindowTitle(_translate("PauseMenu", "Pause"))
        self.pushButton_continue.setText(_translate("PauseMenu", "Continue"))
        self.pushButton_break.setText(_translate("PauseMenu", "Break"))
        self.label_printed.setText(_translate("PauseMenu", "Printed"))
        self.label_speed.setText(_translate("PauseMenu", "Speed"))
        self.label_errors.setText(_translate("PauseMenu", "Errors "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PauseMenu = QtWidgets.QMainWindow()
    ui = Ui_PauseMenu()
    ui.setupUi(PauseMenu)
    PauseMenu.show()
    sys.exit(app.exec_())
