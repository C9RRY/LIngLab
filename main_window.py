from PyQt5 import QtCore, QtGui, QtWidgets
from lessons_choice import Ui_LessonChoice
from vocabulary import Ui_Vocabulary
from blind_print import Ui_BlindPrint
from user import Ui_User
from user_select import Ui_UserSelect
from database import check_current_user


class Ui_MainWindow(object):
    def open_new_windows(self, ui_name):
        self.window = QtWidgets.QMainWindow()
        self.ui = ui_name
        self.ui.setupUi(self.window, MainWindow, self.user)
        MainWindow.hide()
        self.window.show()

    def open_profile(self, UserSelect):
        self.user = check_current_user()
        self.window = QtWidgets.QMainWindow()
        if self.user["id"] == 1:
            self.ui = Ui_UserSelect()
            self.ui.setupUi(self.window, self.user, lambda: self.update_main() )
        else:
            self.ui = Ui_User()
            self.ui.setupUi(self.window, self.user, UserSelect, lambda: self.update_main())
        self.window.show()
        self.retranslateUi(MainWindow)

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 450)
        MainWindow.setStyleSheet("background-color: rgb(53, 132, 228);")
        self.user = check_current_user()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(-1, 1, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.profileOpenButton = QtWidgets.QPushButton(self.centralwidget,
                                                       clicked=lambda: self.open_profile(Ui_UserSelect))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.profileOpenButton.sizePolicy().hasHeightForWidth())
        self.profileOpenButton.setSizePolicy(sizePolicy)
        self.profileOpenButton.setMinimumSize(QtCore.QSize(80, 30))
        self.profileOpenButton.setMaximumSize(QtCore.QSize(100, 30))
        self.profileOpenButton.setObjectName("profileOpenButton")
        self.gridLayout_2.addWidget(self.profileOpenButton, 1, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 58, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 1, 1, 1, 1)
        self.user_info_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(True)
        self.user_info_label.setFont(font)
        self.user_info_label.setObjectName("user_info_label")
        self.gridLayout_2.addWidget(self.user_info_label, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 2, 1, 3)
        spacerItem4 = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 4, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.grammarOpenButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grammarOpenButton.sizePolicy().hasHeightForWidth())
        self.grammarOpenButton.setSizePolicy(sizePolicy)
        self.grammarOpenButton.setMaximumSize(QtCore.QSize(700, 60))
        self.grammarOpenButton.setStyleSheet("background-color: rgb(46, 194, 126);")
        self.grammarOpenButton.setObjectName("grammarOpenButton")
        self.gridLayout_3.addWidget(self.grammarOpenButton, 4, 0, 1, 1)
        self.blindPrintOpenButton = QtWidgets.QPushButton(self.centralwidget,
                                                          clicked=lambda: self.open_new_windows(Ui_BlindPrint()))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blindPrintOpenButton.sizePolicy().hasHeightForWidth())
        self.blindPrintOpenButton.setSizePolicy(sizePolicy)
        self.blindPrintOpenButton.setMaximumSize(QtCore.QSize(700, 60))
        self.blindPrintOpenButton.setStyleSheet("background-color: rgb(87, 227, 137);")
        self.blindPrintOpenButton.setObjectName("blindPrintOpenButton")
        self.gridLayout_3.addWidget(self.blindPrintOpenButton, 2, 0, 1, 1)
        self.wokabularyOpenButton = QtWidgets.QPushButton(self.centralwidget,
                                                          clicked=lambda: self.open_new_windows(Ui_Vocabulary()))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wokabularyOpenButton.sizePolicy().hasHeightForWidth())
        self.wokabularyOpenButton.setSizePolicy(sizePolicy)
        self.wokabularyOpenButton.setMaximumSize(QtCore.QSize(700, 60))
        self.wokabularyOpenButton.setStyleSheet("background-color: rgb(143, 240, 164);")
        self.wokabularyOpenButton.setObjectName("wokabularyOpenButton")
        self.gridLayout_3.addWidget(self.wokabularyOpenButton, 0, 0, 1, 1)
        self.lessonChoiceOpenButton = QtWidgets.QPushButton(self.centralwidget,
                                                            clicked=lambda: self.open_new_windows(Ui_LessonChoice()))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lessonChoiceOpenButton.sizePolicy().hasHeightForWidth())
        self.lessonChoiceOpenButton.setSizePolicy(sizePolicy)
        self.lessonChoiceOpenButton.setMaximumSize(QtCore.QSize(700, 60))
        self.lessonChoiceOpenButton.setStyleSheet("background-color: rgb(51, 209, 122);")
        self.lessonChoiceOpenButton.setObjectName("lessonChoiceOpenButton")
        self.gridLayout_3.addWidget(self.lessonChoiceOpenButton, 3, 0, 1, 1)
        self.passButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passButton.sizePolicy().hasHeightForWidth())
        self.passButton.setSizePolicy(sizePolicy)
        self.passButton.setMaximumSize(QtCore.QSize(700, 60))
        self.passButton.setStyleSheet("background-color: rgb(38, 162, 105);")
        self.passButton.setObjectName("passButton")
        self.gridLayout_3.addWidget(self.passButton, 5, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 1, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(15, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem4, 2, 3, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem5 = QtWidgets.QSpacerItem(25, 9, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem5)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MyLearn"))
        self.profileOpenButton.setText(_translate("MainWindow", "Profile"))
        self.user_info_label.setText(_translate("MainWindow", self.user['user_name']))
        self.grammarOpenButton.setText(_translate("MainWindow", "Grammar"))
        self.blindPrintOpenButton.setText(_translate("MainWindow", "Blind print"))
        self.wokabularyOpenButton.setText(_translate("MainWindow", "Wokabulary"))
        self.lessonChoiceOpenButton.setText(_translate("MainWindow", "Lessons"))
        self.passButton.setText(_translate("MainWindow", "Pass"))

    def update_main(self):
        self.user = check_current_user()
        self.retranslateUi(MainWindow)

    def check_auth(self):
        self.user = check_current_user()
        if self.user['id'] == 0:
            self.open_new_windows(Ui_UserSelect())
        else:
            self.open_new_windows(Ui_User())


if __name__ == "__main__":
    from models import create_all
    import sys

    create_all()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
