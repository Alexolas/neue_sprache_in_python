import sys
from mainwindow import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = MainWindow()

    mainwindow.show()
    app.exec()
