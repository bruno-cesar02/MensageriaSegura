from bancoDeDados import GerenciadorBancoDeDados
from usuario import Usuario
from envioMensagens import Mensagem
from recebeMensagens import receber_mensagens


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



    print("\nFim do programa.")


if __name__ == '__main__':
    main()
