import pymongo
import bcrypt
from datetime import datetime

class GerenciadorBancoDeDados:
    """
    Classe para gerenciar a conexão e as operações com o MongoDB.
    """
    def __init__(self, string_conexao, nome_banco="chat"):
        """
        Inicializa o gerenciador de banco de dados.

        Args:
            string_conexao (str): A string de conexão para o MongoDB.
            nome_banco (str): O nome do banco de dados.
        """
        self.cliente = None
        self.banco = None
        
        try:
            print("Conectando ao MongoDB...")
            self.cliente = pymongo.MongoClient(string_conexao)
            # A linha abaixo força a conexão e verifica se o servidor está disponível
            self.cliente.admin.command('ping') 
            self.banco = self.cliente['chat']
            print("Conexão estabelecida com sucesso!")
        except pymongo.errors.ConnectionFailure as e:
            print(f"Não foi possível conectar ao MongoDB: {e}")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    def buscar_usuario(self, nome_usuario):
        """
        Busca um usuário pelo seu nome de usuário.
        
        Args:
            nome_usuario (str): O nome de usuário a ser buscado.

        Returns:
            dict: O documento do usuário, ou None se não for encontrado.
        """
        if not self.banco:
            print("Conexão com o banco não estabelecida.")
            return None
            
        colecao_usuarios = self.banco.users
        return colecao_usuarios.find_one({"username": nome_usuario})

    def adicionar_usuario(self, nome_usuario, senha):
        """
        Adiciona um novo usuário ao banco de dados com senha hasheada.

        Args:
            nome_usuario (str): O nome de usuário.
            senha (str): A senha em texto plano.

        Returns:
            bool: True se o usuário foi adicionado, False caso contrário.
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
    # ATENÇÃO: Substitua pela sua string de conexão do MongoDB Atlas
    STRING_DE_CONEXAO_MONGO = "mongodb+srv://brunocesarglm_db_user:bruno2006@mensageriasegura.fzzowy5.mongodb.net/?retryWrites=true&w=majority&appName=MensageriaSegura"

    gerenciador_db = GerenciadorBancoDeDados(STRING_DE_CONEXAO_MONGO)

   
    if gerenciador_db.banco is not None:
        configurar_usuarios_iniciais(gerenciador_db)
