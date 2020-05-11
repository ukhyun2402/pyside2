from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import Slot

@Slot()
def sayHello():
    print("Button Clicked, Hello")

app = QApplication()
btn = QPushButton("Click Me")
btn.clicked.connect(sayHello)
btn.show()

app.exec_()