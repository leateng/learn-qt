import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("QLineEdit example")
        self.setMaximumSize(310, 130)
        # self.setMinimumSize(310, 250)

        self.propmt_label = QLabel("Please enter your name blow", self)
        self.propmt_label.move(70, 10)

        self.name_label = QLabel("Name:", self)
        self.name_label.move(20, 50)

        self.name_edit = QLineEdit(self)
        self.name_edit.move(70, 50)
        self.name_edit.resize(210, 20)

        self.clear_button = QPushButton("Clear", self)
        self.clear_button.move(130, 90)
        self.clear_button.clicked.connect(self.onClearClicked)

        self.ok_button = QPushButton("OK", self)
        self.ok_button.move(210, 90)
        self.ok_button.clicked.connect(self.onOkClicked)

    def onClearClicked(self):
        self.name_edit.clear()

    def onOkClicked(self):
        text = self.name_edit.text()
        print(f"Hello {text}")

        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()

    sys.exit(app.exec())