from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

class Highlighter(QSyntaxHighlighter):
    """def __init__(self):
        super().__init__()"""

    def highlightBlock(self, text):
        text_format = QTextCharFormat()
        text_format.setFontWeight(QFont.Bold)
        text_format.setForeground(Qt.cyan)
        pattern = "help"
        print(text)
        if text.startswith("help") and len(text.rstrip()) == 4:
            self.setFormat(0, len(text.rstrip()), text_format)
