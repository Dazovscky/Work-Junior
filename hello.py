import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 Window'
        self.left = 200
        self.top = 100
        self.width = 400
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.label = QLabel("Hello World", self)
        self.label.move(150, 100)

        button = QPushButton("Click", self)
        button.move(150, 150)
        button.clicked.connect(self.onClick)

        btn2 = QPushButton("Button B", self)
        btn2.move(0, 100)
        btn2.clicked.connect(self.onClickB)

        self.show()

    @pyqtSlot()
    def onClick(self):
        print('Button click!')

    @pyqtSlot()
    def onClickB(self):
        print('Button2 click!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())