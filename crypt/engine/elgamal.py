import random
import math

from typing import List
from crypt.engine.base_engine import BaseEngine
from crypt.engine.key import *
from crypt.engine.data import *
from crypt.utils.number_util import *
from crypt.utils.string_util import *

from main import Ui_MainWindow
from PyQt5 import QtCore, QtWidgets, QtGui

class Elgamal(BaseEngine):
    def encrypt(self, public_key: Key, plain_text: Data):
        y = public_key.value[0]
        g = public_key.value[1]
        p = public_key.value[2]

        block_size = get_block_size(p)

        if plain_text.type == DataType.TEXT:
            block_text = group_string(plain_text.value, block_size)
            block_text = map(string_to_int, block_text)
            result = []
            for text in block_text:
                k = random.randrange(1, p-1, 1)
                a = pow(g,k,p)

                b = (pow(y,k) * text) % p

                result.append(str(a))
                result.append(str(b))
            return ' '.join(result)
        else:
            raise NotImplementedError('Belum dibuat')

    def decrypt(self, secret_key: Key, cipher_text: Data):
        x = secret_key.value[0]
        p = secret_key.value[1]

        if cipher_text.type == DataType.TEXT:
            block_text = cipher_text.value.split(' ')
            block_text = map(int, block_text)
            result = []

            idx = 1
            a = 0
            b = 0
            
            for text in block_text:
                if (idx==1):
                    a = text
                    idx += 1
                else:
                    b = text
                    a_x_inverse = pow(a, p-1-x, p)
                    cipher = (b * a_x_inverse) % p
                    result.append(int_to_string(cipher))
                    idx = 1
            return ''.join(result)
        else:
            raise NotImplementedError('Belum dibuat')

    def generate_key(self, params: List[int], output_path: str):
        p, g, x = params
        y = pow(g,x,p)

        return g, p, x, y

    def render(self, window: Ui_MainWindow):
        self.Elgamal_Key_Widget = QtWidgets.QWidget(window.customWidget)
        self.Elgamal_Key_Widget.setObjectName("Elgamal_Key_Widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Elgamal_Key_Widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget1 = QtWidgets.QWidget(self.Elgamal_Key_Widget)
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.P_Key_Text = QtWidgets.QLineEdit(self.widget1)
        self.P_Key_Text.setObjectName("P_Key_Text")
        self.horizontalLayout_3.addWidget(self.P_Key_Text)
        self.verticalLayout_2.addWidget(self.widget1)
        self.widget2 = QtWidgets.QWidget(self.Elgamal_Key_Widget)
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.widget2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.G_Key_Text = QtWidgets.QLineEdit(self.widget2)
        self.G_Key_Text.setObjectName("G_Key_Text")
        self.horizontalLayout_4.addWidget(self.G_Key_Text)
        self.verticalLayout_2.addWidget(self.widget2)
        self.widget3 = QtWidgets.QWidget(self.Elgamal_Key_Widget)
        self.widget3.setObjectName("widget3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.widget3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.X_Key_Text = QtWidgets.QLineEdit(self.widget3)
        self.X_Key_Text.setObjectName("X_Key_Text")
        self.horizontalLayout_5.addWidget(self.X_Key_Text)
        self.verticalLayout_2.addWidget(self.widget3)
        window.horizontalLayout_9.addWidget(self.Elgamal_Key_Widget)

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Form", "P"))
        self.label_2.setText(_translate("Form", "G"))
        self.label_3.setText(_translate("Form", "X"))

if __name__ == "__main__":
    elgamal = Elgamal()
    data = Data(DataType.TEXT, 'abcdeajdkasdkakdsasdnoqjwneoqiwjeqowijeqwoiejqwoejio')
    g, p, x, y = elgamal.generate_key([2357, 2, 1751], 'a')
    public_key = Key([y, g, p])
    secret_key = Key([x,p])

    result = elgamal.encrypt(public_key, data)
    print(result)

    data = Data(DataType.TEXT, result)
    result = elgamal.decrypt(secret_key, data)
    print(result)