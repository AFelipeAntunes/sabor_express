import os

restaurantes = ['Feijoada', 'Churrasco']

def exibir_nome_do_programa():
    print('Sabor Express\n')

def exibir_menu():
    print('Menu de opções:')
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizar app')
    print('Encerrando o programa...')
    return True

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu ')

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def cadastra_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} cadastrado com sucesso!')
    voltar_ao_menu_principal()
def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')

    for i, restaurante in enumerate(restaurantes):
        print(f'{i+1}.{restaurante}')

    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastra_novo_restaurante()
            return False
        elif opcao_escolhida == 2:
            listar_restaurantes()
            return False
        elif opcao_escolhida == 3:
            print('Ativar restaurante')
            return False
        elif opcao_escolhida == 4:
            return finalizar_app()
        else:
            return opcao_invalida()
    except ValueError:
        return opcao_invalida()
def main():
    while True:
        os.system('cls')
        exibir_nome_do_programa()
        exibir_menu()
        if escolher_opcao():
            break
        os.system('cls')
        exibir_nome_do_programa()
        exibir_menu()
        escolher_opcao()
if __name__ == '__main__':
    main()
    # Executa a função principal