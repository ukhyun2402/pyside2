# PySide2.QtWidgets 에서 사용하는 widget들 임포트
# PySide2 위젯을 사용하기 위해서는 반드시 PySide2.QtWidget을 불러와야함
from PySide2.QtWidgets import QApplication,QLabel,QLayout

# QApplication 인스턴스 생성
app = QApplication()
# QLabel 인스턴스 생성, Construct 이용하여 Label에 내용삽입
# QLabel은 이미지와 html을 이용이 가능함
label = QLabel("<font color=red> Hello World </font>")

# Label 표시
label.show()
# 루프 실행
app.exec_()
