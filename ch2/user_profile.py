import sys
import os
from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtGui import QPixmap, QFont

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("2.1 User Profile GUI")
        self.setGeometry(50, 50, 250, 400)
        self.setFixedSize(250, 400)

        self.create_image_labels()

        user_label = QLabel(self)
        user_label.setText("Johb Doe")
        user_label.move(80, 140)
        user_label.setFont(QFont('Arial', 18))

        Bio_label = QLabel(self)
        Bio_label.setText("Biography")
        Bio_label.move(15, 170)
        Bio_label.setFont(QFont('Arial', 14))

        about_label = QLabel(self)
        about_label.setText("I am a software engineer with 10 years experience creating awesome code.")
        about_label.setWordWrap(True)
        about_label.move(15, 190)
        
        skills_label = QLabel(self)
        skills_label.setText("Skills")
        skills_label.setFont(QFont("Arial", 14))
        skills_label.move(15, 240)

        languages_label = QLabel(self)
        languages_label.setText("Python | PHP | SQL | JavaScript")
        languages_label.move(15, 260)

        experience_label = QLabel(self)
        experience_label.setText("Experience")
        experience_label.setFont(QFont("Arial", 14))
        experience_label.move(15, 290)
        developer_label = QLabel(self)
        developer_label.setText("Python Developer")
        developer_label.move(15, 310)
        dev_dates_label = QLabel(self)
        dev_dates_label.setText("Mar 2011 - Present")
        dev_dates_label.setFont(QFont("Arial", 10))
        dev_dates_label.move(15, 330)
        driver_label = QLabel(self)
        driver_label.setText("Pizza Delivery Driver")
        driver_label.move(15, 350)
        driver_dates_label = QLabel(self)
        driver_dates_label.setText("Aug 2015 - Dec 2017")
        driver_dates_label.setFont(QFont("Arial", 10))
        driver_dates_label.move(15, 370)

    def create_image_labels(self):
        images = ["images/skyblue.png", "images/profile_image.png"]
        for image in images:
            full_path = os.path.join(os.path.dirname(__file__), image)

            try:
                with open(full_path):
                    image_label = QLabel(self)
                    pixmap = QPixmap(full_path)
                    image_label.setPixmap(pixmap)
                    if image == "images/profile_image.png":
                        image_label.move(70, 15)
            except FileNotFoundError as error:
                print(f"Image not found.\nerror {error}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()

    sys.exit(app.exec())