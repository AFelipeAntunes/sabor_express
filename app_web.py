from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import json
import os

app = Flask(__name__)
app.secret_key = 'sabor_express_secret'  # Chave necessária para sessões e flash messages

# Definindo o caminho para o arquivo de dados
DADOS_FILE = 'restaurantes.json'

# Função para carregar os restaurantes do arquivo JSON
def carregar_restaurantes():
    """
    Carrega os dados dos restaurantes do arquivo JSON ou cria dados iniciais
    se o arquivo não existir.
    
    Returns:
        list: Lista de dicionários contendo os dados dos restaurantes
    """
    if os.path.exists(DADOS_FILE):
        with open(DADOS_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)
    else:
        # Dados iniciais se o arquivo não existir
        restaurantes_iniciais = [
            {'nome':'Praça','categoria':'Japonesa','ativo':False},
            {'nome':'Pizza','categoria':'Italiana','ativo':True},
            {'nome':'Feijoada','categoria':'Brasileiro','ativo':True}
        ]
        with open(DADOS_FILE, 'w', encoding='utf-8') as file:
            json.dump(restaurantes_iniciais, file, ensure_ascii=False, indent=4)
        return restaurantes_iniciais

# Função para salvar os restaurantes no arquivo JSON
def salvar_restaurantes(restaurantes):
    """
    Salva a lista de restaurantes no arquivo JSON.
    
    Args:
        restaurantes (list): Lista de dicionários contendo os dados dos restaurantes
    """
    with open(DADOS_FILE, 'w', encoding='utf-8') as file:
        json.dump(restaurantes, file, ensure_ascii=False, indent=4)

# Rota principal - Lista de restaurantes
@app.route('/')
def index():
    """
    Exibe a página principal com a lista de restaurantes.
    """
    restaurantes = carregar_restaurantes()
    return render_template('index.html', restaurantes=restaurantes)

# Rota para cadastrar novo restaurante
@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    """
    Processa o formulário de cadastro de um novo restaurante.
    
    GET: Exibe o formulário de cadastro
    POST: Processa os dados do formulário e cadastra um novo restaurante
    """
    if request.method == 'POST':
        nome = request.form['nome']
        categoria = request.form['categoria']
        
        restaurantes = carregar_restaurantes()
        
        # Verificar se já existe um restaurante com este nome
        if any(r['nome'].lower() == nome.lower() for r in restaurantes):
            flash(f'O restaurante "{nome}" já está cadastrado.', 'danger')
        else:
            novo_restaurante = {
                'nome': nome,
                'categoria': categoria,
                'ativo': False  # Inicialmente inativo
            }
            restaurantes.append(novo_restaurante)
            salvar_restaurantes(restaurantes)
            flash(f'Restaurante "{nome}" cadastrado com sucesso!', 'success')
        
        return redirect(url_for('index'))
    
    return render_template('cadastrar.html')

# Rota para alterar o estado de um restaurante
@app.route('/alterar_estado/<nome_restaurante>')
def alterar_estado(nome_restaurante):
    """
    Altera o estado (ativo/inativo) de um restaurante existente.
    
    Args:
        nome_restaurante (str): Nome do restaurante a ter o estado alterado
    """
    restaurantes = carregar_restaurantes()
    encontrado = False
    
    for restaurante in restaurantes:
        if restaurante['nome'].lower() == nome_restaurante.lower():
            restaurante['ativo'] = not restaurante['ativo']
            novo_status = "ativado" if restaurante['ativo'] else "desativado"
            flash(f'O restaurante "{restaurante["nome"]}" foi {novo_status} com sucesso!', 'success')
            salvar_restaurantes(restaurantes)
            encontrado = True
            break
    
    if not encontrado:
        flash(f'O restaurante "{nome_restaurante}" não foi encontrado!', 'danger')
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)