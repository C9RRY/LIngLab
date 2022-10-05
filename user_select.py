from PyQt5 import QtCore, QtGui, QtWidgets
from database import get_user_list, pin_user, check_current_user
from user_create import Ui_UserCreate
from user import Ui_User


class Ui_UserSelect(object):
    def open_user_create(self, user, UserSelect):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_UserCreate()
        self.ui.setupUi(self.window, user, Ui_UserSelect)
        self.window.show()
        UserSelect.close()

    def open_user(self, UserSelect):
        pin_user(self.comboBox.currentText())
        self.user = check_current_user()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_User()
        self.ui.setupUi(self.window, self.user, Ui_UserSelect)
        self.window.show()
        self.UserSelect.close()

    def setupUi(self, UserSelect, user):
        self.UserSelect = UserSelect
        self.user = user
        UserSelect.setObjectName("UserSelect")
        UserSelect.resize(270, 128)
        UserSelect.setStyleSheet("background-color: rgb(65, 91, 93);")
        self.centralwidget = QtWidgets.QWidget(UserSelect)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(30, 20, 211, 27))
        self.comboBox.setStyleSheet("background-color: rgb(153, 193, 241);")
        self.comboBox.setObjectName("comboBox")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget,
                                                clicked=lambda: self.open_user(UserSelect))
        self.pushButton.setGeometry(QtCore.QRect(20, 80, 91, 27))
        self.pushButton.setStyleSheet("background-color: rgb(98, 160, 234);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget,
                                                clicked=lambda: self.open_user_create(self.user, UserSelect))
        self.pushButton_2.setGeometry(QtCore.QRect(160, 80, 91, 27))
        self.pushButton_2.setStyleSheet("background-color: rgb(98, 160, 234);")
        self.pushButton_2.setObjectName("pushButton_2")
        UserSelect.setCentralWidget(self.centralwidget)
        for user in get_user_list():
            self.comboBox.addItem(user[1])
        self.retranslateUi(UserSelect)
        QtCore.QMetaObject.connectSlotsByName(UserSelect)

    def retranslateUi(self, UserSelect):
        _translate = QtCore.QCoreApplication.translate
        UserSelect.setWindowTitle(_translate("UserSelect", "MainWindow"))
        self.pushButton.setText(_translate("UserSelect", "OK"))
        self.pushButton_2.setText(_translate("UserSelect", "New User"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UserSelect = QtWidgets.QMainWindow()
    ui = Ui_UserSelect()
    ui.setupUi(UserSelect)
    UserSelect.show()
    sys.exit(app.exec_())
