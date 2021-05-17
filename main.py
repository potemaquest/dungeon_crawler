import sys
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction, QMessageBox, QCheckBox
from PyQt5.QtGui import QIcon


class DungeonCrawler(QMainWindow):

    def __init__(self):
        super(DungeonCrawler, self).__init__()
        self.setGeometry(0, 0, 1000, 750)
        self.setWindowTitle("dungeon_crawler")
        self.setWindowIcon(QIcon("image0.jpg"))

        extract_action = QAction("Exit", self)
        extract_action.setShortcut("Ctrl+Q")
        extract_action.setStatusTip("Close Application")
        extract_action.triggered.connect(self.close_application)

        self.statusBar()

        main_menu = self.menuBar()
        file_menu = main_menu.addMenu("&File")
        file_menu.addAction(extract_action)

        self.home()

    def home(self):
        btn = QPushButton("Close", self)
        btn.clicked.connect(self.close_application)

        btn.resize(btn.sizeHint())
        btn.move(0, 100)

        extract_action = QAction(QIcon("grugg1001.png"), "Grugg it up!", self)
        extract_action.triggered.connect(self.close_application)

        self.toolBar = self.addToolBar("Grugg")
        self.toolBar.addAction(extract_action)

        check_box = QCheckBox("Enlarge Window", self)
        check_box.move(100, 25)
        check_box.stateChanged.connect(self.enlarge_window)

        self.show()

    def enlarge_window(self, state):
        if state == Qt.Checked:
            self.setGeometry(50, 50, 1920, 1080)
        else:
            self.setGeometry(50, 50, 1000, 750)

    def close_application(self):
        choice = QMessageBox.question(self, "Exit",
                                      "Close the Application?",
                                      QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            print("closing application")
            sys.exit()
        else:
            pass


def run():
    app = QApplication(sys.argv)
    GUI = DungeonCrawler()
    sys.exit(app.exec_())


run()
