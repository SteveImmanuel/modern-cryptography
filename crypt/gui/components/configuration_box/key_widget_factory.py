from crypt.engine.engine_factory import EngineType
from crypt.gui.components.configuration_box.base_key_setup import BaseKeySetup
from crypt.gui.components.configuration_box.base_keygen import BaseKeygen
from crypt.gui.components.configuration_box.rsa.rsa_key_setup import RSAKeySetup
from crypt.gui.components.configuration_box.rsa.rsa_keygen import RSAKeygen
from crypt.gui.components.configuration_box.elgamal.elgamal_key_setup import ElgamalKeySetup
from crypt.gui.components.configuration_box.elgamal.elgamal_keygen import ElgamalKeygen
from crypt.gui.components.configuration_box.dh.dh_key_setup import DHKeySetup
from crypt.gui.components.configuration_box.dh.dh_keygen import DHKeygen


class KeyWidgetFactory():
    @staticmethod
    def create_keygen_widget(engine: EngineType) -> BaseKeygen:
        if engine == EngineType.RSA:
            return RSAKeygen()
        elif engine == EngineType.ELGAMAL:
            return ElgamalKeygen()
        elif engine == EngineType.DH:
            return DHKeygen()
        else:
            raise RuntimeError('Widget for engine type not found')

    @staticmethod
    def create_key_setup_widget(engine: EngineType) -> BaseKeySetup:
        if engine == EngineType.RSA:
            return RSAKeySetup()
        elif engine == EngineType.ELGAMAL:
            return ElgamalKeySetup()
        elif engine == EngineType.DH:
            return DHKeySetup()
        else:
            raise RuntimeError('Widget for engine type not found')
