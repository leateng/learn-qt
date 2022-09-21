import sys
import os
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.Qsci import *


class CustomMainWindow(QMainWindow):
    def __init__(self):
        super(CustomMainWindow, self).__init__()

        font_path = os.path.join(os.path.dirname(__file__), "./fonts/FiraCode-Regular.ttf")
        fira_code_font_id = QFontDatabase.addApplicationFont(font_path)
        print(f"fira_code_font_id = {fira_code_font_id}")
        fira_code_families = QFontDatabase.applicationFontFamilies(fira_code_font_id)

        # Window setup
        # --------------

        # 1. Define the geometry of the main window
        self.setGeometry(300, 300, 800, 400)
        self.setWindowTitle("QScintilla Test")

        # 2. Create frame and layout
        self.__frm = QFrame(self)
        # self.__frm.setStyleSheet("QWidget { background-color: #ffeaeaea }")
        self.__lyt = QVBoxLayout()
        self.__frm.setLayout(self.__lyt)
        self.setCentralWidget(self.__frm)
        self.__myFont = QFont(fira_code_families[0])
        self.__myFont.setPointSize(12)
        self.__myFont.setHintingPreference(QFont.HintingPreference.PreferFullHinting)

        # 3. Place a button
        self.__btn = QPushButton("Qsci")
        self.__btn.setFixedWidth(50)
        self.__btn.setFixedHeight(50)
        self.__btn.clicked.connect(self.__btn_action)
        self.__btn.setFont(self.__myFont)
        self.__lyt.addWidget(self.__btn)

        # QScintilla editor setup
        # ------------------------

        # ! Make instance of QsciScintilla class!
        self.__editor = QsciScintilla()
        self.__editor.setText("select * from alert_results where a = 1 order by name limit 10\n")
        self.__editor.setFont(self.__myFont)  # Set encoding to UTF-8
        self.__editor.setUtf8(True)  # Set encoding to UTF-8

        self.__lexer = QsciLexerSQL(self.__editor)
        self.__lexer.setFont(self.__myFont)
        self.__editor.setLexer(self.__lexer)        

        # 1. Text wrapping
        # -----------------
        self.__editor.setWrapMode(QsciScintilla.WrapMode.WrapWord)
        self.__editor.setWrapVisualFlags(QsciScintilla.WrapVisualFlag.WrapFlagByText)
        self.__editor.setWrapIndentMode(QsciScintilla.WrapIndentMode.WrapIndentIndented)

        # 2. End-of-line mode
        # --------------------
        self.__editor.setEolMode(QsciScintilla.EolMode.EolWindows)
        self.__editor.setEolVisibility(False)

    # 3. Indentation
        # ---------------
        self.__editor.setIndentationsUseTabs(False)
        self.__editor.setTabWidth(4)
        self.__editor.setIndentationGuides(True)
        self.__editor.setTabIndents(True)
        self.__editor.setAutoIndent(True)

        # 4. Caret
        # ---------
        self.__editor.setCaretForegroundColor(QColor("#ff0000ff"))
        self.__editor.setCaretLineVisible(True)
        self.__editor.setCaretLineBackgroundColor(QColor("#1f0000ff"))
        self.__editor.setCaretWidth(2)

        # 5. Margins
        # -----------
        # Margin 0 = Line nr margin
        self.__editor.setMarginType(0, QsciScintilla.MarginType.NumberMargin)
        self.__editor.setMarginWidth(0, "0000")
        self.__editor.setMarginsForegroundColor(QColor("#ff888888"))

        self.__editor.setedit

        # ! Add editor to layout !
        self.__lyt.addWidget(self.__editor)

        self.show()

    def __btn_action(self):
        print("Hello World!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # QApplication.setStyle(QStyleFactory.create('Fusion'))
    myGUI = CustomMainWindow()

    sys.exit(app.exec())