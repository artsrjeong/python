import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import tensorflow as tf


form_class = uic.loadUiType("main.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushButtonClicked2)
    def pushButtonClicked(self):
        fname=QFileDialog.getOpenFileName(self)
        self.label.setText(fname[0])
    def pushButtonClicked2(self):
        text,ok=QInputDialog.getInt(self,'매수 수량','매수 수량을 입력하세요.')
        if ok:
            self.label.setText(str(text))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()