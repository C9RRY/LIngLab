from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PauseMenu(object):
    def setupUi(self, PauseMenu, count, error, time):
        PauseMenu.setObjectName("PauseMenu")
        PauseMenu.resize(240, 135)
        PauseMenu.setStyleSheet("background-color: rgb(71, 94, 87);")
        self.centralwidget = QtWidgets.QWidget(PauseMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.display(str(error / (error + count) * 100)[:4] if error != 0 else '0')
        self.lcdNumber.setGeometry(QtCore.QRect(140, 90, 61, 23))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.display(str(count / time * 60)[:3] if time != 0 else "0")
        self.lcdNumber_2.setGeometry(QtCore.QRect(140, 50, 61, 23))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_3.display(str(count))
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 50, 41, 21))
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 90, 21, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_2.setObjectName("label_2")
        PauseMenu.setCentralWidget(self.centralwidget)

        self.retranslateUi(PauseMenu)
        QtCore.QMetaObject.connectSlotsByName(PauseMenu)


    def retranslateUi(self, PauseMenu):
        _translate = QtCore.QCoreApplication.translate
        PauseMenu.setWindowTitle(_translate("PauseMenu", "Pause"))
        self.label_printed.setText(_translate("PauseMenu", "Printed"))
        self.label_speed.setText(_translate("PauseMenu", "Speed"))
        self.label_errors.setText(_translate("PauseMenu", "Errors "))
        self.label.setText(_translate("PauseMenu", "%"))
        self.label_2.setText(_translate("PauseMenu", "%"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PauseMenu = QtWidgets.QMainWindow()
    ui = Ui_PauseMenu()
    ui.setupUi(PauseMenu)
    PauseMenu.show()
    sys.exit(app.exec_())
