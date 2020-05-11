from PySide2.QtWidgets import QApplication,QDialog,QLineEdit,QPushButton,QVBoxLayout

class form(QDialog):
    def __init__(self, parent = None):
        super(form,self).__init__(parent)
        self.setWindowTitle("My Form")

        self.edit = QLineEdit("Write Your Name")
        self.btn = QPushButton("Show Greetings")

        ly = QVBoxLayout()
        ly.addWidget(self.edit)
        ly.addWidget(self.btn)

        self.setLayout(ly)
        
        self.btn.clicked.connect(self.greeting)

    def greeting(self):
        print("Hello {}".format(self.edit.text()))

if __name__ =="__main__":
    app = QApplication()
    form = form()
    form.show()
    app.exec_()