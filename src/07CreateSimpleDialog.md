# Creating a Simple PySide2 Dialog Application
이번에는 간단한 위젯을 이용해서 간단한 Dialog를 만든방법을 알아보겠습니다. QLineEdit을 이용해 유저가 이름을 제공해주고 이를 Dialog가 QPushButton을 클릭하면 환영해주는 응용프로그램입니다.

간단한 토막의 코드를 이용해 Dialog를 만들고 표시해봅시다.

- 07main.py
```python
from PySide2.QtWidgets import QApplication,QDialog,QLineEdit,QPushButton

class form(QDialog):
    def __init__(self, parent = None):
        super(form,self).__init__(parent)
        self.setWindowTitle("My Form")


if __name__ =="__main__":
    app = QApplication()
    form = form()
    form.show()
    app.exec_()
```
첫번째 라인의 import 구문과 QApplication, 메인루프를 실행하는 구문은 새롭지 않겠지만 클래스 선언문은 새로울 수 있습니다. 

PySide2는 모든 위젯들의 서브클래스를 생성할 수 있습니다. 위의 상황에서는 QDialog의 서브클래스를 생성하고 나의 선호에 맞게끔 커스텀한 것입니다. 이렇게 커스텀한 QDialog를 우리는 `form` 이라고 칭했습니다. 우리는 또한 `__init__`메소드를 실행하고 부모 위젯의 메소드를 불렀습니다. 또한 새로운 `setWindowTitle()`메소드를 통해 Dialog윈도우의 이름을 정했습니다. 


## Creating the Widgets
우리는 2개의 위젯을 만들어 볼까 합니다. 하나는 QLineEidt이며 이는 사용자의 이름을 넣을 수 있는 공간입니다. 또 다른 하나는 QPushButton 이며 이는 QLineEdit에 있는 내용을 출력하는 버튼(트리거)입니다. 다음의 코드를 `init()`메소드에 넣어봅시다.

```python
self.edit = QLineEdit("Write Your Name")
self.btn = QPushButton("Show Greetings")
```
> 위의 위젯들은 생성자(Constructor)을 이용해 라벨을 붙이는 코드입니다.

## Create a layout to organize the Widgets
Qt는 위젯들의 레이아웃을 잡아주는 기능이 들어있습니다. 이번에는 `QVBoxLayout`을 이용해 위젯들을 수직선으로 배치해보겠습니다. 다음의 코드를 `init()` 메소드에 추가해주세요. (이 때 위에서 생성한 위젯들 밑에 코드가 위치해야 합니다.)
> import에 QVBoxLayout을 추가해주세요!

```python
ly = QVBoxLayout()
ly.addWidget(self.edit)
ly.addWidget(self.btn)

self.setLayout(ly)
```
이렇게 하면 우리는 레이아웃의 틀을 추가한 것입니다. 이 틀에 위에서 생성한 위젯들을 추가하는 것을 코드로 보여주고 있습니다.

### Create the function to greet and connect the Button
이제는 커스텀된 폼을 작성하고 버튼에 함수를 연결시키는 작업을 할까합니다. 우리의 함수는 `form`의 일부이며 `init()`메소드 이후에 작성되어야 합니다.

> `init()` 메소드 안이 아닙니다. form 클래스의 멤버 메소드로 작성해주세요

```python
def greeting(self):
    print("Hello {}".format(self.edit.text())
```
위 함수는 단순히 QLineEdit의 Text를 Pythone Console에 출력하는 함수입니다. 

이제는 우리가 필요한 모든 구성들을 다 마쳤습니다. 이제는 QPushButton과 함수를 연결하고 클릭하면 `form.greeting()` 메소드를 불러오면 됩니다. 다음의 코드를 `init()` 메소드에 추가해주세요

```python
self.btn.clicked.connect(self.greeting)
```
실행한 후에 이름을 QLineEdit에 이름을 입력하고 콘솔을 보면 출력이 보이게 됩니다 !

- 전체코드
```python
from PySide2.QtWidgets import QApplication,QDialog,QLineEdit,QPushButton,QVBoxLayout

class form(QDialog):
    # QDialog의 생성자
    def __init__(self, parent = None):
        # 부모크클래스의 메소드 상속
        super(form,self).__init__(parent)
        # QDialog의 WindowTitle 지정
        self.setWindowTitle("My Form")

        # QLineEdit 인스턴스 생성 with 라벨
        self.edit = QLineEdit("Write Your Name")
        # QPushButton 인스턴스 생성 with 라벨
        self.btn = QPushButton("Show Greetings")

        # QVBoxLayout 인스턴스 생성
        ly = QVBoxLayout()
        # Layout 인스턴스 멤버 추가
        ly.addWidget(self.edit)
        ly.addWidget(self.btn)

        # QDialog에 레이아웃 셋
        self.setLayout(ly)
        
        # QPushButton 함수 연결
        self.btn.clicked.connect(self.greeting)

    # 유저 함수 선언
    def greeting(self):
        print("Hello {}".format(self.edit.text()))

if __name__ =="__main__":
    app = QApplication()
    form = form()
    form.show()
    app.exec_()
```