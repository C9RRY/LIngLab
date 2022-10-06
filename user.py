from PyQt5 import QtCore, QtGui, QtWidgets
from database import check_current_user, log_out


class Ui_User(object):
    def open_user_select(self, UserSelect):
        log_out()
        self.update_main()

    def setupUi(self, User, user, UserSelect, update_main):
        self.update_main = update_main
        self.User = User
        self.UserSelect = UserSelect
        self.user = user
        User.resize(253, 381)
        User.setStyleSheet("background-color: rgb(65, 91, 93);")
        self.centralwidget = QtWidgets.QWidget(User)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 20, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 241, 31))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 241, 31))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 140, 241, 31))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 180, 241, 31))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 220, 241, 31))
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 260, 241, 31))
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 300, 241, 31))
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(180, 340, 71, 31))
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 340, 161, 31))
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.logOut = QtWidgets.QPushButton(self.centralwidget,
                                            clicked=lambda: self.open_user_select(UserSelect))
        self.logOut.clicked.connect(User.close)
        self.logOut.setGeometry(QtCore.QRect(10, 20, 61, 21))
        self.logOut.setStyleSheet("background-color: rgb(154, 153, 150);")
        self.logOut.setObjectName("logOut")
        User.setCentralWidget(self.centralwidget)

        self.retranslateUi(User)
        QtCore.QMetaObject.connectSlotsByName(User)

    def retranslateUi(self, User):
        _translate = QtCore.QCoreApplication.translate
        User.setWindowTitle(_translate("User", "MainWindow"))
        self.label.setText(_translate("User", self.user['user_name']))
        self.label_2.setText(_translate("User", "pass"))
        self.label_3.setText(_translate("User", "pass"))
        self.label_4.setText(_translate("User", "pass"))
        self.label_5.setText(_translate("User", "pass"))
        self.label_6.setText(_translate("User", "pass"))
        self.label_7.setText(_translate("User", "pass"))
        self.label_8.setText(_translate("User", "pass"))
        self.label_9.setText(_translate("User", "pass"))
        self.logOut.setText(_translate("User", "log out"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    User = QtWidgets.QMainWindow()
    ui = Ui_User()
    ui.setupUi(User)
    User.show()
    sys.exit(app.exec_())
