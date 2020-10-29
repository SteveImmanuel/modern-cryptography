from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSizePolicy, QSpacerItem

from crypt.gui.components.configuration_box.base_keygen import BaseKeygen
from crypt.gui.components.configuration_box.edit_with_button import EditWithButton
from crypt.utils.number_util import generate_prime_number


class RSAKeygen(BaseKeygen):
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        self.p_value = EditWithButton('p value', 'Randomize')
        self.q_value = EditWithButton('q value', 'Randomize')
        self.spacer = QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.p_value)
        self.layout.addWidget(self.q_value)
        self.layout.addSpacerItem(self.spacer)

        self.setLayout(self.layout)

        self.p_value.btn_random.clicked.connect(lambda: self.randomize(is_p=True))
        self.q_value.btn_random.clicked.connect(lambda: self.randomize(is_p=False))

    def randomize(self, is_p: bool):
        random_number = generate_prime_number(9)
        if is_p:
            self.p_value.line_edit.setText(str(random_number))
        else:
            self.q_value.line_edit.setText(str(random_number))

    def build_params(self):
        p = int(self.p_value.line_edit.text())
        q = int(self.q_value.line_edit.text())
        return [p, q]
