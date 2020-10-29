from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QFileDialog
from PyQt5.QtCore import QSize, QThreadPool

from crypt.gui.components.main_input import MainInput
from crypt.gui.components.configuration_box import ConfigurationBox
from crypt.gui.dialog_window import DialogWindow
from crypt.gui.encryption_parms import EncryptionParms, ModeType
from crypt.gui.worker import Worker
from crypt.engine.engine_factory import EngineType
from crypt.engine.data import *
from crypt.utils.file_util import *

from multiprocessing import cpu_count


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.enc_parms = EncryptionParms.get_instance()
        QThreadPool.globalInstance().setMaxThreadCount(cpu_count() - 1)

        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle('Modern Cryptography')
        self.setMinimumSize(950, 600)
        self.central_widget = QtWidgets.QWidget(self)

        self.main_input = MainInput(self.central_widget)
        self.configuration_box = ConfigurationBox(self.central_widget)

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.configuration_box)
        self.layout.addWidget(self.main_input)

        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

        self.main_input.tab_string.input_mode.btn_execute.clicked.connect(self.execute_string)
        self.main_input.tab_file.input_mode.btn_execute.clicked.connect(self.execute_file)

        self.main_input.tab_string.output_string.btn_save_to_file.clicked.connect(self.save_to_file)
        self.main_input.tab_string.input_string.btn_load_from_file.clicked.connect(self.load_from_file)

        output_conf_signal = EncryptionParms.get_instance().signal.output_type
        # output_conf_slot = self.main_input.tab_string.output_string.on_change_format
        # output_conf_signal.connect(output_conf_slot)

        engine_type_signal = EncryptionParms.get_instance().signal.engine_type
        # engine_type_slot = self.configuration_box.encryption_box.on_update_key_widget
        # engine_type_slot_2 = self.main_input.on_engine_change
        # engine_type_signal.connect(engine_type_slot)
        # engine_type_signal.connect(engine_type_slot_2)

        self.configuration_box.keygen.btn_generate.clicked.connect(self.generate_key)

    def show_dialog_window(self, title, msg):
        DialogWindow(title, msg).exec_()

    def show_error_dialog(self, error_msg):
        self.show_dialog_window('Error', error_msg)

    def show_success_window(self, msg):
        self.show_dialog_window('Success', msg)

    def load_from_file(self):
        filepath, _ = QFileDialog.getOpenFileName(
            self, 'Load Text', QtCore.QDir.currentPath(), '*.txt'
        )
        if filepath:
            worker = Worker(read_file, filepath)
            worker.signals.error.connect(self.show_error_dialog)
            worker.signals.result.connect(self.main_input.tab_string.input_string.on_load_from_file)
            QThreadPool.globalInstance().start(worker)

    def save_to_file(self):
        filepath, _ = QFileDialog.getSaveFileName(self, 'Save Text', QtCore.QDir.currentPath(), '*')
        if filepath:
            worker = Worker(
                save_file, filepath,
                self.main_input.tab_string.output_string.text_edit.toPlainText()
            )
            worker.signals.error.connect(self.show_error_dialog)
            worker.signals.result.connect(lambda: self.show_success_window("Success saving file"))
            QThreadPool.globalInstance().start(worker)

    def generate_key(self):
        engine = self.enc_parms.get_engine()
        output_path = self.configuration_box.keygen.output_file.line_edit.text()
        params = self.configuration_box.keygen.key_input.build_params()
        worker = Worker(engine.generate_key, params, output_path)
        worker.signals.error.connect(self.show_error_dialog)
        worker.signals.result.connect(self.show_success_window)
        QThreadPool.globalInstance().start(worker)

    def prepare_exec_fun(self):
        mode = self.enc_parms.mode
        engine = self.enc_parms.get_engine()
        data = self.main_input.get_data()

        if mode == ModeType.ENCRYPT:
            fn = engine.encrypt
            key = self.configuration_box.key_setup.get_key(is_private=False)
        else:
            fn = engine.decrypt
            key = self.configuration_box.key_setup.get_key(is_private=True)

        return fn, key, data

    def execute_string(self):
        try:
            fn, key, data = self.prepare_exec_fun()
        except Exception as e:
            self.show_error_dialog(str(e))
            return

        worker = Worker(fn, key, data)
        worker.signals.error.connect(self.show_error_dialog)
        worker.signals.result.connect(self.main_input.tab_string.output_string.on_result_update)
        QThreadPool.globalInstance().start(worker)

    def execute_file(self):
        try:
            fn, key, data = self.prepare_exec_fun()
        except Exception as e:
            self.show_error_dialog(str(e))
            return

        worker = Worker(fn, key, data)
        worker.signals.error.connect(self.show_error_dialog)
        worker.signals.result.connect(self.show_success_window)
        QThreadPool.globalInstance().start(worker)
