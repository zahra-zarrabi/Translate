# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget,QMessageBox
from PySide6.QtUiTools import QUiLoader

class translate(QWidget):
    def __init__(self):
        super(translate, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load('dialog.ui')
        self.ui.show()

        try:
            self.f = open('text.txt')
        except:
            msg_box = QMessageBox()
            msg_box.setText('no')
            msg_box.exec_()

        self.big_text = self.f.read()
        self.parts = self.big_text.split('\n')

        self.words = []
        i = 0
        while i < len(self.parts):
            my_Dictionary = {'english': self.parts[i], 'persian': self.parts[i + 1]}
            self.words.append(my_Dictionary)
            i += 2

        self.ui.btn_tar.clicked.connect(self.my_checked)

        self.ui.lineEdit_2.setStyleSheet('color: red; background-color:#ecbbcc')
    def my_checked(self):
        if self.ui.rb_english.isChecked():
            self.ne=""
            self.matn=self.ui.lineEdit_1.text()
            user_word=self.matn.split()
            for n in range(len(user_word)):
                for m in range(len(self.words)):
                    if self.words[m]['english']==user_word[n]:
                        self.ne = self.ne + self.words[m]['persian']+" "
                        self.ui.lineEdit_2.setText(self.ne)
                        break
                else:
                    self.ne = self.ne + user_word[n] + " "
                    self.ui.lineEdit_2.setText(self.ne)

        if self.ui.rb_persian.isChecked():
            self.ne = ""
            string = self.ui.lineEdit_1.text()
            user_word = string.split()
            for n in range(len(user_word)):
                for m in range(len(self.words)):
                    if self.words[m]['persian'] == user_word[n]:
                        self.ne = self.ne + self.words[m]['english'] + " "
                        self.ui.lineEdit_2.setText(self.ne)
                        break
                else:
                    self.ne = self.ne + user_word[n] + " "
                    self.ui.lineEdit_2.setText(self.ne)

if __name__ == "__main__":
    app = QApplication([])
    window = translate()
    sys.exit(app.exec_())
