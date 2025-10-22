from bancoDeDados import GerenciadorBancoDeDados
from usuario import Usuario
from envioMensagens import Mensagem
from recebeMensagens import receber_mensagens

# Este será o arquivo principal da sua aplicação.
# Por enquanto, ele apenas importará o necessário e servirá como ponto de partida.

# from database import DatabaseManager
# from crypto import Criptografia # Será usado nos próximos passos
# from user import User           # Será usado nos próximos passos
# from message import Message     # Será usado nos próximos passos

def main():
    """
    Função principal que inicia a aplicação.
    """
    print("Bem-vindo ao sistema de Mensageria Segura!")
    STRING_DE_CONEXAO_MONGO = "mongodb+srv://juliano:8779130@mensageriasegura.fzzowy5.mongodb.net/?retryWrites=true&w=majority&appName=MensageriaSegura"
    gerenciador_db = GerenciadorBancoDeDados(STRING_DE_CONEXAO_MONGO)

    if gerenciador_db.banco is None:
        print("Erro ao conectar ao banco.")
        return
    
    usuario = Usuario()
    if not usuario.autenticar(gerenciador_db):
        return
    
    while True:
        print("\n1- Enviar mensagem")
        print("\n2- Ler Mensagem")
        print("\n0- Sair")

        opcao = input("Escolha uma opcao: ")

        match opcao:
            case "1":
                msg = Mensagem(usuario.nome_usuario, gerenciador_db)
                msg.enviar()
            case "2":
                receber_mensagens(usuario.nome_usuario, gerenciador_db)
            case "0":
                print("Saindo . . .")
                break
            case _:
                print("Opcao invalida.")


    # Nos próximos passos, a lógica de login e o menu principal virão aqui.
    # Por enquanto, o objetivo é apenas garantir que a conexão com o banco funciona.

    # 1. Definir a string de conexão
    # MONGO_CONNECTION_STRING = "SUA_CONNECTION_STRING_AQUI"

    # 2. Iniciar o gerenciador do banco de dados
    # db = DatabaseManager(MONGO_CONNECTION_STRING)

    print("\nFim do programa.")


if __name__ == '__main__':
    main()
