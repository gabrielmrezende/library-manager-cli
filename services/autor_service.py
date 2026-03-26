from database import get_conexao

def cadastrar_autor(nome, nacionalidade):
    if not nome:
        print('Erro: o nome do autor é obrigatorio')
        return
     
    with get_conexao() as conexao:
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO autor (nome, nacionalidade) VALUES (?, ?)",
            (nome, nacionalidade)
        )
        print('Cadastro de Autor realizado com sucesso!')
    

def listar_autor():
    with get_conexao() as conexao:
        cursor = conexao.cursor()
        cursor.execute(
            "SELECT * FROM autor"
        )
        
        resultado = cursor.fetchall()

        if not resultado:
            print('Nenhum autor cadastrado.')
            return 
        
        for autor in resultado:
            print(f"ID: {autor[0]} | Nome: {autor[1]} | Nacionalidade: {autor[2]}")

def atualizar_autor(id, nome):
    if not nome:
        print('Erro: o nome do autor é obrigatório')
        return
    
    with get_conexao() as conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            UPDATE autor
            SET nome = ?
            Where id = ?    
        """, (nome, id))

        if cursor.rowcount == 0:
            print('Autor não encontrado')
            return 
        
        print('Autor atualizado com sucesso!')

def remover_autor(id):
    with get_conexao() as conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            DELETE FROM autor
            WHERE id = ?
        """, (id, ))

        if cursor.rowcount == 0:
            print('Autor não encontrado')
            return 

        print('Autor removido com sucesso')

