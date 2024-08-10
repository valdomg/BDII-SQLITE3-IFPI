from flask import Flask, render_template, redirect, url_for, flash, request
import sqlite3

from models.crud import verificarID
from models.show import mostrarTabelaVenda, mostrarTabelaCliente, mostrarTabelaProduto
from models.show import mostrarCliente, mostrarProduto, mostrarVenda
from models.insercao import inserirClientes, inserirProdutos, inserirVendas
from models.delete import delRegistroCliente, delRegistroProduto, delRegistroVenda
from models.edit import updateCliente, updateProduto, updateVenda

app = Flask(__name__)


#LEITURA DE DADOS

#READ
@app.route('/')
def home():
 
  #Chamada das funções dentro de models
  cliente = mostrarTabelaCliente()
  produto = mostrarTabelaProduto()
  venda = mostrarTabelaVenda()
  
  return render_template('home.html', cliente = cliente, produto = produto, venda=venda)

#-----------------------------------------------------------------------------------------------------------------------

'''Parte apenas para lembrar como fazer quando necessito usar outra página para formulário, desconsidere
CREATE
@app.route('/renderCad') #ROTA PARA RENDERIZAR A PÁGINA DE CADASTRO
def addCliente(): #FUNÇÃO COM NOME IGUAL A URL(ROTA) DA PÁGINA DE FORMULÁRIO
  return render_template ('cadCliente.html') #RENDERIZAR A PÁGINA DE CADASTRO
'''

#CRIAÇÃO DE DADOS 

#Função para adicionar Clientes
@app.route('/addCliente', methods=['POST']) #ROTA COM MÉTODO POST
def cadCliente(): #FUNÇÃO DE CADASTRO QUE IRÁ FUNCIONAR DENTRO DA FUNÇÃO ADDCLIENTE

  #Valores pegos dos inputs do formulário
  nome = request.form['nomeCliente']
  email = request.form['emailCliente']
  data = request.form['dataCliente']
  cidade = request.form['cidadeCliente']
  tel = request.form['telCliente']

  inserirClientes(None,nome, data, cidade, tel, email)

  #Redirecionamento para função home() que irá renderizar a página principal
  return redirect(url_for('home'))


#Função para Adicionar Produtos
@app.route('/addProduto', methods = ['POST'])#Rota com método POST
def cadProduto(): #Nome da função que será chamada no formulário
  
  #Valores pegos dos inputs do formulário
  nomeProduto = request.form['nomeProduto']
  preco = request.form['preco']
  marca = request.form['marca']
  categoria = request.form['categoria']
  qtd = request.form['quantidade']

  inserirProdutos(None,nomeProduto, preco, marca, categoria, qtd)

  #Redirecionamento para função home() que irá renderizar a página principal
  return redirect(url_for('home'))

#Função para adicionar vendas
@app.route('/addVenda', methods = ['POST'])#Rota com parâmetro POST
def cadVenda():#Nome da função que será chamada no formulário

  #Conexão com o DB

  #Valores pegos dos inputs do formulário
  data = request.form['dataVenda']
  valor_total = request.form['valor']
  idCliente = int(request.form['idCliente'])
  idProd = int(request.form['idProd'])
  nomeFunc = request.form['nomeFunc']

  
  inserirVendas(None, data, valor_total, idCliente, idProd, nomeFunc)

  #Redirecionamento para função home() que irá renderizar a página principal
  return redirect(url_for('home'))

#---------------------------------------------------------------------------------------------------------------------------

#EXCLUSÃO DE DADOS

#Função para exclusão de clientes
@app.route('/delCliente/<int:id>', methods = ['GET']) #Rota com método GET para pegar o ID único do Cliente
def delCliente(id): #Função com o parâmetro id que foi pego na rota
    

    #Execução da exclusão de dados
    delRegistroCliente(id)
    
    #Redirecionamento para a página home
    return redirect(url_for('home'))


#Função para exclusão de produtos
@app.route('/delProduto/<int:id>', methods = ['GET']) #Rota com método GET para pegar o ID único do Produto
def delProduto(id):#Função com o parâmetro id que foi pego na rota


  #Execução da exclusão de dados
  delRegistroProduto(id)

  #Redirecionamento para a página home
  return redirect(url_for('home'))

#Função para exclusão de produtos
@app.route('/delVenda/<int:id>', methods = ['GET']) #Rota com método GET para pegar o ID único da Venda
def delVenda(id):#Função com o parâmetro id que foi pego na rota

  #Execução da exclusão de dados
  delRegistroVenda(id)

  #Redirecionamento para a página home
  return redirect(url_for('home'))

#-----------------------------------------------------------------------------------------------------------------------------------

#EDIÇÃO DE DADOS

#Rota para editar cliente
@app.route('/editarCliente/<int:id>', methods = ['GET', 'POST'])#Rota com método GET, POST para mostrar e alterar o valor
def editarCliente(id):#parâmetro id pego na url da rota

  #Lógica para mostrar a linha proveniente da tabela cliente com o id do cliente
  if request.method == 'GET': 
      
      #Execução para mostrar os dados
      cliente = mostrarCliente(id)
      return render_template('editarCliente.html', cliente = cliente)
  
  #Lógica para edição da linha do id 
  elif request.method == 'POST':
    nome = request.form['nomeCliente']
    email = request.form['emailCliente']
    data = request.form['dataCliente']
    cidade = request.form['cidadeCliente']
    tel = request.form['telCliente']

    updateCliente(id,nome, email, data, cidade,tel)

    #Redirecionamento para a página
    return redirect(url_for('home'))
  

#Rota para editar produto
@app.route('/editarProduto/<int:id>', methods = ['GET', 'POST'])#Rota com método GET, POST para mostrar e alterar o valor
def editarProduto(id): #parâmetro id pego na url da rota

  #Lógica para mostrar a linha proveniente da tabela produto com o id do produto
  if request.method == 'GET': 

    #Execução para mostrar os dados
    produto = mostrarProduto(id)

    return render_template('editarProduto.html', produto = produto)
  
  elif request.method == 'POST': #Lógica para edição da linha do id 
    nomeProduto = request.form['nomeProduto']
    preco = request.form['preco']
    marca = request.form['marca']
    categoria = request.form['categoria']
    qtd = request.form['quantidade']

    #Conexão com o BD

    #Execução para atualizar os dados
    updateProduto(id, nomeProduto, preco, marca, categoria, qtd)
    
    #Redirecionamento para a página
    return redirect(url_for('home'))
  

#Rota para editar venda
@app.route('/editarVenda/<int:id>', methods = ['GET', 'POST']) #Rota com método GET, POST para mostrar e alterar o valor
def editarVenda(id): #parâmetro id pego na url da rota

  #Lógica para mostrar a linha proveniente da tabela venda com o id da venda
  if request.method == 'GET':

    #Execução para mostrar os dados
    venda = mostrarVenda(id)

    return render_template('editarVenda.html', venda = venda)
  
  #Lógica para edição da linha do id 
  elif request.method == 'POST': 

    data = request.form['dataVenda']
    valor_total = request.form['valor']
    idCliente = int(request.form['idCliente'])
    idProd = int(request.form['idProd'])
    nomeFunc = request.form['nomeFunc']
    
    #Lógica para verificar a existência nos ID do formulário
    if verificarID("cliente", "idcliente", int(idCliente)) and verificarID('produto', 'idprod', int(idProd)):
      updateVenda(id, data, valor_total, idCliente, idProd, nomeFunc)

    #Redirecionamento para a página home
    return redirect(url_for('home'))



#função de verificação
'''
def verificarID(coluna, tabela, id):
      banco = sqlite3.connect('vendas.db')
      cursor = banco.cursor()

      cursor.execute(f'SELECT {coluna} FROM {tabela}')
      lista = cursor.fetchall()
      for i in range (len(lista)):
          if id == lista[i][0]:
              return True 
'''

if __name__ == "__main__":
  app.secret_key = 'admin123' 
  app.run(debug=True)