from crypt.engine.engine_factory import EngineType
from crypt.gui.components.configuration_box.base_key_setup import BaseKeySetup
from crypt.gui.components.configuration_box.base_keygen import BaseKeygen
from crypt.gui.components.configuration_box.rsa.rsa_key_setup import RSAKeySetup
from crypt.gui.components.configuration_box.rsa.rsa_keygen import RSAKeygen
from crypt.gui.components.configuration_box.elgamal.elgamal_key_setup import ElgamalKeySetup
from crypt.gui.components.configuration_box.elgamal.elgamal_keygen import ElgamalKeygen

class KeyWidgetFactory():
    @staticmethod
    def create_keygen_widget(engine: EngineType) -> BaseKeygen:
        if engine == EngineType.RSA:
            return RSAKeygen()
        elif engine == EngineType.ELGAMAL:
            return ElgamalKeygen()
        else:
            return RSAKeygen()

    @staticmethod
    def create_key_setup_widget(engine: EngineType) -> BaseKeySetup:
        if engine == EngineType.RSA:
            return RSAKeySetup()
        elif engine == EngineType.ELGAMAL:
            return ElgamalKeySetup()
        else:
            return RSAKeySetup()
