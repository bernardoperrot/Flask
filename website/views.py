from flask import Blueprint, render_template, send_file
from flask_login import login_required, current_user
import pandas as pd
from .models import *

views = Blueprint('views',__name__)

#HOME
@views.route('/')
@login_required
def home():
    df = pd.read_excel('./tabela.xlsx', header=None, names=['nome', 'idade'])
    for index, row in df.iterrows():
        pessoas = Pessoas(nome=row['nome'], idade=row['idade'], usuario_id = current_user.id)
        db.session.add(pessoas)
    db.session.commit()
    return render_template("home.html", usuario=current_user)


@views.route('/exportar')
@login_required
def exportar_para_excel():
    # Consulta todos os registros da tabela `Pessoas` para o usuário atual
    pessoas = Pessoas.query.filter_by(usuario_id=current_user.id).all()
    
    # Criar uma lista de dicionários contendo os dados das pessoas
    dados = []
    for pessoa in pessoas:
        dados.append({
            'nome': pessoa.nome,
            'idade': pessoa.idade
        })
    
    # Converter a lista de dicionários em um DataFrame do pandas
    df = pd.DataFrame(dados)

    # Exportar o DataFrame para um arquivo Excel
    caminho_arquivo = './pessoas.xlsx'
    df.to_excel(caminho_arquivo, index=False)  # Salva o arquivo sem a coluna de índices
    
    # Enviar o arquivo Excel como resposta para download
    return send_file(caminho_arquivo, as_attachment=True)
