# Your First Application Using PySide2 and QtQuick/QML
QML은 기존의 언들보다 빠르게 응용프로그램을 선언할 수 있는 프로그래밍 언어입니다. 이는 UI를 디자인하는데에 최적입니다. QML에서는 트리 구조로 각각의 설정들을 선언할 수 있습니다. 이번 튜토리얼에서는 "Hello World"라는 응용프로그램을 PySide2와 QML을 이용하여 만들어 보겠습니다.

QML을 이용하기 위해서는 최소한 PySide2와 QML 파일 2가지는 가지고 있어야합니다. QML파일은 유저 인터페이스를 설명하고, python파일(PySide2)파일은 QML파일을 로드하여 UI를 구성합니다. 다음 2가지의 파일을 같은 디렉토리에 저장해주세요!

- view.qml
```QML
import QtQuick 2.0

Rectangle {
    width: 200
    height: 200
    color: "green"

    Text{
        text: "Hello World"
        anchors.centerIn: parent
    }
}
```
이때 우리는 제일먼저 QtQuick(QML) 모듈을 불러와야합니다.

그 외의 나머지 QML코드는 XML 또는 HTML을 이용한 유저에게는 매우 간단한 코드입니다. 기본적으로 우리는 200x200의 초록색 사각형을 만들고 그 곳에 "Hello World"라는 Text를 생성했습니다. <code>anchors.centerIn: parent</code>이라는 코드는 부모의 위치에 대비해서 중간에 위치시키는 코드입니다.

이제 모든 UI에 대해서 설정을 다 했으니, PySide2 코드를 작성해 봅시다.

- main.py
```python
from PySide2.QtWidgets import QApplication
from PySide2.QtQuick import QQuickView
from PySide2.QtCore import QUrl

app = QApplication([])
view = QQuickView()
url = QUrl("./src/05view.qml")

view.setSource(url)
view.show()
app.exec_()

# 또는 QUrl을 쓰지않고 다음처럼 사용할 수 있습니다.

from PySide2.QtWidgets import QApplication
from PySide2.QtQuick import QQuickView

app = QApplication()
view = QQuickView(source="./src/05view.qml")

view.show()
app.exec_()
```

만약 PySide2에 대해서 익숙하거나 이 Tutorial을 다 읽어본 경우는 이미 위와 같은 코드를 많이 본 경험이 있을겁니다. 그러나 중간에 조금은 새로운 코드인 <code>import QtQuick</code>와 `QQuickView`객체에 URL을 통해 QML파일을 불러오는 것일 겁니다. 그리고 어떠한 QtWidget도 QQuickView.show()을 통해 불러올 수 있습니다.

> 만약 Desktop을 위한 응용프로그램을 만든다면 반드시 view전에 view.setResizeMode(QQuickView.SizeRootObjectToView)을 추가하여야 합니다. 