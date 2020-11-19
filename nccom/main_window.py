from PyQt5 import QtWidgets as qw, QtCore as qc, QtGui as qg
from nccom.ui.mainwindow_ui import Ui_MainWindow


class MainWindow(qw.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
