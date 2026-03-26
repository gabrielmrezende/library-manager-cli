import sqlite3

# Conexão
if __name__ == '__main__':
    with sqlite3.connect('biblioteca.db') as conexao:

        # Fazer conexão
        cursor = conexao.cursor()

        print("Banco de dados criado com sucesso!")


        # 2. Criar tabela
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS autor (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                nacionalidade TEXT
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS livro (
                id INTEGER PRIMARY KEY AUTOINCREMENT,   
                titulo TEXT,
                id_autor INTEGER,
                ano INTEGER,
                categoria TEXT,
                quantidade INTEGER,
                -- Definição de Chave Estrangeira
                FOREIGN KEY (id_autor) REFERENCES autor(id)
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS emprestimo(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_livro INTEGER,
                nome TEXT,
                data_retirada DATE,
                data_devolucao DATE,
                status TEXT,
                FOREIGN KEY (id_livro) REFERENCES livro(id)        
            )
        ''')

def get_conexao():
    return sqlite3.connect('biblioteca.db')
