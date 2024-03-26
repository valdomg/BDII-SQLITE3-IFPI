from flask import Flask, render_template, redirect, url_for, flash, request
import sqlite3


app = Flask(__name__)

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



#CREATE
@app.route('/renderCad') #ROTA PARA RENDERIZAR A PÁGINA DE CADASTRO
def addCliente(): #FUNÇÃO COM NOME IGUAL A PÁGINA DE FORMULÁRIO
  return render_template ('cadCliente.html') #RENDERIZAR A PÁGINA DE CADASTRO

@app.route('/addCliente', methods=['POST']) #ROTA COM MÉTODO POST
def cadCliente(): #FUNÇÃO DE CADASTRO QUE IRÁ FUNCIONAR DENTRO DA FUNÇÃO ADDCLIENTE
  nome = request.form['nomeCliente']
  email = request.form['emailCliente']
  data = request.form['dataCliente']
  cidade = request.form['cidadeCliente']
  tel = request.form['telCliente']

  banco = sqlite3.connect('vendas.db')
  cursor = banco.cursor()

  cursor.execute('INSERT INTO cliente VALUES(?,?,?,?,?,?)',(None,nome, email, data, cidade, tel))
  banco.commit()
  banco.close()

  return redirect(url_for('home'))

@app.route('/renderProd')
def addProd():
  return render_template('cadProduto.html')

@app.route('/addProduto', methods = ['POST'])
def cadProduto():
  
  nomeProduto = request.form['nomeProduto']
  preco = request.form['preco']
  marca = request.form['marca']
  categoria = request.form['categoria']
  qtd = request.form['quantidade']

  banco = sqlite3.connect('vendas.db')
  cursor = banco.cursor()

  cursor.execute('INSERT INTO produto VALUES (?,?,?,?,?,?)', (None,nomeProduto, preco, marca, categoria, qtd))
  banco.commit()
  banco.close()

  return redirect(url_for('home'))

@app.route('/renderVenda')
def addVenda():
  return render_template('cadVenda.html')

@app.route('/addVenda', methods = ['POST'])
def cadVenda():
  banco = sqlite3.connect('vendas.db')
  cursor = banco.cursor()

  data = request.form['dataVenda']
  valor_total = request.form['valor']
  idCliente = int(request.form['idCliente'])
  idProd = request.form['idProd']
  nomeFunc = request.form['nomeFunc']

  if verificarID("idcliente", "cliente", int(idCliente)) and verificarID('idprod', 'produto', int(idProd)):
    cursor.execute('INSERT INTO venda VALUES (?,?,?,?,?,?)',(None, data, valor_total, idCliente, idProd, nomeFunc))
    banco.commit()
    banco.close()

  return redirect(url_for('home'))

#DELETE
@app.route('/delCliente/<int:id>', methods = ['GET'])
def delCliente(id):
    banco = sqlite3.connect('vendas.db')
    cursor = banco.cursor()

    cursor.execute(f'DELETE FROM cliente WHERE idcliente = {id}')
    banco.commit()
    banco.close()
    flash('DADOS DELETADOS')
    
    return redirect(url_for('home'))

@app.route('/delProduto/<int:id>', methods = ['GET'])
def delProduto(id):
  banco = sqlite3.connect('vendas.db')
  cursor = banco.cursor()

  cursor.execute(f'DELETE FROM produto WHERE idprod = {id}')
  banco.commit()
  banco.close()
  return redirect(url_for('home'))

@app.route('/delVenda/<int:id>', methods = ['GET'])
def delVenda(id):
  banco = sqlite3.connect('vendas.db')
  cursor = banco.cursor()

  cursor.execute(f'DELETE FROM venda WHERE idvenda = {id}')
  banco.commit()
  banco.close()
  return redirect(url_for('home'))


#Editar
@app.route('/editarCliente/<int:id>', methods = ['GET', 'POST'])
def editarCliente(id):
  if request.method == 'GET':
      banco = sqlite3.connect('vendas.db')
      cursor = banco.cursor()

      cursor.execute(f'SELECT * FROM cliente WHERE idCliente = {id}')
      cliente = cursor.fetchone()
      cursor.close()
      return render_template('editarCliente.html', cliente = cliente)
    
  elif request.method == 'POST':
    nome = request.form['nomeCliente']
    email = request.form['emailCliente']
    data = request.form['dataCliente']
    cidade = request.form['cidadeCliente']
    tel = request.form['telCliente']

    banco = sqlite3.connect('vendas.db')
    cursor = banco.cursor()

    cursor.execute('UPDATE cliente SET nome=?, email=?, data_nasc=?, cidade=?, telefone=? WHERE idCliente=?', (nome, email, data, cidade, tel, id))
    banco.commit()
    banco.close()

    return redirect(url_for('home'))

@app.route('/editarProduto/<int:id>', methods = ['GET', 'POST'])
def editarProduto(id):
  if request.method == 'GET':
    banco = sqlite3.connect('vendas.db')
    cursor = banco.cursor()

    cursor.execute(f'SELECT * FROM produto WHERE idprod={id}')
    produto = cursor.fetchone()
    cursor.close()

    return render_template('editarProduto.html', produto = produto)
  
  elif request.method == 'POST':
    nomeProduto = request.form['nomeProduto']
    preco = request.form['preco']
    marca = request.form['marca']
    categoria = request.form['categoria']
    qtd = request.form['quantidade']

    banco = sqlite3.connect('vendas.db')
    cursor = banco.cursor()

    cursor.execute('UPDATE produto SET nome=?, preco=?, marca=?, categoria=?, qtd=? WHERE idprod = ?',(nomeProduto, preco, marca, categoria, qtd, id))
    banco.commit()
    banco.close()
    
    return redirect(url_for('home'))

@app.route('/editarVenda/<int:id>', methods = ['GET', 'POST'])
def editarVenda(id):
  if request.method == 'GET':
    banco = sqlite3.connect('vendas.db')
    cursor = banco.cursor()

    cursor.execute(f'SELECT * FROM venda WHERE idvenda={id}')
    venda = cursor.fetchone()
    cursor.close()

    return render_template('editarVenda.html', venda = venda)
  
  elif request.method == 'POST':

    banco = sqlite3.connect('vendas.db')
    cursor = banco.cursor()

    data = request.form['dataVenda']
    valor_total = request.form['valor']
    idCliente = int(request.form['idCliente'])
    idProd = request.form['idProd']
    nomeFunc = request.form['nomeFunc']
      
    if verificarID("idcliente", "cliente", int(idCliente)) and verificarID('idprod', 'produto', int(idProd)):
      cursor.execute('UPDATE venda SET data_venda=?, valor_total=?, idcliente=?, idprod=?, nomeFunc=? WHERE idvenda = ?',(data, valor_total, idCliente, idProd, nomeFunc, id))
      banco.commit()
      banco.close()
    else:
      flash('IDS INVÁLIDOS, TENTE NOVAMENTE')
    return redirect(url_for('home'))
    
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