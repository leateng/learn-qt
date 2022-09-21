from email.mime import image
import sys
import os
from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtGui import QPixmap

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("QLabel example")
        self.setGeometry(100, 100, 250, 250)

        hello_label = QLabel(self)
        hello_label.setText("Hello")
        hello_label.move(105, 15)

        image_path = os.path.join(os.path.dirname(__file__), "images/world.png")
        with open(image_path):
            pixmap = QPixmap(image_path)
            image_label = QLabel(self)
            image_label.setPixmap(pixmap)
            image_label.move(25, 40)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()

    sys.exit(app.exec())