from database import get_conexao
import datetime

def realizar_emprestimo(id_livro, nome):
    with get_conexao() as conexao:
        cursor = conexao.cursor()

        cursor.execute("SELECT quantidade FROM livro WHERE id = ?", (id_livro,))
        livro = cursor.fetchone()

        if livro is None:
            print('Livro não encontrado.')
            return

        if livro[0] == 0:
            print('Livro indisponível.')
            return
        
        data_retirada = datetime.date.today()

        cursor.execute(
            "INSERT INTO emprestimo (id_livro, nome, data_retirada, status) VALUES (?, ?, ?, ?)",
            (id_livro, nome, data_retirada, 'ativo')
        )

        cursor.execute(
            "UPDATE livro SET quantidade = quantidade - 1 WHERE id = ?",
            (id_livro,)
        )

        print('Empréstimo realizado com sucesso!')


def devolver_livro(id_livro, nome):
    with get_conexao() as conexao:
        cursor = conexao.cursor()

        cursor.execute("SELECT quantidade FROM livro WHERE id = ?", (id_livro,))
        livro = cursor.fetchone()

        if livro is None:
            print('Livro não encontrado.')
            return
        
        data_devolucao = datetime.date.today()

        cursor.execute(
            "UPDATE emprestimo SET data_devolucao = ?, status = ? WHERE id_livro = ? AND status = 'ativo'",
            (data_devolucao, 'devolvido', id_livro)
        )

        if cursor.rowcount == 0:
            print('Nenhum empréstimo ativo encontrado para esse livro.')
            return
        
        cursor.execute(
            "UPDATE livro SET quantidade = quantidade + 1 WHERE id = ?",
            (id_livro,)
        )

        print('Devolução realizado com sucesso!')


def listar_emprestimos():
    with get_conexao() as conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT emprestimo.id, livro.titulo, emprestimo.nome, emprestimo.data_retirada, emprestimo.status
            FROM emprestimo
            LEFT JOIN livro ON emprestimo.id_livro = livro.id
            WHERE emprestimo.status = 'ativo'
        """)
        resultado = cursor.fetchall()

        if not resultado:
            print('Nenhum livro emprestado.')
            return 

        for emprestimo in resultado:
            print(f'ID: {emprestimo[0]} | Livro: {emprestimo[1]} | Nome: {emprestimo[2]} | Data Retirada: {emprestimo[3]} | Status: {emprestimo[4]}')