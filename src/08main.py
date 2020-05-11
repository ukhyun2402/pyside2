from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader

if __name__ == '__main__':
    app = QApplication()
    ui_file = QFile('08UsingUIFile.ui')
    loader = QUiLoader()
    window = loader.load(ui_file)
    window.show()
    app.exec_()