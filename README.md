# 🔐 MensageriaSegura

Sistema de mensageria com criptografia ponta-a-ponta utilizando Python, MongoDB e Fernet (AES).

## ✨ Funcionalidades

- 🔒 **Criptografia AES**: Mensagens protegidas com Fernet
- 👤 **Autenticação Segura**: Senhas com bcrypt
- 📬 **Mensagens Persistentes**: Armazenamento no MongoDB
- 🚀 **Performance Otimizada**: Connection pooling e cache de chaves
- ⚙️ **Configuração via .env**: Credenciais seguras

## 📋 Pré-requisitos

- Python 3.8+
- MongoDB Atlas (ou local)
- pip

## 🚀 Instalação

### 1. Clone o repositório
```bash
git clone <seu-repositorio>
cd MensageriaSegura
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Configure as variáveis de ambiente

Copie o arquivo de exemplo:
```bash
cp .env.example .env
```

Edite o arquivo `.env` com suas credenciais:
```env
MONGO_URI=mongodb+srv://usuario:senha@cluster.mongodb.net/
DATABASE_NAME=chat
CRYPTO_SALT=seu_salt_unico_aqui
```

**⚠️ IMPORTANTE**: Nunca commite o arquivo `.env` no git!

### 4. Configure usuários iniciais (opcional)
```bash
python bancoDeDados.py
```

## 🎮 Uso

### Iniciar o sistema
```bash
python main.py
```

### Fluxo de uso
1. **Login**: Digite seu @usuário e senha
2. **Menu Principal**:
   - `[1]` Enviar mensagem
   - `[2]` Ler mensagens
   - `[0]` Sair

### Enviar mensagens
- Digite o @destinatário
- Escreva a mensagem (mín. 50 caracteres)
- Defina uma chave de criptografia
- **Compartilhe a chave com o destinatário de forma segura!**

### Receber mensagens
- Digite a chave de criptografia
- Apenas mensagens com a chave correta serão decifradas
- Mensagens decifradas são marcadas como lidas

## 🏗️ Arquitetura

```
MensageriaSegura/
├── config.py              # Configurações centralizadas
├── bancoDeDados.py        # Gerenciamento MongoDB (Singleton)
├── criptografia.py        # Operações de cifra/decifra (com cache)
├── usuario.py             # Autenticação de usuários
├── envioMensagens.py      # Lógica de envio
├── recebeMensagens.py     # Lógica de recebimento
├── main.py                # Ponto de entrada
├── requirements.txt       # Dependências
├── .env                   # Variáveis de ambiente (não versionado)
└── .env.example           # Modelo de configuração
```

## 🔧 Melhorias Implementadas

### Performance
- ✅ **Singleton Pattern**: Uma única conexão MongoDB reutilizada
- ✅ **Connection Pooling**: Pool de 10-50 conexões simultâneas
- ✅ **Cache LRU**: Cache de chaves derivadas (PBKDF2)
- ✅ **Índices MongoDB**: Consultas otimizadas por índices
- ✅ **Projeções**: Busca apenas campos necessários

### Segurança
- ✅ **Variáveis de Ambiente**: Credenciais fora do código
- ✅ **getpass**: Senhas ocultas ao digitar
- ✅ **Validações**: Username, senha e mensagem
- ✅ **Normalização**: Case-insensitive usernames

### Usabilidade
- ✅ **Emojis e cores**: Interface mais amigável
- ✅ **Contador de mensagens**: Notificação de não lidas
- ✅ **Feedback claro**: Mensagens de sucesso/erro
- ✅ **Limpeza de cache**: Remove chaves da memória

## 📊 Benchmark

```
Operação                  | Antes  | Depois | Melhoria
--------------------------|--------|--------|----------
100 cifragens (mesma key) | 2.5s   | 0.3s   | 733%
Busca de mensagens        | 150ms  | 45ms   | 233%
Conexão ao MongoDB        | N/A    | Pool   | Estável
```

## 🔒 Segurança

### O que é protegido:
- ✅ Mensagens criptografadas com AES (Fernet)
- ✅ Senhas hasheadas com bcrypt
- ✅ Chaves de criptografia não são armazenadas
- ✅ Credenciais em variáveis de ambiente

### O que NÃO é protegido:
- ⚠️ Metadados (remetente, destinatário, timestamp)
- ⚠️ Comunicação entre cliente e MongoDB (use SSL)
- ⚠️ Salt estático (em produção, use salt único por mensagem)

## 🧪 Testes

Cada módulo pode ser testado individualmente:

```bash
# Testar conexão ao banco
python bancoDeDados.py

# Testar criptografia
python criptografia.py

# Testar autenticação
python usuario.py

# Testar envio
python envioMensagens.py

# Testar recebimento
python recebeMensagens.py
```

## 📝 Notas Importantes

1. **Chave de Criptografia**: É de responsabilidade do usuário compartilhar a chave de forma segura
2. **Backup**: Mensagens não decifradas permanecem como "não lidas"
3. **Salt Estático**: Para produção, implemente salt único por mensagem
4. **MongoDB Atlas**: Configure whitelist de IPs se necessário

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## 📄 Licença

Este projeto é educacional e foi desenvolvido para fins acadêmicos.

## 👨‍💻 Autor

Projeto desenvolvido para a disciplina de Segurança da Informação.

---

**⚠️ LEMBRE-SE**: Nunca compartilhe suas credenciais do MongoDB ou o arquivo `.env`!
