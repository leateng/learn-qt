from PySide6.QtWidgets import QApplication, QWidget

class EmptyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("Hello Qt")
        self.setGeometry(300, 300, 800, 600)


if __name__ == '__main__':
    app = QApplication([])
    win = EmptyWindow()
    win.show()

    app.exec()