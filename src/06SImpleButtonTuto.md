# A Simple Button Tutorial

이번에는 `signals 와 slots`을 다루는 방법에 대해서 이야기 하고자 합니다.  `Signals 와 Slots`은 그래픽적 위젯이 다른 위젯들 또는 Python Code와 상호작용할 수 있는 Qt feature입니다. 우리는 버튼을 클릭하면 "Hello"라는 메시지를 python console에 표시하는 응용프로그램을 만들어 볼 것입니다.

먼저 필수적인 PySide2 클래스를 불러옵니다.

```python
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import Slot
```
이제 메시지를 python console에다 표시하는 함수를 만들어 봅시다.
```python
@Slot()
def sayHello():
    print("Button Clicked, Hello")
```
> `@Slot`은 함수를 slot으로 표시하는 하나의 장식입니다. 지금으로선 이것을 이해하는 것은 중요하지 않습니다. 하지만 비정상적 행동을 피할때에는 언제나 이를 사용하게 됩니다.

돌아와서 위에서 작성한 코드에 QApplication 인스턴스를 생성합니다.
```python
app = QApplication()
```

QPushButton 인스턴스를 생성하고, 버튼에 라벨을 QPushButton의 constructor(생성자)를 이용해 붙입니다.

```python
btn = QPushButton("Click Me")
```
위에서 만든 버튼을 보여주기 전에 먼저 이 버튼을 눌렀을 때 어떠한 동작을 수행할 것인지를 정해야합니다. 이미 메시지를 콘솔에 보여주는 함수를 선언했습니다. 버튼과 함수를 연결하는 방법은 2가지(old, new)가 존재합니다. 이번에는 새로운 방법을 사용해보겠습니다. 2가지 방법에 대해서 조금 더 알고 싶은 경우 [Signals and Slots in PySide2](https://wiki.qt.io/Qt_for_Python_Signals_and_Slots)를 참조하세요


QPushButton은 `clikced`라고 불리는 시그널을 이미 가지고 있습니다. 이러한 트리거는 버튼을 클릭할 때마다 실행됩니다. 다음의 코드를 통해 이미 선언한 함수 sayHello와 버튼을 연결해 봅시다.

```python
btn.clicked.connect(sayHello)
```
마지막으로 button을 보기에 설정하고 Qt 메인 루프를 실행합니다.

```python
btn.show()
app.exec_()
```

## 전체 코드
```python
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
```