from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

class Highlighter(QSyntaxHighlighter):
    def __init__(self, parent: QObject):
        super().__init__(parent)
        self.var = {}
        self.listanimals = []

    def highlightBlock(self, text):
        text_format1 = QTextCharFormat()
        text_format1.setFontWeight(QFont.Bold)
        text_format1.setForeground(Qt.blue)

        text_format2 = QTextCharFormat()
        text_format2.setFontWeight(QFont.Bold)
        text_format2.setForeground(Qt.darkGreen)

        text_format3 = QTextCharFormat()
        text_format3.setFontWeight(QFont.Bold)
        text_format3.setForeground(Qt.red)

        if text.startswith("help") and len(text.rstrip()) == 4:
            self.setFormat(0, len(text.rstrip()), text_format1)
        if text.startswith("say ") or text.startswith("s "):
            if text.startswith("s "):
                self.setFormat(0, 1, text_format1)
                self.setFormat(2, len(text), text_format2)
            else:
                self.setFormat(0, 3, text_format1)
                self.setFormat(4, len(text), text_format2)
        if text.startswith("randomAnimal") or text.startswith("randomanimal") or text.startswith("ra"):
            self.process_randomAnimal(text, text_format1, text_format2, text_format3)
        if text.startswith("listAnimals") or text.startswith("listanimals") or text.startswith("la") and len(text.rstrip()) < 12:
            if text.startswith("la") and len(text.rstrip()) == 2:
                self.setFormat(0, 2, text_format1)
            elif len(text.rstrip()) == 11:
                self.setFormat(0, 12, text_format1)
        if text.startswith("make") or text.startswith("mk"):
            if text.startswith("mk"):
                self.setFormat(0, 2, text_format1)
                if "=" not in text:
                    self.setFormat(3, len(text), text_format2)
                else:
                    self.setFormat(3, text.index("=") - 1, text_format2)
                    self.setFormat(text.index("="), 1, text_format3)
                    self.setFormat(text.index("=") + 1, len(text), text_format2)
            else:
                self.setFormat(0, 4, text_format1)
                if "=" not in text:
                    self.setFormat(5, len(text), text_format2)
                else:
                    v_u_w = ''.join(text.split("make "))
                    self.setFormat(5, text.index("=") - 1, text_format2)
                    self.setFormat(text.index("="), 1, text_format3)
                    self.setFormat(text.index("=") + 1, len(text), text_format2)
                    v = v_u_w.split("=")[0].strip()
                    w = v_u_w.split("=")[1].strip()
                    self.var[v] = w
        if text.startswith("$"):
            self.setFormat(0, 1, text_format3)
            v_name = text[1:len(text.strip())]
            if v_name in self.var:
                self.setFormat(1, len(text), text_format2)


    def process_randomAnimal(self, text, text_format1, text_format2, text_format3):
        if text.startswith("randomAnimal") or text.startswith("randomanimal"):
            self.setFormat(0, 12, text_format1)
            animals = text[13:len(text)].split(",")
            self.animal_func(animals, text, text_format2, text_format3)
        elif not text.startswith("ra ") and len(text.rstrip()) == 2:
            self.setFormat(0, 2, text_format1)
        elif text.startswith("ra "):
            self.setFormat(0, 2, text_format1)
            animals = text[2:len(text)].split(",")
            self.animal_func(animals, text, text_format2, text_format3)
            print(animals)

    def animal_func(self, animals, text, text_format2, text_format3):
        for x in animals:
            xs = x.strip()
            pos_animal = text.index(xs)
            pos_komma = text.find(",", pos_animal)
            if pos_komma != -1:
                self.setFormat(pos_komma, 1, text_format3)
            if xs in self.listanimals:
                self.setFormat(text.index(xs), len(xs), text_format2)
