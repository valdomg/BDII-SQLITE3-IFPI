import sqlite3

banco = sqlite3.connect('vendas.db')

#Mostrar tabelas
def mostrarTabelaCliente():
    banco = sqlite3.connect('vendas.db')
    cursor = banco.cursor()
    cursor.execute('SELECT * FROM cliente')
    cliente = cursor.fetchall()
    cursor.close()
    return cliente

def mostrarTabelaProduto():
    banco = sqlite3.connect('vendas.db')
    cursor = banco.cursor()
    cursor.execute('SELECT * FROM produto')
    cliente = cursor.fetchall()
    cursor.close()
    return cliente

def mostrarTabelaVenda():
    banco = sqlite3.connect('vendas.db')
    cursor = banco.cursor()
    cursor.execute('SELECT * FROM venda')
    venda = cursor.fetchall()
    cursor.close()
    return venda

def mostrarCliente(id):
    banco = sqlite3.connect('vendas.db')
    cursor = banco.cursor()
    cursor.execute(f'SELECT * FROM cliente WHERE idcliente = {id}')
    cliente = cursor.fetchone()
    cursor.close()
    return cliente
    
def mostrarProduto(id):
    banco = sqlite3.connect('vendas.db')
    cursor = banco.cursor()
    cursor.execute(f'SELECT * FROM produto WHERE idprod = {id}')
    produto = cursor.fetchone()
    cursor.close()
    return produto

def mostrarVenda(id):
    banco = sqlite3.connect('vendas.db')
    cursor = banco.cursor()
    cursor.execute(f'SELECT * FROM venda WHERE idvenda = {id}')
    venda = cursor.fetchone()
    cursor.close()
    return venda