import bcrypt

# Precisamos do nosso gerenciador de banco para consultar os usuários
from bancoDeDados import GerenciadorBancoDeDados

class Usuario:
    """
    Representa um usuário e gerencia o processo de autenticação.
    """
    def __init__(self, nome_usuario=None):
        self.nome_usuario = nome_usuario

    def autenticar(self, gerenciador_db):
        """
        Realiza o processo de login, pedindo nome de usuário e senha.
        Verifica as credenciais contra o banco de dados.

        Args:
            gerenciador_db (GerenciadorBancoDeDados): A instância do gerenciador do banco.

        Returns:
            bool: True se a autenticação for bem-sucedida, False caso contrário.
        """
        # 1. Solicita as credenciais ao usuário no terminal
        nome_usuario_input = input("Digite seu nome de usuário (ex: @alice): ")
        # getpass esconde a senha enquanto o usuário digita, por segurança
        senha_input = input("Digite sua senha: ") 

        # 2. Busca o usuário no banco de dados
        dados_usuario = gerenciador_db.buscar_usuario(nome_usuario_input)

        # 3. Verifica se o usuário foi encontrado
        if not dados_usuario:
            print("\nAutenticação falhou: Usuário não encontrado.")
            return False

        # 4. Compara a senha fornecida com o hash armazenado no banco
        senha_hasheada_db = dados_usuario['password']
        
        # A função bcrypt.checkpw faz a comparação segura por nós
        if bcrypt.checkpw(senha_input.encode('utf-8'), senha_hasheada_db):
            print(f"\nAutenticação bem-sucedida! Bem-vindo, {nome_usuario_input}.")
            self.nome_usuario = nome_usuario_input # Armazena o usuário que logou com sucesso
            return True
        else:
            print("\nAutenticação falhou: Senha incorreta.")
            return False

# --- Bloco de Teste ---
if __name__ == '__main__':
    print("--- Testando Módulo de Autenticação de Usuário ---")

    # ATENÇÃO: Substitua pela sua string de conexão do MongoDB Atlas
    STRING_DE_CONEXAO_MONGO = "mongodb+srv://brunocesarglm_db_user:bruno2006@mensageriasegura.fzzowy5.mongodb.net/?retryWrites=true&w=majority&appName=MensageriaSegura"
    
    gerenciador_db = GerenciadorBancoDeDados(STRING_DE_CONEXAO_MONGO)

    # Verifica se a conexão com o banco foi bem-sucedida antes de continuar
    if gerenciador_db.banco is not None:
        # Cria uma instância de usuário para o teste
        usuario_teste = Usuario()
        
        print("\nPor favor, tente fazer o login.")
        # Inicia o processo de autenticação interativo
        usuario_teste.autenticar(gerenciador_db)
