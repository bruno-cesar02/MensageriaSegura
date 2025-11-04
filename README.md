**Bruno César      RA: 24795502** 

**Juliano Perusso  RA: 24023434**

**Nicolas Nogueira RA: 24801664**

**Otávio Marquez   RA: 24025832**




## 🔐 MensageriaSegura

> Sistema de mensageria com criptografia ponta-a-ponta desenvolvido em Python

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-green.svg)
![License](https://img.shields.io/badge/License-Academic-yellow.svg)

---

## 📋 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Funcionalidades](#-funcionalidades)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Pré-requisitos](#-pré-requisitos)
- [Instalação](#-instalação)
- [Configuração](#-configuração)
- [Como Usar](#-como-usar)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Segurança](#-segurança)
- [Exemplos de Uso](#-exemplos-de-uso)
- [Erros que podem acontecer](#-erros-que-podem-acontecer)
- [Contribuindo](#-contribuindo)

---

## 🎯 Sobre o Projeto

O **MensageriaSegura** é um sistema de comunicação que implementa criptografia ponta-a-ponta, garantindo que apenas o remetente e o destinatário possam ler as mensagens trocadas. Desenvolvido como projeto acadêmico para a disciplina de Banco de Dados 2.

### 🔑 Características Principais

- **Criptografia AES (Fernet)**: Mensagens protegidas por algoritmo de criptografia simétrica
- **Autenticação Segura**: Senhas armazenadas com hash bcrypt
- **Persistência de Dados**: MongoDB Atlas para armazenamento na nuvem

---

## ✨ Funcionalidades

### Para Usuários

- ✅ Cadastro e autenticação de usuários
- ✅ Envio de mensagens criptografadas
- ✅ Leitura de mensagens com descriptografia
- ✅ Marcação automática de mensagens lidas
- ✅ Validação de destinatários

### Segurança

- 🔒 Criptografia AES-128 (Fernet)
- 🔒 Hash de senhas com bcrypt
- 🔒 Mensagens armazenadas criptografadas
- 🔒 Chave de criptografia definida pelo usuário
- 🔒 Senha oculta durante digitação (getpass)

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Versão | Uso |
|------------|--------|-----|
| **Python** | 3.8+ | Linguagem principal |
| **MongoDB Atlas** | Latest | Banco de dados na nuvem |
| **PyMongo** | Latest | Driver MongoDB para Python |
| **Cryptography** | Latest | Biblioteca de criptografia |
| **Bcrypt** | Latest | Hash de senhas |

---

## 📦 Pré-requisitos

Antes de começar, você precisa ter instalado:

- [Python 3.8+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- Conta no [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) (grátis)
- Terminal/CMD

### Verificando Instalações

```bash
python --version   # Deve mostrar Python 3.8 ou superior
pip --version      # Deve mostrar a versão do pip
```

---

## 🚀 Instalação

### 1. Clone o Repositório

```bash
git clone https://github.com/seu-usuario/MensageriaSegura.git
cd MensageriaSegura
```

### 2. Instale as Dependências

```bash
pip install -r requirements.txt
```

**Pacotes instalados:**
- `pymongo` - Conexão com MongoDB
- `cryptography` - Operações de criptografia
- `bcrypt` - Hash de senhas

---

## ⚙️ Configuração

### 1. Configurar MongoDB Atlas

1. Acesse [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
2. Crie um cluster gratuito
3. Configure acesso de rede (IP 0.0.0.0/0 para desenvolvimento)
4. Crie um usuário do banco de dados
5. Copie a string de conexão

### 2. Configurar o Projeto

Abra o arquivo `config.py` e cole sua string de conexão:

```python
# config.py

MONGO_CONNECTION_STRING = "mongodb+srv://USUARIO:SENHA@cluster.mongodb.net/..."
DATABASE_NAME = "chat"
MIN_MESSAGE_LENGTH = 50
```

**⚠️ IMPORTANTE:** Nunca compartilhe sua string de conexão publicamente!

### 3. Criar Usuários Iniciais (Opcional)

```bash
python bancoDeDados.py
```

Isso criará dois usuários de teste:
- **@alice** (senha: senha123)
- **@bob** (senha: senha456)

---

## 💻 Como Usar

### Iniciar o Sistema

```bash
python main.py
```

### Fluxo de Uso

#### 1️⃣ **Login**
```
Digite seu nome de usuário (ex: @alice): @alice
Digite sua senha:

Autenticação bem-sucedida! Bem-vindo, @alice.
```

#### 2️⃣ **Menu Principal**
```
------------------------------------------------------------
MENU PRINCIPAL
------------------------------------------------------------
1 - Enviar mensagem
2 - Ler mensagens
0 - Sair
------------------------------------------------------------
```

#### 3️⃣ **Enviar Mensagem**
1. Escolha a opção `1`
2. Digite o **@destinatário**
3. Escreva a mensagem (mínimo 50 caracteres)
4. Defina uma **chave de criptografia**
5. ✅ Mensagem enviada e criptografada!


#### 4️⃣ **Ler Mensagens**
1. Escolha a opção `2`
2. Digite a **chave de criptografia** usada pelo remetente
3. 📬 Mensagens decifradas aparecerão na tela
4. ✅ Mensagens marcadas como lidas automaticamente

---

## 📁 Estrutura do Projeto

```
MensageriaSegura/
│
├── 📄 config.py              # Configurações centralizadas
├── 📄 bancoDeDados.py        # Gerenciamento do MongoDB
├── 📄 criptografia.py        # Operações de criptografia
├── 📄 usuario.py             # Autenticação de usuários
├── 📄 envioMensagens.py      # Lógica de envio
├── 📄 recebeMensagens.py     # Lógica de recebimento
├── 📄 main.py                # Ponto de entrada do sistema
├── 📄 requirements.txt       # Dependências do projeto
└── 📄 README.md              # Este arquivo
```

### Descrição dos Módulos

| Arquivo | Responsabilidade |
|---------|------------------|
| `config.py` | Armazena configurações (string de conexão, parâmetros) |
| `bancoDeDados.py` | Gerencia conexão e operações com MongoDB |
| `criptografia.py` | Implementa cifra e decifra de mensagens (Fernet/AES) |
| `usuario.py` | Autentica usuários com bcrypt |
| `envioMensagens.py` | Envia mensagens criptografadas |
| `recebeMensagens.py` | Lê e decifra mensagens recebidas |
| `main.py` | Interface principal e menu do sistema |

---

## 🔒 Segurança

### Como Funciona a Criptografia

1. **Envio de Mensagem:**
   ```
   Texto Claro → [Fernet + Chave] → Texto Cifrado → MongoDB
   ```

2. **Leitura de Mensagem:**
   ```
   MongoDB → Texto Cifrado → [Fernet + Chave] → Texto Claro
   ```

### Algoritmos Utilizados

- **Fernet (AES-128 CBC)**: Criptografia simétrica das mensagens
- **PBKDF2**: Derivação de chave a partir da senha do usuário
- **SHA-256**: Hash usado na derivação de chave
- **Bcrypt**: Hash das senhas de usuários (custo 12)

### Boas Práticas Implementadas

✅ Senhas nunca armazenadas em texto plano  
✅ Chaves de criptografia não armazenadas no banco  
✅ Salt na derivação de chaves (PBKDF2)  
✅ 100.000 iterações no PBKDF2  
✅ Validação de entrada de usuários  

### Limitações Conhecidas

⚠️ **Salt estático**: Em produção, use salt único por mensagem  
⚠️ **Chave simétrica**: Requer compartilhamento prévio da chave  
⚠️ **Metadados visíveis**: Remetente e destinatário não são criptografados  

---

## 📸 Exemplos de Uso

### Exemplo 1: Enviando uma Mensagem

```
Escolha uma opcao: 1

Digite @destinatario: @bob
Digite a mensagem (mínimo 50 caracteres): Esta é uma mensagem 
super secreta que precisa ter no mínimo cinquenta caracteres!
Digite a chave de criptografia (não será armazenada): minhaChave123

Mensagem enviada e armazenada de forma criptografada!
```

### Exemplo 2: Lendo Mensagens

```
Escolha uma opcao: 2

Encontradas 2 mensagem(ns) não lida(s).
Digite a CHAVE/SENHA para decifrar: minhaChave123

--- Mensagens ---

[2024-11-04 14:30:25] De @alice  (id: 507f1f77bcf86cd799439011)
Mensagem:
Esta é uma mensagem super secreta que precisa ter no 
mínimo cinquenta caracteres!

✓ Marcadas como 'lida' 2 mensagem(ns) decifrada(s).
```

### Exemplo 3: Chave Incorreta

```
Digite a CHAVE/SENHA para decifrar: chaveErrada

[2024-11-04 14:30:25] De @alice  (id: 507f1f77bcf86cd799439011)
Não foi possível decifrar (chave incorreta?).

Nenhuma mensagem foi decifrada; nada marcado como lida.
```

---

## 🔧 Erros que podem acontecer

### Problema: Erro ao Conectar ao MongoDB

**Sintoma:**
```
Não foi possível conectar ao MongoDB: [Errno 11001] getaddrinfo failed
```

**Solução:**
1. Verifique sua conexão com a internet
2. Confirme se a string de conexão está correta no `config.py`
3. Verifique se seu IP está na whitelist do MongoDB Atlas
4. Tente adicionar `0.0.0.0/0` nas configurações de Network Access

---

### Problema: Módulo não Encontrado

**Sintoma:**
```
ModuleNotFoundError: No module named 'pymongo'
```

**Solução:**
```bash
pip install -r requirements.txt
```
---

### Problema: Mensagem Muito Curta

**Sintoma:**
```
Mensagem muito curta. Digite pelo menos 50 caracteres.
```

**Solução:**
Escreva uma mensagem com no mínimo 50 caracteres. Você pode alterar esse valor em `config.py`:
```python
MIN_MESSAGE_LENGTH = 30  # Reduzir para 30 caracteres
```

---

## 🧪 Testando o Sistema

Cada módulo pode ser testado individualmente:

### Testar Conexão com Banco
```bash
python bancoDeDados.py
```

### Testar Criptografia
```bash
python criptografia.py
```

### Testar Autenticação
```bash
python usuario.py
```

---

## 🎓 Conceitos Aprendidos

Este projeto demonstra:

- ✅ **Criptografia Simétrica** (AES via Fernet)
- ✅ **Hash de Senhas** (Bcrypt)
- ✅ **Derivação de Chaves** (PBKDF2)
- ✅ **NoSQL** (MongoDB)
- ✅ **Arquitetura de Software** (Separação de responsabilidades)
- ✅ **Boas Práticas** (Validação, tratamento de erros)

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

---

## 📝 Licença

Este projeto é desenvolvido para fins **acadêmicos** e **educacionais**.

---
## 📚 Referências

- [Documentação Cryptography](https://cryptography.io/)
- [MongoDB Python Driver](https://pymongo.readthedocs.io/)
- [Bcrypt Documentation](https://github.com/pyca/bcrypt/)
- [OWASP - Cryptographic Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)

---

<div align="center">

**🔐 Desenvolvido com segurança em mente**

⭐ Se este projeto foi útil, considere dar uma estrela!

</div>
