from PyQt5 import QtCore, QtGui, QtWidgets
from database import find_translation, add_word_to_user
from add_my_translate import Ui_add_my_translate


class Ui_add_to_vocab(object):
    def open_new_windows(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_add_my_translate()
        self.ui.setupUi(self.window, self.user, self.word, self.insert_into)
        self.window.show()

    def setupUi(self, add_to_vocab, Vocabulary, user, word, insert_into):
        self.user = user
        self.word = word
        self.insert_into = insert_into
        add_to_vocab.setObjectName("add_to_vocab")
        add_to_vocab.resize(387, 135)
        add_to_vocab.setStyleSheet("background-color: rgb(205, 171, 143);")
        self.centralwidget = QtWidgets.QWidget(add_to_vocab)
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
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.push_button_my_variant = QtWidgets.QPushButton(self.centralwidget,
                                                            clicked=lambda: self.open_new_windows())
        self.push_button_my_variant.clicked.connect(add_to_vocab.close)
        self.push_button_my_variant.setObjectName("push_button_my_variant")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.push_button_my_variant)
        self.push_button_save = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.clicker(user))
        self.push_button_save.clicked.connect(self.insert_into)
        self.push_button_save.clicked.connect(add_to_vocab.close)
        self.push_button_save.setObjectName("push_button_save")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.push_button_save)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.FieldRole, spacerItem)
        add_to_vocab.setCentralWidget(self.centralwidget)
        self.retranslateUi(add_to_vocab)
        QtCore.QMetaObject.connectSlotsByName(add_to_vocab)

        self.word_list = find_translation(word)
        for word in self.word_list:
            self.comboBox.addItem(word[3])

    def retranslateUi(self, add_to_vocab):
        _translate = QtCore.QCoreApplication.translate
        add_to_vocab.setWindowTitle(_translate("add_to_vocab", "MainWindow"))
        self.label.setText(_translate("add_to_vocab", f"{self.word}"))
        self.push_button_my_variant.setText(_translate("add_to_vocab", "Yourself variant"))
        self.push_button_save.setText(_translate("add_to_vocab", "Save"))

    def clicker(self, user):
        translated_word = self.comboBox.currentText()
        for word in self.word_list:
            if word[3] == translated_word:
                translated_word_id = word[0]
                add_word_to_user(user, translated_word_id)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    add_to_vocab = QtWidgets.QMainWindow()
    ui = Ui_add_to_vocab()
    ui.setupUi(add_to_vocab)
    add_to_vocab.show()
    sys.exit(app.exec_())
