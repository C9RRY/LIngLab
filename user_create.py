from PyQt5 import QtCore, QtGui, QtWidgets
from database import new_user, check_current_user
from user import Ui_User


class Ui_UserCreate(object):
    def open_user(self, UserSelect):
        name = self.lineEdit.text()
        new_user(name)
        self.user = check_current_user()
        self.update_main()
        self.UserCreate.close()

    def setupUi(self, UserCreate, user, UserSelect, update_main):
        self.update_main = update_main
        self.UserSelect = UserSelect
        self.UserCreate = UserCreate
        UserCreate.setObjectName("UserCreate")
        UserCreate.resize(270, 128)
        UserCreate.setStyleSheet("background-color: rgb(65, 91, 93);")
        self.centralwidget = QtWidgets.QWidget(UserCreate)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget,
                                                clicked=lambda: self.open_user(UserSelect))
        self.pushButton.setGeometry(QtCore.QRect(160, 80, 91, 27))
        self.pushButton.setStyleSheet("background-color: rgb(98, 160, 234);")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(40, 40, 201, 27))
        self.lineEdit.setStyleSheet("background-color: rgb(153, 193, 241);")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 81, 19))
        self.label.setObjectName("label")
        UserCreate.setCentralWidget(self.centralwidget)

        self.retranslateUi(UserCreate)
        QtCore.QMetaObject.connectSlotsByName(UserCreate)

    def retranslateUi(self, UserCreate):
        _translate = QtCore.QCoreApplication.translate
        UserCreate.setWindowTitle(_translate("UserCreate", "MainWindow"))
        self.pushButton.setText(_translate("UserCreate", "OK"))
        self.label.setText(_translate("UserCreate", "UserName"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UserCreate = QtWidgets.QMainWindow()
    ui = Ui_UserCreate()
    ui.setupUi(UserCreate)
    UserCreate.show()
    sys.exit(app.exec_())
