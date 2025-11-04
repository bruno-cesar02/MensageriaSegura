from bancoDeDados import GerenciadorBancoDeDados
from usuario import Usuario
from envioMensagens import Mensagem
from recebeMensagens import receber_mensagens

def main():
    """
    Função principal que inicia a aplicação.
    """
    # MELHORIA: Interface mais amigável
    print("\n" + "="*60)
    print("     BEM-VINDO AO SISTEMA DE MENSAGERIA SEGURA")
    print("="*60 + "\n")
    
    # Cria APENAS UMA conexão que será reutilizada
    gerenciador_db = GerenciadorBancoDeDados()

    if gerenciador_db.banco is None:
        print("Erro ao conectar ao banco.")
        return
    
    # Login do usuário
    usuario = Usuario()
    if not usuario.autenticar(gerenciador_db):
        return
    
    # Menu principal
    while True:
        print("\n" + "-"*60)
        print("MENU PRINCIPAL")
        print("-"*60)
        print("1 - Enviar mensagem")
        print("2 - Ler mensagens")
        print("0 - Sair")
        print("-"*60)

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

    print("Fim do programa.")


if __name__ == '__main__':
    main()