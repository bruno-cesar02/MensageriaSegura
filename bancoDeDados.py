import pymongo
import bcrypt
from datetime import datetime
from config import MONGO_CONNECTION_STRING, DATABASE_NAME

class GerenciadorBancoDeDados:
    
    #Classe para gerenciar a conexão e as operações com o MongoDB.
    #MELHORIAS: Conexão mais rápida e reutilização

    def __init__(self):
        """
        Inicializa o gerenciador de banco de dados.
        """
        self.cliente = None
        self.banco = None
        
        try:
            print("Conectando ao MongoDB...")
            
            # MELHORIA: Configurações para conexão mais rápida e estável
            self.cliente = pymongo.MongoClient(
                MONGO_CONNECTION_STRING,
                serverSelectionTimeoutMS=5000,  # Timeout de 5 segundos
                maxPoolSize=10,                 # Reutiliza até 10 conexões
            )
            
            # Testa a conexão
            self.cliente.admin.command('ping')
            self.banco = self.cliente[DATABASE_NAME]
            print("Conexão estabelecida com sucesso!")
            
        except pymongo.errors.ConnectionFailure as e:
            print(f"Não foi possível conectar ao MongoDB: {e}")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    def buscar_usuario(self, nome_usuario):
        """
        Busca um usuário pelo seu nome de usuário.
        """
        if self.banco is None:
            print("Conexão com o banco não estabelecida.")
            return None
            
        colecao_usuarios = self.banco.users
        return colecao_usuarios.find_one({"username": nome_usuario})

    def adicionar_usuario(self, nome_usuario, senha):
        """
        Adiciona um novo usuário ao banco de dados com senha hasheada.
        """
        if self.banco is None:
            print("Conexão com o banco não estabelecida.")
            return False

        colecao_usuarios = self.banco.users

        if colecao_usuarios.find_one({"username": nome_usuario}):
            print(f"Usuário '{nome_usuario}' já existe.")
            return False

        senha_hasheada = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())

        dados_usuario = {
            "username": nome_usuario,
            "password": senha_hasheada
        }

        try:
            colecao_usuarios.insert_one(dados_usuario)
            print(f"Usuário '{nome_usuario}' adicionado com sucesso.")
            return True
        except Exception as e:
            print(f"Erro ao adicionar usuário: {e}")
            return False


def configurar_usuarios_iniciais(gerenciador_db):
    """
    Função auxiliar para criar usuários de teste no banco de dados.
    """
    print("\nConfigurando usuários iniciais...")
    gerenciador_db.adicionar_usuario("@alice", "senha123")
    gerenciador_db.adicionar_usuario("@bob", "senha456")
    print("Configuração de usuários de teste finalizada.")


if __name__ == '__main__':
    # AGORA A STRING VEM DO config.py - em um único lugar!
    gerenciador_db = GerenciadorBancoDeDados()
   
    if gerenciador_db.banco is not None:
        configurar_usuarios_iniciais(gerenciador_db)