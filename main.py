from utils.menu import main_menu, autor_menu, livros_menu, emprestimo_menu
from services.autor_service import cadastrar_autor, listar_autor, atualizar_autor, remover_autor 
from services.livro_service import atualizar_livros, cadastrar_livros, listar_livros, remover_livros
from services.emprestimo_service import realizar_emprestimo, devolver_livro, listar_emprestimos

while True:
    try:
        opcao = main_menu()

        #Livro
        if int(opcao) == 1:
            opcao_livro = livros_menu()

            if int(opcao_livro) == 1:
                listar_autor()
                titulo = input('Informe o titulo do livro: ').strip()
                id_autor = int(input('Informe o ID do autor: '))
                ano = int(input('Informe o ano do livro: '))
                categoria = input('Informe a categoria do livro: ').strip()
                quantidade = int(input('Informe a quantidade: '))
                cadastrar_livros(titulo, id_autor, ano, categoria, quantidade)
            
            elif int(opcao_livro) == 2:
                listar_livros()
            
            elif int(opcao_livro) == 3:
                listar_livros()
                id = int(input('Informe o ID do livro: '))
                titulo = input('Informe o titulo do livro: ').strip()
                ano = int(input('Informe o ano do livro: '))
                categoria = input('Informe a categoria do livro: ')
                quantidade = int(input('Informe a quantidade: '))
                atualizar_livros(id, titulo, ano, categoria, quantidade)
            
            elif int(opcao_livro) == 4:
                listar_livros()
                id = int(input('Informe o ID do livro a ser removido: '))
                remover_livros(id)

            elif int(opcao_livro) == 0:
                continue
            
            else:
                print('Inválido')

        #Autor
        elif int(opcao) == 2:
            opcao_autor = autor_menu()
            
            if int(opcao_autor) == 1:
                nome = input('Informe o nome do autor: ').strip().capitalize()
                nacionalidade = input('Informe a nacionalidade do Autor: ').strip().capitalize()
                cadastrar_autor(nome, nacionalidade)
            
            elif int(opcao_autor) == 2:
                listar_autor()
            
            elif int(opcao_autor) == 3:
                listar_autor()
                id = int(input('Informe o ID do autor: '))
                nome = input('Informe o novo nome do autor: ').strip()
                atualizar_autor(id, nome)
            
            elif int(opcao_autor) == 4:
                listar_autor()
                id = int(input('Informe o ID do autor a ser removido: '))
                remover_autor(id)
            
            elif int(opcao_autor) == 0:
                continue
            
            else:
                print('Inválido')

        # Emprestimo
        elif int(opcao) == 3:
            opcao_emprestimo = emprestimo_menu()

            if int(opcao_emprestimo) == 1:
                listar_livros()
                id_livro = int(input('Informe o ID do livro: '))
                nome = input('Informe o nome da pessoa: ').strip()
                realizar_emprestimo(id_livro, nome)

            elif int(opcao_emprestimo) == 2:
                listar_emprestimos()
                id_livro = int(input('Informe o ID do livro: '))
                nome = input('Informe o nome da pessoa: ').strip()
                devolver_livro(id_livro, nome)

            elif int(opcao_emprestimo) == 3:
                listar_emprestimos()

            elif int(opcao_emprestimo) == 0:
                continue

            else:
                print('Inválido')
        
        elif int(opcao) == 0:
            break
    
    except ValueError:
        print('Erro: digite apenas números.')