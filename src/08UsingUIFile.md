# Using UI Files
이번에는 QtCreator를 이용해 그래픽 인터페이스를 만들어보겠습니다. 인터페이스를 디자인하고 수정하기 위해서는 Qt Creator가 필요합니다.

만약 Qt Designer를 사용할줄 모른다면 다음의 [링크](http://doc.qt.io/qtcreator/creator-using-qt-designer.html)를 참고해주세요. 
> 저는 Anaconda를 설치한 후 실행가능한 파일 Anaconda Prompt를 사용하면 콘솔창이 나오게 됩니다. 이 콘솔창에 `designer`라고 치면 인터페이스를 구성하고 수정할 수 있는 UI file을 만들 수 있는 툴이 나오게 됩니다.

다음의 사진과 설명을 따라 파일 UI를 만듭니다.

![0801](..\img\0801.png)

Templat에서 Main Windonw를 선택하고 생성합니다.
> 일반적인 Dioalog의 경우 MenuBar가 존재하지 않습니다. 따라서 MenuBar을 사용하고 싶은 경우에는 Main Window를 사용해야 합니다.

![0802](..\img\0802.png)

생성을 누르면 창이 하나 중간에 띄어져 있고 왼쪽에는 QPushButton 등 다양한 위젯들이 오른쪽에는 객체 탐색기와 함께 속성 편집기가 있습니다. 객체탐색기의 MainWindow 또는 Untiltle을 선택하고 속성편집기의 geometry에서 너비와 높이를 다음과 같이 설정합니다.

![0803](..\img\0803.png)

설정하였으면 windowTitle의 이름을 MainWindow로 지정합니다.

![0804](..\img\0804.png)

왼쪽의 위젯상자에서 Push Button을 메인윈도우로 드래그앤 드랍합니다.

![0805](..\img\0805.png)

이후 메인윈도우에서 오른쪽 클릭 후 도구 모음을 추가하면 메뉴바 밑에 얇게 생긴 바를 볼 수 있습니다.

![0806](..\img\0806.png)

위의 메뉴에서 도구 모음 추가 밑에 있었던 상태 표시줄 설정도 해줍니다.

![0807](..\img\0807.png)

하게되면 메인윈도우 우측하단에 작세나마 화살표가 생기고 오른쪽의 객체 탐색기에서 위에서 추가한 모든 객체들이 있는 것을 볼 수 있습니다.

설정을 완료했으면 저장하고 원하는 이름으로 설정합시다! 경로설정을 단순하게 하기 위해서 파이썬 파일과 같은 경로에 설정하면 상대경로 절대경로를 생각하지 않고 할 수 있어 간편합니다.

이제 위에서만든 UI파일을 이용해 응용프로그램을 만들어 봅시다. 아래의 코드를 작성하며 이해해 봅시다.

- 08main.py
```python
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
```

파일을 실행하기 위해서는 반드시 command prompt에서
```bash
python 08main.py
```
를 실행해야합니다.