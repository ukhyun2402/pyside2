import random
from PySide2 import QtCore,QtWidgets,QtGui

class main(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hello World","Python","?하욱현"]

        # PushButton 인스턴스 생성(constructor 이용, Click Me내용을 버튼에 삽입)
        self.button = QtWidgets.QPushButton("Click Me")
        # Label(text) 인스턴스 생성(constructor 이용, Hello World 내용을 라벨에 삽입)
        self.text = QtWidgets.QLabel("Hello World")
        #text 라벨의 정렬에 대한 설정(Center)
        self.text.setAlignment(QtCore.Qt.AlignCenter)

        # Layout 인스턴스 생성
        self.layout = QtWidgets.QVBoxLayout()
        # Laout에 위젯 삽입
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        # Layout 메인에 설정
        self.setLayout(self.layout)

        # 버튼에 대해서 함수 연결
        self.button.clicked.connect(self.magic)

    # magic함수 생성
    def magic(self):
        self.text.setText(random.choice(self.hello))

if __name__ == "__main__":
    
    app = QtWidgets.QApplication()
    widget = main()
    widget.resize(800,600)    
    widget.show()

    app.exec_()