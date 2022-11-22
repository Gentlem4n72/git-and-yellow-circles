import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.drawf)
        self.qp = QPainter()
        self.flag = False

    def drawf(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp.begin(self)
            self.draw_figure()
            self.qp.end()

    def draw_figure(self):
        self.qp.setBrush(QColor(255, 220, 70))
        size = randint(25, 200)
        x, y = randint(100, 500), randint(200, 500)
        self.qp.drawEllipse(x - size, y - size, size, size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
