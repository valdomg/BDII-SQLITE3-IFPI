from flask import Flask, render_template, redirect, url_for, flash, request
import sqlite3
from crud import inserirProdutos


app = Flask(__name__)


#LEITURA DE DADOS

#READ
@app.route('/')
def home():
  banco = sqlite3 .connect('vendas.db')
  cursor = banco.cursor()

  cursor.execute('SELECT * FROM cliente')
  cliente = cursor.fetchall()

  cursor.execute('SELECT * FROM produto')
  produto = cursor.fetchall()

  cursor.execute('SELECT * FROM venda')
  venda = cursor.fetchall()

  banco.close()
  return render_template('home.html', cliente = cliente, produto = produto, venda = venda)

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

  #Conexão com o DB
  banco = sqlite3.connect('vendas.db')
  cursor = banco.cursor()

  #Execução da inserção de valores
  cursor.execute('INSERT INTO cliente VALUES(?,?,?,?,?,?)',(None,nome, email, data, cidade, tel))
  banco.commit()
  banco.close()

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

  #Conexão com o DB
  #banco = sqlite3.connect('vendas.db')
  #cursor = banco.cursor()
  #Execução da inserção de valores
  #cursor.execute('INSERT INTO produto VALUES (?,?,?,?,?,?)', (None,nomeProduto, preco, marca, categoria, qtd))
  inserirProdutos(None,nomeProduto, preco, marca, categoria, qtd)
  #banco.commit()
  #banco.close()

  #Redirecionamento para função home() que irá renderizar a página principal
  return redirect(url_for('home'))

#Função para adicionar vendas
@app.route('/addVenda', methods = ['POST'])#Rota com parâmetro POST
def cadVenda():#Nome da função que será chamada no formulário

  #Conexão com o DB
  banco = sqlite3.connect('vendas.db')
  cursor = banco.cursor()

  #Valores pegos dos inputs do formulário
  data = request.form['dataVenda']
  valor_total = request.form['valor']
  idCliente = int(request.form['idCliente'])
  idProd = request.form['idProd']
  nomeFunc = request.form['nomeFunc']

  #Lógica para verificar a existência das chaves ID de cliente e produto
  if verificarID("idcliente", "cliente", int(idCliente)) and verificarID('idprod', 'produto', int(idProd)):
    cursor.execute('INSERT INTO venda VALUES (?,?,?,?,?,?)',(None, data, valor_total, idCliente, idProd, nomeFunc))
    banco.commit()
    banco.close()

  #Redirecionamento para função home() que irá renderizar a página principal
  return redirect(url_for('home'))

#---------------------------------------------------------------------------------------------------------------------------

#EXCLUSÃO DE DADOS

#Função para exclusão de clientes
@app.route('/delCliente/<int:id>', methods = ['GET']) #Rota com método GET para pegar o ID único do Cliente
def delCliente(id): #Função com o parâmetro id que foi pego na rota
    
    #Conexão com o DB
    banco = sqlite3.connect('vendas.db')
    cursor = banco.cursor()

    #Execução da exclusão de dados
    cursor.execute(f'DELETE FROM cliente WHERE idcliente = {id}')
    banco.commit()
    banco.close()
    flash('DADOS DELETADOS')
    
    #Redirecionamento para a página home
    return redirect(url_for('home'))


#Função para exclusão de produtos
@app.route('/delProduto/<int:id>', methods = ['GET']) #Rota com método GET para pegar o ID único do Produto
def delProduto(id):#Função com o parâmetro id que foi pego na rota

  #Conexão com o DB
  banco = sqlite3.connect('vendas.db')
  cursor = banco.cursor()

  #Execução da exclusão de dados
  cursor.execute(f'DELETE FROM produto WHERE idprod = {id}')
  banco.commit()
  banco.close()

  #Redirecionamento para a página home
  return redirect(url_for('home'))

#Função para exclusão de produtos
@app.route('/delVenda/<int:id>', methods = ['GET']) #Rota com método GET para pegar o ID único da Venda
def delVenda(id):#Função com o parâmetro id que foi pego na rota

  #Conexão com o DB
  banco = sqlite3.connect('vendas.db')
  cursor = banco.cursor()

  #Execução da exclusão de dados
  cursor.execute(f'DELETE FROM venda WHERE idvenda = {id}')
  banco.commit()
  banco.close()

  #Redirecionamento para a página home
  return redirect(url_for('home'))

#-----------------------------------------------------------------------------------------------------------------------------------

#EDIÇÃO DE DADOS

#Rota para editar cliente
@app.route('/editarCliente/<int:id>', methods = ['GET', 'POST'])#Rota com método GET, POST para mostrar e alterar o valor
def editarCliente(id):#parâmetro id pego na url da rota

  #Lógica para mostrar a linha proveniente da tabela cliente com o id do cliente
  if request.method == 'GET': 
      
      #Conexão com o BD
      banco = sqlite3.connect('vendas.db')
      cursor = banco.cursor()

      #Execução para mostrar os dados
      cursor.execute(f'SELECT * FROM cliente WHERE idCliente = {id}')
      cliente = cursor.fetchone()
      cursor.close()
      return render_template('editarCliente.html', cliente = cliente)
  
  #Lógica para edição da linha do id 
  elif request.method == 'POST':
    nome = request.form['nomeCliente']
    email = request.form['emailCliente']
    data = request.form['dataCliente']
    cidade = request.form['cidadeCliente']
    tel = request.form['telCliente']

    #Conexão com o BD
    banco = sqlite3.connect('vendas.db')
    cursor = banco.cursor()

    #Execução para atualizar os dados
    cursor.execute('UPDATE cliente SET nome=?, email=?, data_nasc=?, cidade=?, telefone=? WHERE idCliente=?', (nome, email, data, cidade, tel, id))
    banco.commit()
    banco.close()

    #Redirecionamento para a página
    return redirect(url_for('home'))
  

#Rota para editar produto
@app.route('/editarProduto/<int:id>', methods = ['GET', 'POST'])#Rota com método GET, POST para mostrar e alterar o valor
def editarProduto(id): #parâmetro id pego na url da rota

  #Lógica para mostrar a linha proveniente da tabela produto com o id do produto
  if request.method == 'GET': 

    #Conexão com o BD
    banco = sqlite3.connect('vendas.db')
    cursor = banco.cursor()

    #Execução para mostrar os dados
    cursor.execute(f'SELECT * FROM produto WHERE idprod={id}')
    produto = cursor.fetchone()
    cursor.close()

    return render_template('editarProduto.html', produto = produto)
  
  elif request.method == 'POST': #Lógica para edição da linha do id 
    nomeProduto = request.form['nomeProduto']
    preco = request.form['preco']
    marca = request.form['marca']
    categoria = request.form['categoria']
    qtd = request.form['quantidade']

    #Conexão com o BD
    banco = sqlite3.connect('vendas.db')
    cursor = banco.cursor()

    #Execução para atualizar os dados
    cursor.execute('UPDATE produto SET nome=?, preco=?, marca=?, categoria=?, qtd=? WHERE idprod = ?',(nomeProduto, preco, marca, categoria, qtd, id))
    banco.commit()
    banco.close()
    
    #Redirecionamento para a página
    return redirect(url_for('home'))
  

#Rota para editar venda
@app.route('/editarVenda/<int:id>', methods = ['GET', 'POST']) #Rota com método GET, POST para mostrar e alterar o valor
def editarVenda(id): #parâmetro id pego na url da rota

  #Lógica para mostrar a linha proveniente da tabela venda com o id da venda
  if request.method == 'GET':
    banco = sqlite3.connect('vendas.db')
    cursor = banco.cursor()

    #Execução para mostrar os dados
    cursor.execute(f'SELECT * FROM venda WHERE idvenda={id}')
    venda = cursor.fetchone()
    cursor.close()

    return render_template('editarVenda.html', venda = venda)
  
  #Lógica para edição da linha do id 
  elif request.method == 'POST': 

    banco = sqlite3.connect('vendas.db')
    cursor = banco.cursor()

    data = request.form['dataVenda']
    valor_total = request.form['valor']
    idCliente = int(request.form['idCliente'])
    idProd = request.form['idProd']
    nomeFunc = request.form['nomeFunc']
    
    #Lógica para verificar a existência nos ID do formulário
    if verificarID("idcliente", "cliente", int(idCliente)) and verificarID('idprod', 'produto', int(idProd)):
      cursor.execute('UPDATE venda SET data_venda=?, valor_total=?, idcliente=?, idprod=?, nomeFunc=? WHERE idvenda = ?',(data, valor_total, idCliente, idProd, nomeFunc, id))
      banco.commit()
      banco.close()
    else:
      flash('IDS INVÁLIDOS, TENTE NOVAMENTE')

    #Redirecionamento para a página home
    return redirect(url_for('home'))



#função de verificação
def verificarID(coluna, tabela, id):
    banco = sqlite3.connect('vendas.db')
    cursor = banco.cursor()

    cursor.execute(f'SELECT {coluna} FROM {tabela}')
    lista = cursor.fetchall()
    for i in range (len(lista)):
        if id == lista[i][0]:
            return True 


if __name__ == "__main__":
  app.secret_key = 'admin123' 
  app.run(debug=True)