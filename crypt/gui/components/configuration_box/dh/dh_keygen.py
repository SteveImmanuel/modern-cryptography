from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSizePolicy, QSpacerItem

from crypt.gui.components.configuration_box.base_keygen import BaseKeygen
from crypt.gui.components.configuration_box.edit_with_button import EditWithButton
from crypt.gui.dialog_window import DialogWindow
from crypt.utils.number_util import *


class DHKeygen(BaseKeygen):
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        self.n_value = EditWithButton('n value', 'Randomize')
        self.g_value = EditWithButton('g value', 'Randomize')
        self.x_value = EditWithButton('x value', 'Randomize')
        self.y_value = EditWithButton('y value', 'Randomize')
        self.spacer = QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.n_value)
        self.layout.addWidget(self.g_value)
        self.layout.addWidget(self.x_value)
        self.layout.addWidget(self.y_value)
        self.layout.addSpacerItem(self.spacer)

        self.setLayout(self.layout)

        self.n_value.btn_random.clicked.connect(lambda: self.randomize_prime(is_n=True))
        self.g_value.btn_random.clicked.connect(lambda: self.randomize_prime(is_n=False))
        self.x_value.btn_random.clicked.connect(lambda: self.randomize_number(is_x=True))
        self.y_value.btn_random.clicked.connect(lambda: self.randomize_number(is_x=False))

    def randomize_prime(self, is_n: bool):
        if(is_n):
            random_prime = generate_prime_number(10)
            self.n_value.line_edit.setText(str(random_prime))
        else:
            try:
                n = int(self.n_value.line_edit.text())

                if is_prime(n):
                    random_prime = generate_prime_number(9)
                    self.g_value.line_edit.setText(str(random_prime))
                    
                else:
                    DialogWindow('Invalid', 'n value must be a prime number').exec_()

            except:
                DialogWindow('Invalid', 'n value must be a prime number').exec_()


    def randomize_number(self, is_x: bool):
        try:
            n = int(self.n_value.line_edit.text())

            if is_prime(n):
                random_number = generate_random_number(1, n - 1)
                if is_x:
                    self.x_value.line_edit.setText(str(random_number))
                else:
                    self.y_value.line_edit.setText(str(random_number))
            else:
                DialogWindow('Invalid', 'n value must be a prime number').exec_()

        except:
            DialogWindow('Invalid', 'p value must be a prime number').exec_()

    def build_params(self):
        n = int(self.n_value.line_edit.text())
        g = int(self.g_value.line_edit.text())
        x = int(self.x_value.line_edit.text())
        y = int(self.y_value.line_edit.text())
        return [n, g, x, y]
