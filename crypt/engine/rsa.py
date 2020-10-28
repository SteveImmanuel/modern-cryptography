import math

from typing import List
from crypt.engine.base_engine import BaseEngine
from crypt.engine.key import *
from crypt.engine.data import *
from crypt.utils.number_util import *
from crypt.utils.string_util import *

from main import Ui_MainWindow
from PyQt5 import QtCore, QtWidgets, QtGui

class RSA(BaseEngine):
    def encrypt(self, public_key: Key, plain_text: Data):
        n = public_key.value[0]
        e = public_key.value[1]
        block_size = get_block_size(n)

        if plain_text.type == DataType.TEXT:
            block_text = group_string(plain_text.value, block_size)
            block_text = map(string_to_int, block_text)
            result = []
            for text in block_text:
                cipher = pow(text, e, n)
                result.append(str(cipher))
            return ' '.join(result)
        else:
            raise NotImplementedError('Belum dibuat')

    def decrypt(self, secret_key: Key, cipher_text: Data):
        n = secret_key.value[0]
        d = secret_key.value[1]

        if cipher_text.type == DataType.TEXT:
            block_text = cipher_text.value.split(' ')
            block_text = map(int, block_text)
            result = []
            for text in block_text:
                cipher = pow(text, d, n)
                result.append(int_to_string(cipher))
            return ''.join(result)
        else:
            raise NotImplementedError('Belum dibuat')

    def generate_key(self, params: List[int], output_path: str):
        p, q = params
        n = p * q
        toitent_n = toitent(p) * toitent(q)
        for i in range(toitent_n, 0, -1):
            if is_relative_prime(i, toitent_n):
                e = i
                break
        d = mod_inverse(e, toitent_n)
        return e, d, n

    def render(self, window: Ui_MainWindow):
        self.RSA_Key_Widget = QtWidgets.QWidget(window.customWidget)
        self.RSA_Key_Widget.setObjectName("RSA_Key_Widget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.RSA_Key_Widget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget = QtWidgets.QWidget(self.RSA_Key_Widget)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.P_Key_Text = QtWidgets.QLineEdit(self.widget)
        self.P_Key_Text.setObjectName("P_Key_Text")
        self.horizontalLayout_3.addWidget(self.P_Key_Text)
        self.verticalLayout_6.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.RSA_Key_Widget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.Q_Key_Text = QtWidgets.QLineEdit(self.widget_2)
        self.Q_Key_Text.setObjectName("Q_Key_Text")
        self.horizontalLayout_4.addWidget(self.Q_Key_Text)
        self.verticalLayout_6.addWidget(self.widget_2)
        window.horizontalLayout_9.addWidget(self.RSA_Key_Widget)

        self.retranslateUI()

    def retranslateUI(self):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "P"))
        self.label_2.setText(_translate("MainWindow", "Q"))


if __name__ == '__main__':
    rsa = RSA()
    data = Data(DataType.TEXT, 'abcdeajdkasdkakdsasdnoqjwneoqiwjeqowijeqwoiejqwoejio')
    e, d, n = rsa.generate_key([231, 491], 'a')
    public_key = Key([n, e])
    secret_key = Key([n, d])
    result = rsa.encrypt(public_key, data)
    print(result)
    data = Data(DataType.TEXT, result)
    result = rsa.decrypt(secret_key, data)
    print(result)