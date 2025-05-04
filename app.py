import os

# Lista inicial de restaurantes (poderia vir de um arquivo ou banco de dados)
restaurantes = [{'nome':'Praça','categoria':'Japonesa','ativo':False},
                {'nome':'Pizza','categoria':'Italiana','ativo':True},
                {'nome':'Feijoada','categoria':'Brasileiro','ativo':True}]

def exibir_nome_do_programa():
    """
    Exibe o nome do programa Sabor Express de forma estilizada no console.
    
    Esta função utiliza arte ASCII para criar um banner decorativo
    e exibe o nome do programa logo abaixo.
    """
    print("""
█▀▀ ▄▀█ █▀█ █▀█ █▀█ █▄█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀▀ █▀▀
█▄▄ █▀█ █▀▄ █▄█ █▀▄ ░█░   █▄▄ █░█ █▄█ █▄█ ██▄ ██▄ ▄▄█
""")
    print('Sabor Express\n')

def exibir_menu():
    """
    Exibe as opções disponíveis no menu principal do programa.
    
    Apresenta numericamente todas as funcionalidades que o usuário pode acessar.
    """
    print('Menu de opções:')
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alterar estado do restaurante') # Texto ajustado
    print('4. Sair\n')

def finalizar_app():
    """
    Exibe mensagem de finalização e prepara o encerramento do aplicativo.
    
    Returns:
        bool: True para sinalizar ao loop principal que o programa deve encerrar.
    """
    exibir_subtitulo('Finalizar app')
    print('Encerrando o programa...')
    return True # Sinaliza para o loop principal que deve terminar

def voltar_ao_menu_principal():
    """
    Pausa a execução até que o usuário pressione uma tecla.
    
    Esta função é utilizada para dar tempo ao usuário de visualizar
    as informações na tela antes de voltar ao menu principal.
    """
    input('\nDigite uma tecla para voltar ao menu principal ')
    # A função main() cuidará de limpar a tela e reexibir o menu

def exibir_subtitulo(texto):
    """
    Limpa a tela e exibe um subtítulo formatado com decoração.
    
    Args:
        texto (str): O texto a ser exibido como subtítulo.
    """
    os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela (Windows ou outros)
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(f'* {texto} *')
    print(linha)
    print() # Linha em branco para espaçamento

def cadastra_novo_restaurante():
    """
    Solicita ao usuário os dados e cadastra um novo restaurante.
    
    Pede o nome e a categoria do restaurante e o adiciona à lista de restaurantes,
    verificando antes se o nome já existe para evitar duplicações.
    O restaurante é cadastrado inicialmente como inativo.
    """
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    # Verifica se o restaurante já existe (opcional, mas boa prática)
    if any(r['nome'].lower() == nome_do_restaurante.lower() for r in restaurantes):
        print(f'O restaurante "{nome_do_restaurante}" já está cadastrado.')
    else:
        categoria_do_restaurante = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
        # Cria o dicionário com os dados do restaurante, iniciando como inativo
        dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria_do_restaurante, 'ativo': False}
        restaurantes.append(dados_do_restaurante)
        print(f'O restaurante "{nome_do_restaurante}" foi cadastrado com sucesso!')

    voltar_ao_menu_principal()

def listar_restaurantes():
    """
    Lista todos os restaurantes cadastrados com suas informações.
    
    Exibe uma tabela formatada com o nome, categoria e status (ativo/inativo)
    de cada restaurante. Caso não haja restaurantes cadastrados, exibe uma
    mensagem informativa.
    """
    exibir_subtitulo('Listando restaurantes')

    # Cabeçalho da tabela
    print(f'{"Nome do Restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status')
    print('-' * (22 + 3 + 20 + 3 + 8)) # Linha separadora

    if not restaurantes:
        print('Nenhum restaurante cadastrado.')
    else:
        for restaurante in restaurantes:
            nome_restaurante = restaurante['nome']
            categoria_restaurante = restaurante['categoria']
            # Define o texto do status baseado no valor booleano 'ativo'
            status = "Ativo" if restaurante['ativo'] else "Inativo"
            # Imprime a linha formatada
            print(f'{nome_restaurante.ljust(22)} | {categoria_restaurante.ljust(20)} | {status}')

    voltar_ao_menu_principal()

def alterar_estado_restaurante():
    """
    Altera o estado (ativo/inativo) de um restaurante existente.
    
    Solicita ao usuário o nome do restaurante que deseja alterar o estado,
    busca na lista de restaurantes e inverte seu estado atual (ativo → inativo
    ou inativo → ativo). Se o restaurante não for encontrado, exibe uma mensagem.
    """
    exibir_subtitulo('Alterar estado do restaurante') # Texto ajustado
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = None

    # Procura o restaurante na lista (ignorando maiúsculas/minúsculas)
    for restaurante in restaurantes:
        if nome_restaurante.lower() == restaurante['nome'].lower():
            restaurante_encontrado = restaurante
            break # Para o loop assim que encontrar

    if restaurante_encontrado:
        # Inverte o estado atual (True vira False, False vira True)
        estado_anterior = restaurante_encontrado['ativo']
        restaurante_encontrado['ativo'] = not estado_anterior
        novo_status = "ativado" if restaurante_encontrado['ativo'] else "desativado"
        print(f'O restaurante "{restaurante_encontrado["nome"]}" foi {novo_status} com sucesso!')
    else:
        print(f'O restaurante "{nome_restaurante}" não foi encontrado!')

    voltar_ao_menu_principal()


def escolher_opcao():
    """
    Solicita a opção do usuário e direciona para a função correspondente.

    Returns:
        bool: True se o app deve finalizar, False caso contrário.
    """
    try:
        # Lê a opção como string para evitar erro imediato se não for número
        opcao_escolhida_str = input('Escolha uma opção: ')
        opcao_escolhida = int(opcao_escolhida_str) # Tenta converter para inteiro

        print(f'Você escolheu a opção: {opcao_escolhida}\n') # Feedback para o usuário

        if opcao_escolhida == 1:
            cadastra_novo_restaurante()
            return False # Continua o loop
        elif opcao_escolhida == 2:
            listar_restaurantes()
            return False # Continua o loop
        elif opcao_escolhida == 3:
            alterar_estado_restaurante()
            return False # Continua o loop
        elif opcao_escolhida == 4:
            return finalizar_app() # Retorna True para quebrar o loop
        else:
            # Opção é um número, mas fora do intervalo válido (1-4)
            print('Opção inválida! Escolha um número entre 1 e 4.\n')
            voltar_ao_menu_principal()
            return False # Continua o loop
    except ValueError:
        # A entrada não pôde ser convertida para inteiro
        print('Opção inválida! Por favor, digite um número.\n')
        voltar_ao_menu_principal()
        return False # Continua o loop

def main():
    """
    Função principal que executa o loop do programa.
    
    Inicializa a aplicação, limpa a tela, exibe o nome do programa
    e gerencia o fluxo principal do aplicativo em um loop até que
    o usuário escolha sair.
    """
    # Limpa a tela uma vez no início e exibe o nome
    os.system('cls' if os.name == 'nt' else 'clear')
    exibir_nome_do_programa()
    # Loop principal do programa
    while True:
        exibir_menu()
        # Chama a função para escolher a opção e verifica se deve sair
        if escolher_opcao():
            break # Sai do loop while se escolher_opcao retornar True

# Garante que a função main() seja chamada apenas quando o script é executado diretamente
if __name__ == '__main__':
    main()