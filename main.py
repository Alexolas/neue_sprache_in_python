import sys
from mainwindow import *

"""@Slot()
def keine_ahnung():
    print("Irgendwas")"""

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = MainWindow()

    mainwindow.show()
    app.exec()
