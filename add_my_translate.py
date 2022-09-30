from PyQt5 import QtCore, QtGui, QtWidgets
from database import save_to_dict


class Ui_add_my_translate(object):
    def setupUi(self, add_my_translate, user, word, insert_into):
        add_my_translate.setObjectName("add_my_to_vocab")
        add_my_translate.resize(387, 135)
        add_my_translate.setStyleSheet("background-color: rgb(205, 171, 143);")
        self.user = user
        self.word = word
        self.insert_into = insert_into
        self.centralwidget = QtWidgets.QWidget(add_my_translate)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.push_button_save = QtWidgets.QPushButton(self.centralwidget)
        self.push_button_save.clicked.connect(self.save_my_variant)
        self.push_button_save.clicked.connect(add_my_translate.close)
        self.push_button_save.setObjectName("push_button_save")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.push_button_save)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.FieldRole, spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(2, QtWidgets.QFormLayout.LabelRole, spacerItem1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        add_my_translate.setCentralWidget(self.centralwidget)

        self.retranslateUi(add_my_translate)
        QtCore.QMetaObject.connectSlotsByName(add_my_translate)

    def save_my_variant(self, add_my_translate):
        save_to_dict(self.user, self.word, self.lineEdit.text())
        self.insert_into()

    def retranslateUi(self, add_my_translate):
        _translate = QtCore.QCoreApplication.translate
        add_my_translate.setWindowTitle(_translate("add_my_to_vocab", "MainWindow"))
        self.label.setText(_translate("add_my_to_vocab", f"{self.word}"))
        self.push_button_save.setText(_translate("add_my_to_vocab", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    add_my_to_vocab = QtWidgets.QMainWindow()
    ui = Ui_add_my_translate()
    ui.setupUi(add_my_to_vocab)
    add_my_to_vocab.show()
    sys.exit(app.exec_())
