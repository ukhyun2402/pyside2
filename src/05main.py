from PySide2.QtWidgets import QApplication
from PySide2.QtQuick import QQuickView

app = QApplication()
view = QQuickView(source="./src/05view.qml")

view.show()
app.exec_()