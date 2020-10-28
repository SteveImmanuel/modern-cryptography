from enum import Enum

from crypt.engine.engine_factory import EngineType
from crypt.gui.components.configuration_box.base_keygen import BaseKeygen
from crypt.gui.components.configuration_box.base_key_setup import BaseKeySetup
from crypt.gui.components.configuration_box.rsa.rsa_keygen import RSAKeygen
from crypt.gui.components.configuration_box.rsa.rsa_key_setup import RSAKeySetup
# from crypt.gui.components.configuration_box.string_full_key import StringFullKey
# from crypt.gui.components.configuration_box.hill_key import HillKey
# from crypt.gui.components.configuration_box.affine_key import AffineKey
# from crypt.gui.components.configuration_box.enigma_key import EnigmaKey


class KeyWidgetFactory():
    @staticmethod
    def create_keygen_widget(engine: EngineType) -> BaseKeygen:
        if engine == EngineType.RSA:
            return RSAKeygen()
        # elif engine == EngineType.ELGAMAL:
        #     return StringFullKey()
        else:
            return RSAKeygen()

    @staticmethod
    def create_key_setup_widget(engine: EngineType) -> BaseKeySetup:
        if engine == EngineType.RSA:
            return RSAKeySetup()
        # elif engine == EngineType.ELGAMAL:
        #     return StringFullKey()
        else:
            return RSAKeySetup()
