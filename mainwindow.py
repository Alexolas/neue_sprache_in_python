from parser_1 import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Neue Sprache")
        self.resize(1024, 512)
        self.createWidget()
        self.createActions()
        self.createMenuBar()

    @Slot()
    def run(self):
        parser = Parser()
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
        self._exit_act = QAction("E&xit", self, shortcut="Ctrl+Q",
                statusTip="Exit the application", triggered=self.close)

        self._about_qt_act = QAction(text="About &Qt", parent=self,
                statusTip="Show the Qt library's About box",
                triggered=qApp.aboutQt)

        self._about_act = QAction("&About", self,
                statusTip="Show the Qt library's About box",
                triggered=self.about)

        icon = QIcon.fromTheme("document-new", QIcon(':/images/new.png'))
        self._new_act = QAction("&New", self, shortcut=QKeySequence.New,
                statusTip="Create a new file", triggered=self.new)

        icon = QIcon.fromTheme("document-open", QIcon(':/images/open.png'))
        self._open_act = QAction("&Open...", self,
                shortcut=QKeySequence.Open, statusTip="Open an existing file",
                triggered=self.open)

        icon = QIcon.fromTheme("document-save", QIcon(':/images/save.png'))
        self._save_act = QAction("&Save", self,
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

# icons