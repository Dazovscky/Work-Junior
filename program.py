import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class Program(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('1.png'), '&Выход', self)
        editAciton = QAction(QIcon('1.png'), '&Редактировать', self)

        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Выход из приложения')
        exitAction.triggered.connect(qApp.quit)

        editAciton.setShortcut('Ctrl+N')
        editAciton.setStatusTip('Добавить дисциплину')
        editAciton.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Файл')
        editMenu = menubar.addMenu('Редактировать')
        fileMenu.addAction(exitAction)
        editMenu.addAction(editAciton)

        self.setGeometry(300, 300, 800, 800)
        self.setWindowTitle('Menubar')
        self.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Program()
    sys.exit(app.exec_())