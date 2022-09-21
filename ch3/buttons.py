import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PySide6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("QPushButton example")
        self.setGeometry(100, 100, 250, 150)

        self.time_pressed = 0

        self.name_label = QLabel("Don't push the button", self)
        # self.name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.name_label.move(60, 30)

        self.button = QPushButton("Push Me", self)
        self.button.move(80, 70)
        self.button.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        self.time_pressed += 1

        if self.time_pressed == 1:
            self.name_label.setText("Why'd you pressed me?")
        
        if self.time_pressed == 2:
            self.name_label.setText("I'm warnning you!")
            self.button.setText("Feelin' Luck?")

        if self.time_pressed == 3:
            print("the window has been closed")
            self.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()

    sys.exit(app.exec())