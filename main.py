import sys

from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
from math import atan, sqrt


def f(x, y):
    if x + y == 0:
        return 99999999
    return x ** 2 + y ** 2


class Example(QWidget):
    def __init__(self, resolution):
        super().__init__()
        self.resolution = resolution
        self.wid = 800
        self.hei = 800
        self.step = 10
        self.delta = 10
        self.initUI()

    def initUI(self):
        self.setGeometry((resolution[0] - self.wid) // 2, (resolution[1] - self.hei) // 2, self.wid, self.hei)
        self.setWindowTitle('Draw text')
        self.text_step = QLineEdit(self)
        self.text_step.setGeometry(0, 80, 100, 20)
        self.text_step.setText("1")
        btn_inc = QPushButton("inc step", self)
        btn_inc.setGeometry(0, 0, 100, 20)
        btn_inc.clicked.connect(self.incStep)
        btn_dec = QPushButton("dec step", self)
        btn_dec.setGeometry(0, 40, 100, 20)
        btn_dec.clicked.connect(self.decStep)
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawBackground(event, qp)
        self.drawCurve(event, qp)
        qp.end()

    def incStep(self, sender):
        value = int(self.text_step.text())
        self.step += value
        self.delta += value
        self.repaint()
        print(self.step)

    def decStep(self, sender):
        value = int(self.text_step.text())
        self.step -= value
        self.delta -= value
        self.repaint()
        print(self.step)

    def drawBackground(self, event, qp : QPainter):
        qp.setPen(QColor(255, 0, 0))
        qp.fillRect(self.rect(), Qt.black)

    def drawCurve(self, event, qp):
        qp.setPen(Qt.green)
        for y in range(0, 800, self.step):
            for x in range(0, 800, self.step):
                alt_x = x / 100 - 4
                alt_y = y / 100 - 4
                tga = atan(f(alt_x, alt_y))
                cosa = 1 / sqrt(1 + tga ** 2)
                sina = sqrt(1 - cosa ** 2)
                qp.drawLine(x, y, x + self.delta * cosa, y + self.delta * sina)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    geometry = app.desktop().screenGeometry()
    resolution = geometry.width(), geometry.height()
    ex = Example(resolution)
    sys.exit(app.exec_())