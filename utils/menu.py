def main_menu():
    print("\n===== BIBLIOTECA =====")
    print("1 - Gerenciar Livros")
    print("2 - Gerenciar Autores")
    print("3 - Gerenciar Empréstimos")
    print("0 - Sair")

    return input("Escolha uma opção: ")

def livros_menu():
    print("\n===== GERENCIA DE LIVROS =====")
    print('1 - Adicionar livro')
    print('2 - Listar livros')
    print('3 - Atualizar livro')
    print('4 - Remover Livro')
    print('0 - Voltar')

    return input("Escolha uma opção: ")

def autor_menu():
    print("\n===== GERENCIA DE AUTORES =====")
    print('1 - Cadastrar Autor')
    print('2 - Listar Autores')
    print('3 - Atualizar Autor')
    print('4 - Remover Autor')
    print('0 - Voltar')


    return input("Escolha uma opção: ")

def emprestimo_menu():
    print("\n===== GERENCIA DE EMPRESTIMOS =====")
    print('1 - Pegar Livro')
    print('2 - Devolver Livro')
    print('3 - Listar Livros')
    print('0 - Voltar')


    return input("Escolha uma opção: ") 