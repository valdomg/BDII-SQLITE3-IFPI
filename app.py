from flask import Flask, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

banco = None
cursor = None

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

  return render_template('home.html', cliente = cliente, produto = produto, venda = venda)


if __name__ == "__main__":
  app.run()