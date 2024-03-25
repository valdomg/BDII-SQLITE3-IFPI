from flask import Flask, render_template, redirect, url_for, flash
import sqlite3
from crud import verificarID

app = Flask(__name__)

#READ
@app.route("/")
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
@app.route('/addCliente')
def addCliente():
  return render_template('addCliente.html')

@app.route('/addProduto')
def addProduto():
  return render_template('addProduto.html')

@app.route('/addVenda')
def addVenda():
  return render_template('addVenda.html')

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


if __name__ == "__main__":
  app.secret_key = 'admin123' 
  app.run(debug=True)