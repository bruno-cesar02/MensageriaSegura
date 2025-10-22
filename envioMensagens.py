from datetime import datetime
from criptografia import Criptografia


class Mensagem:
    def __init__(self, remetente, gerenciador_db):
        self.remetente = remetente
        self.gerenciador_db = gerenciador_db
        self.cripto = Criptografia()

    def enviar(self):
        """
        Envia uma mensagem criptografada para outro usuário.
        """
        destinatario = input("Digite @destinatario: ").strip()
        if not destinatario.startswith("@"):
            destinatario = "@" + destinatario

        # verifica se o destinatário existe
        usuario_dest = self.gerenciador_db.buscar_usuario(destinatario)
        if not usuario_dest:
            print("Destinatário não encontrado no banco de dados.")
            return

        texto = input("Digite a mensagem (mínimo 50 caracteres): ").strip()
        if len(texto) < 50:
            print("Mensagem muito curta. Digite pelo menos 50 caracteres.")
            return

        chave = input("Digite a chave de criptografia (não será armazenada): ").strip()
        if not chave:
            print(" Chave inválida.")
            return

        # Cifrar a mensagem
        msg_cifrada = self.cripto.cifrar_mensagem(texto, chave)
        if not msg_cifrada:
            print("Erro ao criptografar a mensagem.")
            return

        # Inserir no banco
        try:
            colecao_msg = self.gerenciador_db.banco.messages
            doc = {
                "from": self.remetente,
                "to": destinatario,
                "message": msg_cifrada,
                "status": "nao_lida",
                "timestamp": datetime.utcnow()
            }
            colecao_msg.insert_one(doc)
            print("Mensagem enviada e armazenada de forma criptografada!")
        except Exception as e:
            print(f"Erro ao salvar mensagem: {e}")
