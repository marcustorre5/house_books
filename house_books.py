
#variaveis globais:
lista_livros = [] #lista de dicionario
id_global = 0

#cadastrar livros
def cadastrar_livro(id):
    print('\nHouse Books\n')
    print('id do livro: {}'.format(id))
    livro = input('Entre com o nome do livro: ')
    autor = input('Entre com o nome do autor: ')
    editora = input('Entre com o nome da editora:  ')

    #dicioario para armazenar os livros
    dicionario_livro = {'id' : id,
                        'livro' : livro,
                        'autor' : autor,
                        'editora' : editora}

    lista_livros.append(dicionario_livro.copy())

#consultar livros
def consultar_livro():
    while True:
        print('\nBem vindo ao consultar livros\n')
        print('-----Menu principal-----')
        menu_consultar = input('Escolha a opcao desejada\n'
                               '1 - Consultar todos os livros\n'
                               '2 - Consultar livro por id\n'
                               '3 - Consultar livro(s) por autor\n'
                               '4 - Consultar livro(s) por editora\n'
                               '5 - Retornar\n')

        # Opção cadastro de livros
        if menu_consultar == '1':
            print('Você selecionou a opção consultar todos os livros\n')
            for livros in lista_livros: #livros vai varrer toda a lista de livros
                print('--------------------')
                for chave, valor in livros.items(): #varrer todos os conjutos chave e valor do dicionario livros
                    print('{}: {}'.format(chave, valor))
                print('--------------------')

        # Opção consulta de livros
        elif menu_consultar == '2':
            print('Você selecionou a opção Consultar livro por id\n')
            id_selecionado = int(input('Entre com o id do livro desejado: '))
            for livros in lista_livros:
                if livros['id'] == id_selecionado: # O valor do campo id desse dicionario é igual o valor desejado
                    print('--------------------')
                    for chave, valor in livros.items():  # varrer todos os conjutos chave e valor do dicionario livros
                        print('{}: {}'.format(chave, valor))
                    print('--------------------')

        # Opção consulta de livros por autor
        elif menu_consultar == '3':
            print('Você selecionou a opção consultar livro(s) por autor\n')
            id_selecionado = str(input('Entre com o autor desejado: '))
            for livros in lista_livros:
                if livros['autor'] == id_selecionado:  # O valor do campo id desse dicionario é igual o valor desejado
                    print('--------------------')
                    for chave, valor in livros.items():  # varrer todos os co11njutos chave e valor do dicionario livros
                        print('{}: {}'.format(chave, valor))
                    print('--------------------')

        # Opção consulta de livros por editora
        elif menu_consultar == '4':
            print('Você selecionou a opção consultar livro(s) por autor\n')
            id_selecionado = str(input('Entre com o editora desejado: '))
            for livros in lista_livros:
                if livros['editora'] == id_selecionado:  # O valor do campo id desse dicionario é igual o valor desejado
                    print('--------------------')
                    for chave, valor in livros.items():  # varrer todos os conjutos chave e valor do dicionario livros
                        print('{}: {}'.format(chave, valor))
                    print('--------------------')

        # Opção retornar
        elif menu_consultar == '5':
            print('Você selecionou a opção Retornar\n')
            return #sai da função consultar

        else:
            print('opção invalida tente novamente\n')
            continue #volta pro loop

#remover livros
def remover_livro():
    print('Bem vindo ao remover livros')
    livro_dejedo = int(input('Entre com o id do livro que dejesa remover: '))
    for livros in lista_livros:
        if livros['id'] == livro_dejedo:
            lista_livros.remove(livros)
            print('Livro removido')

#inico do main
# Boas-vindas
print('Bem-Vindo sistema de livros de Marcus Vinicius de Araujo Torres\n')
while True:
    print('\n-----Menu principal-----\n')
    menu_principal = input('Escolha a opcao desejada\n'
                           '1 - Cadastrar livro\n'
                           '2 - Consultar livro\n'
                           '3 - Remover livro\n'
                           '4 - Encerrar Programa\n')

    #Opção cadastro de livros
    if menu_principal == '1':
        print('-----Menu cadastrar livro-----')
        id_global = id_global + 1
        cadastrar_livro(id_global)

    elif menu_principal == '2':
        print('-----Menu conultar livro-----')
        consultar_livro()

    elif menu_principal == '3':
        print('-----Menu remover livro-----')
        remover_livro()

    elif menu_principal == '4':
        print('-----Encerrando-----')
        break #Encerra o loop

    else:
        print('opção invalida tente novamente\n')
        continue #volta pro loop

