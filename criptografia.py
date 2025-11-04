from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class Criptografia:
    """
    Classe para gerenciar as operações de cifrar e decifrar mensagens.
    Utiliza o algoritmo Fernet (AES simétrico).
    """

    def _derivar_chave(self, chave_texto):
        """
        Gera uma chave de criptografia segura a partir de uma senha de texto.
        Isso garante que a chave usada pelo Fernet tenha sempre o formato correto.
        
        Args:
            chave_texto (str): A senha fornecida pelo usuário.

        Returns:
            bytes: A chave pronta para ser usada na criptografia.
        """
        salt = b'salt_estatico_para_o_projeto' 
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        # Transforma a chave de texto em uma chave de 32 bytes, URL-safe base64 encoded
        chave_derivada = base64.urlsafe_b64encode(kdf.derive(chave_texto.encode('utf-8')))
        return chave_derivada

    def cifrar_mensagem(self, mensagem, chave_texto):
        """
        Cifra uma mensagem usando a chave fornecida.

        Args:
            mensagem (str): A mensagem a ser criptografada.
            chave_texto (str): A chave em texto plano fornecida pelo usuário.

        Returns:
            str: A mensagem criptografada, ou None em caso de erro.
        """
        try:
            chave_segura = self._derivar_chave(chave_texto)
            fernet = Fernet(chave_segura)
            mensagem_cifrada_bytes = fernet.encrypt(mensagem.encode('utf-8'))
            return mensagem_cifrada_bytes.decode('utf-8')
        except Exception as e:
            print(f"Erro ao cifrar a mensagem: {e}")
            return None

    def decifrar_mensagem(self, mensagem_cifrada, chave_texto):
        """
        Decifra uma mensagem usando a chave fornecida.

        Args:
            mensagem_cifrada (str): A mensagem que foi criptografada.
            chave_texto (str): A chave em texto plano fornecida pelo usuário.

        Returns:
            str: A mensagem original em texto plano, ou None se a chave for incorreta ou houver outro erro.
        """
        try:
            chave_segura = self._derivar_chave(chave_texto)
            fernet = Fernet(chave_segura)
            mensagem_decifrada_bytes = fernet.decrypt(mensagem_cifrada.encode('utf-8'))
            return mensagem_decifrada_bytes.decode('utf-8')
        except Exception as e:
            # Este erro geralmente acontece se a chave estiver incorreta
            print(f"Erro ao decifrar a mensagem. A chave pode estar incorreta.")
            return None

if __name__ == '__main__':
    # Bloco para testar a classe de criptografia de forma independente
    print("--- Testando Módulo de Criptografia ---")
    
    # 1. Cria uma instância da nossa classe
    cripto = Criptografia()
    
    # 2. Define uma mensagem e uma chave para o teste
    minha_mensagem_secreta = "Esta é uma mensagem de teste super secreta com mais de cinquenta caracteres para cumprir os requisitos."
    minha_chave = "chave_forte_123"
    
    print(f"\nMensagem Original: {minha_mensagem_secreta}")
    print(f"Chave Utilizada: {minha_chave}")
    
    # 3. Cifra a mensagem
    mensagem_cifrada = cripto.cifrar_mensagem(minha_mensagem_secreta, minha_chave)
    print(f"\nMensagem Cifrada: {mensagem_cifrada}")
    
    # 4. Decifra a mensagem
    if mensagem_cifrada:
        mensagem_decifrada = cripto.decifrar_mensagem(mensagem_cifrada, minha_chave)
        print(f"\nMensagem Decifrada: {mensagem_decifrada}")

        # Teste de falha (chave incorreta)
        print("\n--- Testando com chave incorreta ---")
        chave_errada = "chave_errada_456"
        print(f"Tentando decifrar com a chave: {chave_errada}")
        mensagem_falha = cripto.decifrar_mensagem(mensagem_cifrada, chave_errada)
        if not mensagem_falha:
            print("Teste de falha bem-sucedido: A mensagem não foi decifrada como esperado.")
