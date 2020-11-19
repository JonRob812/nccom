from PyQt5 import QtWidgets as qw, QtCore as qc, QtGui as qg
from nccom.main_window import MainWindow
import sys

class NcComGUI(qw.QApplication):
    def __init__(self, args):
        super().__init__(args)
        self.setApplicationName('nccom')

        self.main_window = None

    def launch(self):
        self.main_window = MainWindow()
        self.main_window.show()
        return self.exec_()




    def show_main_window(self):
        pass