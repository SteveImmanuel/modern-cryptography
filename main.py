import sys
import mimetypes

from crypt import *
from enum import Enum
from PyQt5 import QtCore, QtGui, QtWidgets

class FileCategory(Enum):
    PLAINTEXT = 'plaintext'
    CIPHERTEXT = 'ciphertext'
    PUBLICKEY = 'publickey'
    PRIVATEKEY = 'privatekey'

class Ui_MainWindow(object):
    def __init__(self):
        self.encrypt = RSA()
        print("RSA")
        self.encrypt_list = [
            RSA(),
            Elgamal()
        ]

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setAcceptDrops(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.Encryption_Option = QtWidgets.QComboBox(self.centralwidget)
        self.Encryption_Option.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Encryption_Option.setFont(font)
        self.Encryption_Option.setObjectName("Encryption_Option")
        self.Encryption_Option.addItem("")
        self.Encryption_Option.addItem("")
        self.verticalLayout_8.addWidget(self.Encryption_Option)
        self.Main_Frame = QtWidgets.QFrame(self.centralwidget)
        self.Main_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Main_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Main_Frame.setObjectName("Main_Frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Main_Frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Plaintext_GroupBox = QtWidgets.QGroupBox(self.Main_Frame)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.Plaintext_GroupBox.setFont(font)
        self.Plaintext_GroupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.Plaintext_GroupBox.setObjectName("Plaintext_GroupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Plaintext_GroupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Plaintext_Text = QtWidgets.QPlainTextEdit(self.Plaintext_GroupBox)
        self.Plaintext_Text.setObjectName("Plaintext_Text")
        self.verticalLayout_4.addWidget(self.Plaintext_Text)
        self.widget_5 = QtWidgets.QWidget(self.Plaintext_GroupBox)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.Open_Plaintext_Button = QtWidgets.QPushButton(self.widget_5)
        self.Open_Plaintext_Button.setMinimumSize(QtCore.QSize(0, 70))
        self.Open_Plaintext_Button.setAcceptDrops(False)
        self.Open_Plaintext_Button.setIconSize(QtCore.QSize(16, 16))
        self.Open_Plaintext_Button.setCheckable(False)
        self.Open_Plaintext_Button.setDefault(False)
        self.Open_Plaintext_Button.setFlat(False)
        self.Open_Plaintext_Button.setObjectName("Open_Plaintext_Button")
        self.horizontalLayout_7.addWidget(self.Open_Plaintext_Button)
        self.Save_Plaintext_Button = QtWidgets.QPushButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Save_Plaintext_Button.sizePolicy().hasHeightForWidth())
        self.Save_Plaintext_Button.setSizePolicy(sizePolicy)
        self.Save_Plaintext_Button.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.Save_Plaintext_Button.setFont(font)
        self.Save_Plaintext_Button.setAcceptDrops(False)
        self.Save_Plaintext_Button.setObjectName("Save_Plaintext_Button")
        self.horizontalLayout_7.addWidget(self.Save_Plaintext_Button)
        self.verticalLayout_4.addWidget(self.widget_5)
        self.Encrypt_Button = QtWidgets.QPushButton(self.Plaintext_GroupBox)
        self.Encrypt_Button.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Encrypt_Button.setFont(font)
        self.Encrypt_Button.setObjectName("Encrypt_Button")
        self.verticalLayout_4.addWidget(self.Encrypt_Button)
        self.horizontalLayout.addWidget(self.Plaintext_GroupBox)
        self.Key_GroupBox = QtWidgets.QGroupBox(self.Main_Frame)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.Key_GroupBox.setFont(font)
        self.Key_GroupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.Key_GroupBox.setObjectName("Key_GroupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Key_GroupBox)
        self.verticalLayout.setObjectName("verticalLayout")

        self.customWidget = QtWidgets.QWidget(self.Key_GroupBox)
        self.customWidget.setObjectName("CustomWidget")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.customWidget)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout.addWidget(self.customWidget)

        self.GenerateKey_Button = QtWidgets.QPushButton(self.Key_GroupBox)
        self.GenerateKey_Button.setObjectName("GenerateKey_Button")
        self.verticalLayout.addWidget(self.GenerateKey_Button)
        self.PublicKey_GroupBox = QtWidgets.QGroupBox(self.Key_GroupBox)
        self.PublicKey_GroupBox.setObjectName("PublicKey_GroupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.PublicKey_GroupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.PublicKey_Text = QtWidgets.QPlainTextEdit(self.PublicKey_GroupBox)
        self.PublicKey_Text.setObjectName("PublicKey_Text")
        self.verticalLayout_2.addWidget(self.PublicKey_Text)
        self.widget_3 = QtWidgets.QWidget(self.PublicKey_GroupBox)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Open_PublicKey_Button = QtWidgets.QPushButton(self.widget_3)
        self.Open_PublicKey_Button.setObjectName("Open_PublicKey_Button")
        self.horizontalLayout_5.addWidget(self.Open_PublicKey_Button)
        self.Save_PublicKey_Button = QtWidgets.QPushButton(self.widget_3)
        self.Save_PublicKey_Button.setObjectName("Save_PublicKey_Button")
        self.horizontalLayout_5.addWidget(self.Save_PublicKey_Button)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.verticalLayout.addWidget(self.PublicKey_GroupBox)
        self.PrivateKey_GroupBox = QtWidgets.QGroupBox(self.Key_GroupBox)
        self.PrivateKey_GroupBox.setObjectName("PrivateKey_GroupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.PrivateKey_GroupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.PrivateKey_Text = QtWidgets.QPlainTextEdit(self.PrivateKey_GroupBox)
        self.PrivateKey_Text.setObjectName("PrivateKey_Text")
        self.verticalLayout_3.addWidget(self.PrivateKey_Text)
        self.widget_4 = QtWidgets.QWidget(self.PrivateKey_GroupBox)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Open_PrivateKey_Button = QtWidgets.QPushButton(self.widget_4)
        self.Open_PrivateKey_Button.setObjectName("Open_PrivateKey_Button")
        self.horizontalLayout_6.addWidget(self.Open_PrivateKey_Button)
        self.Save_PrivateKey_Button = QtWidgets.QPushButton(self.widget_4)
        self.Save_PrivateKey_Button.setObjectName("Save_PrivateKey_Button")
        self.horizontalLayout_6.addWidget(self.Save_PrivateKey_Button)
        self.verticalLayout_3.addWidget(self.widget_4)
        self.verticalLayout.addWidget(self.PrivateKey_GroupBox)
        self.horizontalLayout.addWidget(self.Key_GroupBox)
        self.Ciphertext_GroupBox = QtWidgets.QGroupBox(self.Main_Frame)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.Ciphertext_GroupBox.setFont(font)
        self.Ciphertext_GroupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.Ciphertext_GroupBox.setObjectName("Ciphertext_GroupBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.Ciphertext_GroupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.CipherText_Text = QtWidgets.QPlainTextEdit(self.Ciphertext_GroupBox)
        self.CipherText_Text.setObjectName("CipherText_Text")
        self.verticalLayout_5.addWidget(self.CipherText_Text)
        self.widget_6 = QtWidgets.QWidget(self.Ciphertext_GroupBox)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.Open_Ciphertext_Button = QtWidgets.QPushButton(self.widget_6)
        self.Open_Ciphertext_Button.setMinimumSize(QtCore.QSize(0, 70))
        self.Open_Ciphertext_Button.setAcceptDrops(False)
        self.Open_Ciphertext_Button.setIconSize(QtCore.QSize(16, 16))
        self.Open_Ciphertext_Button.setCheckable(False)
        self.Open_Ciphertext_Button.setDefault(False)
        self.Open_Ciphertext_Button.setFlat(False)
        self.Open_Ciphertext_Button.setObjectName("Open_Ciphertext_Button")
        self.horizontalLayout_8.addWidget(self.Open_Ciphertext_Button)
        self.Save_Ciphertext_Button = QtWidgets.QPushButton(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Save_Ciphertext_Button.sizePolicy().hasHeightForWidth())
        self.Save_Ciphertext_Button.setSizePolicy(sizePolicy)
        self.Save_Ciphertext_Button.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.Save_Ciphertext_Button.setFont(font)
        self.Save_Ciphertext_Button.setAcceptDrops(False)
        self.Save_Ciphertext_Button.setObjectName("Save_Ciphertext_Button")
        self.horizontalLayout_8.addWidget(self.Save_Ciphertext_Button)
        self.verticalLayout_5.addWidget(self.widget_6)
        self.Decrypt_Button = QtWidgets.QPushButton(self.Ciphertext_GroupBox)
        self.Decrypt_Button.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Decrypt_Button.setFont(font)
        self.Decrypt_Button.setObjectName("Decrypt_Button")
        self.verticalLayout_5.addWidget(self.Decrypt_Button)
        self.horizontalLayout.addWidget(self.Ciphertext_GroupBox)
        self.verticalLayout_8.addWidget(self.Main_Frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Encryption_Option.currentIndexChanged.connect(self.changeEncryption)

        #Open File Text Button Listener
        self.Open_Plaintext_Button.clicked.connect(self.openPlaintextButtonCallback)
        self.Open_Ciphertext_Button.clicked.connect(self.openCiphertextButtonCallback)
        self.Open_PublicKey_Button.clicked.connect(self.openPublicKeyButtonCallback)
        self.Open_PrivateKey_Button.clicked.connect(self.openPrivateKeyButtonCallback)

        #Save File Text Button Listener
        self.Save_Plaintext_Button.clicked.connect(self.savePlaintextButtonCallback)
        self.Save_Ciphertext_Button.clicked.connect(self.saveCiphertextButtonCallback)
        self.Save_PublicKey_Button.clicked.connect(self.savePublicKeyButtonCallback)
        self.Save_PrivateKey_Button.clicked.connect(self.savePrivateKeyButtonCallback)

        self.encrypt.render(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Encryption_Option.setItemText(0, _translate("MainWindow", "RSA"))
        self.Encryption_Option.setItemText(1, _translate("MainWindow", "Elgamal"))
        self.Plaintext_GroupBox.setTitle(_translate("MainWindow", "Plaintext"))
        self.Open_Plaintext_Button.setText(_translate("MainWindow", "Open\nPlaintext\nFile"))
        self.Save_Plaintext_Button.setText(_translate("MainWindow", "Save\nPlaintext\nFile"))
        self.Encrypt_Button.setText(_translate("MainWindow", "Encrypt"))
        self.Key_GroupBox.setTitle(_translate("MainWindow", "Key"))
        self.GenerateKey_Button.setText(_translate("MainWindow", "Generate Key"))
        self.PublicKey_GroupBox.setTitle(_translate("MainWindow", "Public Key"))
        self.Open_PublicKey_Button.setText(_translate("MainWindow", "Open Key"))
        self.Save_PublicKey_Button.setText(_translate("MainWindow", "Save Key"))
        self.PrivateKey_GroupBox.setTitle(_translate("MainWindow", "Private Key"))
        self.Open_PrivateKey_Button.setText(_translate("MainWindow", "Open Key"))
        self.Save_PrivateKey_Button.setText(_translate("MainWindow", "Save Key"))
        self.Ciphertext_GroupBox.setTitle(_translate("MainWindow", "Ciphertext"))
        self.Open_Ciphertext_Button.setText(_translate("MainWindow", "Open\nCiphertext\nFile"))
        self.Save_Ciphertext_Button.setText(_translate("MainWindow", "Save\nCiphertext\nFile"))
        self.Decrypt_Button.setText(_translate("MainWindow", "Decrypt"))

    def clean(self, layout):
        for i in reversed(range(layout.count())):
            item = layout.takeAt(i)
            widget = item.widget()
            if widget is not None:
                widget.close()
            else:
                self.clean(item.layout())

    def changeEncryption(self, idx: int):
        self.clean(self.horizontalLayout_9)
        self.encrypt = self.encrypt_list[idx]
        self.encrypt.render(self)

    def openPlaintextButtonCallback(self):
        self.openFileText(FileCategory.PLAINTEXT)

    def openCiphertextButtonCallback(self):
        self.openFileText(FileCategory.CIPHERTEXT)

    def openPublicKeyButtonCallback(self):
        self.openFileText(FileCategory.PUBLICKEY)

    def openPrivateKeyButtonCallback(self):
        self.openFileText(FileCategory.PRIVATEKEY)

    def openFileText(self, data:FileCategory):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            None,
            "Select Media File",
            "",
            "All Files (*)",
        )
        if fileName:
            mime = mimetypes.guess_type(fileName)
            print(mime)
            if mime[0] and mime[0].split('/')[0] == 'text':
                with open(fileName, 'r') as f:
                    if data==FileCategory.PLAINTEXT:
                        self.Plaintext_Text.setPlainText(f.read())
                    elif data==FileCategory.CIPHERTEXT:
                        self.CipherText_Text.setPlainText(f.read())
                    elif data==FileCategory.PUBLICKEY:  
                        self.PublicKey_Text.setPlainText(f.read())
                    elif data==FileCategory.PRIVATEKEY:
                        self.PrivateKey_Text.setPlainText(f.read())

    def savePlaintextButtonCallback(self):
        self.saveFileText(FileCategory.PLAINTEXT)

    def saveCiphertextButtonCallback(self):
        self.saveFileText(FileCategory.CIPHERTEXT)

    def savePublicKeyButtonCallback(self):
        self.saveFileText(FileCategory.PUBLICKEY)

    def savePrivateKeyButtonCallback(self):
        self.saveFileText(FileCategory.PRIVATEKEY)

    def saveFileText(self, data:FileCategory):
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(
            None,
            "Select File to Save Output Text",
            "",
            "All Files (*)",
        )
        if fileName:
            with open(fileName, 'w') as f:
                if data==FileCategory.PLAINTEXT:
                    f.write(self.Plaintext_Text.toPlainText())
                elif data==FileCategory.CIPHERTEXT:
                    f.write(self.CipherText_Text.toPlainText())
                elif data==FileCategory.PUBLICKEY:  
                    f.write(self.PublicKey_Text.toPlainText())
                elif data==FileCategory.PRIVATEKEY:
                    f.write(self.PrivateKey_Text.toPlainText())

if __name__ == "__main__":
    #Try Main RSA
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

    #Try Main Elgamal
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

    #Main
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())