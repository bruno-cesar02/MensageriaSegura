# recebemensagens.py
from datetime import datetime
from bson import ObjectId
from criptografia import Criptografia

def receber_mensagens(usuario_logado: str, gerenciador_db):
    """
    Lê mensagens NÃO LIDAS destinadas a `usuario_logado`,
    pede a chave/senha, decifra e marca como 'lida'.
    """
    if gerenciador_db.banco is None:
        print("Erro: sem conexão com o banco.")
        return

    col = gerenciador_db.banco.messages

    # 1) Buscar mensagens não lidas para o usuário
    cursor = col.find(
        {"to": usuario_logado, "status": "nao_lida"},
        {"from": 1, "to": 1, "message": 1, "timestamp": 1}
    ).sort("timestamp", 1)

    msgs = list(cursor)
    if not msgs:
        print(" Você não tem mensagens não lidas.")
        return

    print(f"\nEncontradas {len(msgs)} mensagem(ns) não lida(s).")
    # 2) Pede a chave/senha (não armazene)
    chave = input("Digite a CHAVE/SENHA para decifrar: ").strip()
    if not chave:
        print("Chave/senha vazia.")
        return

    cripto = Criptografia()

    # 3) Tentar decifrar cada mensagem
    lidas_ids = []
    print("\n--- Mensagens ---")
    for m in msgs:
        cid = str(m.get("_id"))
        remetente = m.get("from")
        ts = m.get("timestamp")
        ts_fmt = ts.strftime("%Y-%m-%d %H:%M:%S") if isinstance(ts, datetime) else str(ts)

        ciphertext = m.get("message", "")

        texto = cripto.decifrar_mensagem(ciphertext, chave)  # retorna None se chave errada
        if texto is None:
            print(f"\n[{ts_fmt}] De {remetente}  (id: {cid})")
            print("Não foi possível decifrar (chave incorreta?).")
            continue

        print(f"\n[{ts_fmt}] De {remetente}  (id: {cid})")
        print("Mensagem:")
        print(texto)

        # coletar para marcar como lida
        lidas_ids.append(m["_id"])

    # 4) Marcar como lidas as que foram decifradas
    if lidas_ids:
        col.update_many(
            {"_id": {"$in": lidas_ids}},
            {"$set": {"status": "lida"}}
        )
        print(f"\n Marcadas como 'lida' {len(lidas_ids)} mensagem(ns) decifrada(s).")
    else:
        print("\nNenhuma mensagem foi decifrada; nada marcado como lida.")
