from database import get_conexao

def cadastrar_livros(titulo, id_autor, ano, categoria, quantidade):
    if not titulo:
        print('Erro: o nome do livro é obrigatorio')
        return
    
    with get_conexao() as conexao:
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO livro (titulo, id_autor, ano, categoria, quantidade) VALUES (?, ?, ?, ?, ?)",
            (titulo, id_autor, ano, categoria, quantidade)
        )

        if cursor.rowcount == 0:
            print('Autor não encontrado')
            return 

        print('Livro cadastrado com sucesso!')


def listar_livros():
    with get_conexao() as conexao:
        cursor = conexao.cursor()
        cursor.execute(
            """
                SELECT livro.id, livro.titulo, autor.nome, livro.ano, livro.categoria, livro.quantidade 
                FROM livro
                LEFT JOIN autor
                ON livro.id_autor = autor.id
            """
        )

        resultado = cursor.fetchall()

        if not resultado:
            print('Nenhum livro cadastrado.')
            return 
        
        for livro in resultado:
            print(f"ID: {livro[0]} | Titulo: {livro[1]} | Autor: {livro[2]} | Ano: {livro[3]} | Categoria: {livro[4]} | Quantidade: {livro[5]}")


def atualizar_livros(id, titulo, ano, categoria, quantidade):
    if not titulo:
        print('ERRO: o nome do livro é obrigatório')
        return 
    
    with get_conexao() as conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            UPDATE livro
            SET titulo = ?,
                ano = ?,
                categoria = ?,
                quantidade = ?
            WHERE id = ?
        """, (titulo, ano, categoria, quantidade, id))

        if cursor.rowcount == 0:
            print('Livro não encontrado')
            return 
        
        print('Livro atualizado com sucesso!')


def remover_livros(id):
    with get_conexao() as conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            DELETE FROM livro
            WHERE id = ?
        """, (id, ))

        if cursor.rowcount == 0:
            print('Livro não encontrado')
            return
        
        print('Livro removido com sucesso!')
        
