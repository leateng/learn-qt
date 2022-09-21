import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QCheckBox
from PySide6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("QCheckbox example")
        self.setMaximumSize(250, 150)
        self.resize(250, 150)

        self.header_label = QLabel("Which shifts can you work? (Please check all that apply)", self)
        self.header_label.setWordWrap(True)
        self.header_label.move(20, 10)

        self.morning_cb = QCheckBox("Morning [8 AM - 2 PM]", self)
        self.morning_cb.move(40, 60)
        self.morning_cb.toggle()
        self.morning_cb.toggled.connect(self.printSelected)

        self.after_cb = QCheckBox("Afternoon [1 PM - 8 PM]", self)
        self.after_cb.move(40, 80)
        self.after_cb.toggled.connect(self.printSelected)

        self.night_cb = QCheckBox("Night [7 PM - 3 AM]", self)
        self.night_cb.move(40, 100)
        self.night_cb.toggled.connect(self.printSelected)

    def printSelected(self, checked):
        sender = self.sender()

        if checked:
            print(f"{sender.text()} Selected")
        else:
            print(f"{sender.text()} DeSelected")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()

    sys.exit(app.exec())