from parser_1 import *
from highlighter import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtSvg import *
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.listanimals = ['Alpaka', 'Elefant', 'Esel', 'Hase', 'Hund', 'Katze', 'Krokodil', 'Kuh', 'Löwe',
        'Maus', 'Panda', 'Salamander', 'Schaf', 'Schwein', 'Tiger']

        self.setWindowTitle("Neue Sprache")
        self.resize(1024, 512)
        self.createWidget()
        self.createActions()
        self.createMenuBar()

    @Slot()
    def run(self):
        parser = Parser()
        parser.list_animals = self.listanimals
        success = parser.parse(self.textedit1.toPlainText())
        if not success:
            QMessageBox.critical(self, "Fehler", "Du hast keinen gültigen Befehl angegeben.")
        if parser._messages != []:
            self.textedit2.setPlainText(''.join(parser._messages))
        else:
            self.textedit2.setPlainText("Error")



    def createWidget(self):
        window = QWidget()
        layout1 = QVBoxLayout(window)
        layout2 = QGridLayout()
        label1 = QLabel("Programm:")
        label2 = QLabel("Ergebnis:")

        layout2.addWidget(label1, 0, 0)
        layout2.addWidget(label2, 0, 1)

        self.textedit1 = QTextEdit()
        layout1.addLayout(layout2)
        self.textedit1.textChanged.connect(self.clear)
        layout2.addWidget(self.textedit1, 1, 0)
        self.highlighter = Highlighter(self.textedit1.document())
        self.highlighter.listanimals = self.listanimals

        self.textedit2 = QTextEdit()
        self.textedit2.setReadOnly(True)
        layout2.addWidget(self.textedit2, 1, 1)

        button1 = QPushButton("Run")
        button1.clicked.connect(self.run)
        layout1.addWidget(button1)
        self.setCentralWidget(window)

    def createMenuBar(self):
        self._file_menu = self.menuBar().addMenu("&File")
        self._file_menu.addAction(self._new_act)
        self._file_menu.addAction(self._open_act)
        self._file_menu.addAction(self._save_act)
        self._file_menu.addSeparator()
        self._file_menu.addAction(self._exit_act)

        self._help_menu = self.menuBar().addMenu("&Help")
        self._help_menu.addAction(self._about_act)
        self._help_menu.addAction(self._about_qt_act)

    def createActions(self):
        icon_path_exit = os.path.join(os.path.dirname(__file__), 'Icons\exit.svg')
        self._exit_act = QAction(QIcon(icon_path_exit), "E&xit", self, shortcut="Ctrl+Q",
                statusTip="Exit the application", triggered=self.close)

        icon_path_qt = os.path.join(os.path.dirname(__file__), 'Icons\qtlogo.svg')
        self._about_qt_act = QAction(icon=QIcon(icon_path_qt), text="About &Qt", parent=self,
                statusTip="Show the Qt library's About box",
                triggered=qApp.aboutQt)

        icon_path_about = os.path.join(os.path.dirname(__file__), 'Icons\question.svg')
        self._about_act = QAction(QIcon(icon_path_about), "&About", self,
                statusTip="Show the Qt library's About box",
                triggered=self.about)

        icon_path_new = os.path.join(os.path.dirname(__file__), 'Icons\\new.svg')
        self._new_act = QAction(QIcon(icon_path_new), "&New", self, shortcut=QKeySequence.New,
                statusTip="Create a new file", triggered=self.new)

        icon_path_open = os.path.join(os.path.dirname(__file__), 'Icons\open.svg')
        self._open_act = QAction(QIcon(icon_path_open), "&Open...", self,
                shortcut=QKeySequence.Open, statusTip="Open an existing file",
                triggered=self.open)

        icon_path_save = os.path.join(os.path.dirname(__file__), 'Icons\save.svg')
        self._save_act = QAction(QIcon(icon_path_save), "&Save", self,
                shortcut=QKeySequence.Save,
                statusTip="Save the document to disk", triggered=self.save)


    def about(self):
        QMessageBox.about(self, "About Application",
                "The <b>Application</b> example demonstrates how to write "
                "modernGui applications using Qt, with a menu bar, "
                "toolbars, and a status bar.")

    def new(self):
        self.textedit1.clear()
        self.textedit2.clear()
        self.textedit1.setFocus()

    def open(self):
        filename, filter = QFileDialog.getOpenFileName(self)
        with open(filename, 'r') as f:
            read_data = f.read()
            self.textedit1.setText(read_data)

    def save(self):
        filename, filter = QFileDialog.getSaveFileName(self)
        with open(filename, 'w') as w:
            w.write(self.textedit1.toPlainText())

    @Slot()
    def clear(self):
        if self.textedit1.toPlainText() == '':
            self.textedit2.clear()
