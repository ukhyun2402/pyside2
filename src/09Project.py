import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import QApplication,QDialog,QPushButton

class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        self.ui()

    # Group Of Drage Event
    def mousePressEvent(self,event):
        self.offset = event.pos()
    def mouseMoveEvent(self, e):
        x = e.globalX()
        y = e.globalY()
        x_w = self.offset.x()
        y_w = self.offset.y()
        self.move(x - x_w, y - y_w)

    def ui(self):
        # TitleBar
        self.setWindowFlags(Qt.FramelessWindowHint)

        # Window Size
        self.setGeometry(600,300,400,500)

        # Window Background Color
        self.BackGroundColor = QPalette()
        self.BackGroundColor.setColor(QPalette.Background, QColor(240,240,240))
        self.setPalette(self.BackGroundColor)

        # Close img
        self.closeBtn = QPushButton(self)
        self.closeBtn.setGeometry(368,0,32,32)
        self.closeBtn.setFlat(True)
        self.closeBtn.setStyleSheet('QPushButton{background-color: rgba(0,0,0,0.0)}')
        self.closeBtn.setIcon(QIcon('pyside2/img/close.png'))
        self.closeBtn.setIconSize(QSize(13,13))
        self.closeBtn.clicked.connect(QCoreApplication.instance().quit)

def main():
    app = QApplication()
    win = Main()
    win.show()
    app.exec_()

if __name__ == "__main__":
    main()