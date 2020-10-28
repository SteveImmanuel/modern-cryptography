from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QLabel, QPushButton, QMainWindow, QApplication, QDialog, QDialogButtonBox, QSizePolicy


class DialogWindow(QDialog):
    def __init__(self, title: str, desc: str):
        super(DialogWindow, self).__init__()
        dim = QApplication.desktop().screenGeometry()

        self.title = title
        self.desc = desc

        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle(self.title)

        self.btn_ok = QDialogButtonBox(QDialogButtonBox.Ok)
        self.btn_ok.accepted.connect(self.accept)

        self.lbl_dec = QLabel()
        self.lbl_dec.setText(self.desc)
        self.lbl_dec.setWordWrap(True)
        self.lbl_dec.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.layout = QVBoxLayout()
        self.layout.setSpacing(10)

        self.layout.addWidget(self.lbl_dec)
        self.layout.addWidget(self.btn_ok)
        self.setLayout(self.layout)
