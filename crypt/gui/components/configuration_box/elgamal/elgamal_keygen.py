from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSizePolicy, QSpacerItem

from crypt.gui.components.configuration_box.base_keygen import BaseKeygen
from crypt.gui.components.configuration_box.edit_with_button import EditWithButton
from crypt.gui.dialog_window import DialogWindow
from crypt.utils.number_util import *


class ElgamalKeygen(BaseKeygen):
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        self.p_value = EditWithButton('p value', 'Randomize')
        self.g_value = EditWithButton('g value', 'Randomize')
        self.x_value = EditWithButton('x value', 'Randomize')
        self.spacer = QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.p_value)
        self.layout.addWidget(self.g_value)
        self.layout.addWidget(self.x_value)
        self.layout.addSpacerItem(self.spacer)

        self.setLayout(self.layout)

        self.p_value.btn_random.clicked.connect(self.randomize_prime)
        self.g_value.btn_random.clicked.connect(lambda: self.randomize_number(is_g=True))
        self.x_value.btn_random.clicked.connect(lambda: self.randomize_number(is_g=False))

    def randomize_prime(self):
        random_prime = generate_prime_number(9)
        print(random_prime)
        self.p_value.line_edit.setText(str(random_prime))

    def randomize_number(self, is_g: bool):
        try:
            p = int(self.p_value.line_edit.text())

            if is_prime(p):
                random_number = generate_random_number(1, p - 1)
                if is_g:
                    self.g_value.line_edit.setText(str(random_number))
                else:
                    self.x_value.line_edit.setText(str(random_number))

        except:
            DialogWindow('Invalid', 'p value must be a prime number').exec_()

    def build_params(self):
        p = int(self.p_value.line_edit.text())
        g = int(self.g_value.line_edit.text())
        x = int(self.x_value.line_edit.text())
        return [p, g, x]
