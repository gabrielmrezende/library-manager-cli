# 📚 Library CLI System

Sistema de gerenciamento de biblioteca desenvolvido em **Python**, executado diretamente no terminal (CLI - Command Line Interface).

Este projeto implementa operações **CRUD completas** para gerenciamento de livros, autores e empréstimos, com persistência de dados em banco **SQLite**.

---

## 🚀 Funcionalidades

### 📖 Livros
- Cadastrar livro vinculado a um autor
- Listar todos os livros com nome do autor
- Atualizar informações do livro
- Remover livro

### ✍️ Autores
- Cadastrar autor
- Listar todos os autores
- Atualizar autor
- Remover autor

### 🔄 Empréstimos
- Registrar empréstimo com controle de disponibilidade
- Devolver livro com atualização automática de estoque
- Listar empréstimos ativos

---

## 🧠 Tecnologias utilizadas

- Python 3
- SQLite3 (banco de dados embutido)

---

## 📂 Estrutura do Projeto
```
library-cli/
│
├── main.py               # Ponto de entrada e navegação do sistema
├── database.py           # Conexão e criação das tabelas
├── models.py             # Classes de modelo (Livro, Autor, Emprestimo)
├── services/
│   ├── __init__.py
│   ├── livro_service.py       # CRUD de livros
│   ├── autor_service.py       # CRUD de autores
│   └── emprestimo_service.py  # Lógica de empréstimos
│
└── utils/
    ├── __init__.py
    └── menu.py           # Menus do terminal
```

---

## ⚙️ Como executar

Clone o repositório:
```bash
git clone https://github.com/seuusuario/library-cli.git
```

Entre na pasta:
```bash
cd library-cli
```

Crie o banco de dados:
```bash
python database.py
```

Execute o sistema:
```bash
python main.py
```

---

## 🖥️ Exemplo de uso
```
===== LIBRARY MANAGER =====
1 - Gerenciar Livros
2 - Gerenciar Autores
3 - Gerenciar Empréstimos
0 - Sair

Escolha uma opção:
```

---

## 🗄️ Banco de Dados

O sistema utiliza SQLite com três tabelas:

- **autor** — id, nome, nacionalidade
- **livro** — id, titulo, id_autor (FK), ano, categoria, quantidade
- **emprestimo** — id, id_livro (FK), nome, data_retirada, data_devolucao, status

---

## 📌 Melhorias futuras

- Interface gráfica (Tkinter ou Web)
- API REST com Flask
- Sistema de autenticação de usuários
- Relatórios e estatísticas de empréstimos
- Exportação de dados (CSV/JSON)

---

## 👨‍💻 Autor

Projeto desenvolvido para prática de Python e construção de portfólio.