from PyQt5 import uic   # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
import random
import sys


class DrawBeautifulCircles(QMainWindow):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.get_circles.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            # Создаем объект QPainter для рисования
            qp = QPainter()
            # Начинаем процесс рисования
            qp.begin(self)
            qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            self.draw_circles(qp)
            # Завершаем рисование
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_circles(self, painter):
        for i in range(3):
            painter.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            r = random.randint(0, 300)
            painter.drawEllipse(random.randint(r, 450) - r, random.randint(r, 300) - r, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DrawBeautifulCircles()
    ex.show()
    sys.exit(app.exec_())