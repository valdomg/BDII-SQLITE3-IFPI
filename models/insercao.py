import sqlite3
from models.crud import verificarID
banco = sqlite3.connect('vendas.db')

#DEPENDECY INJECTION
cursor = banco.cursor()

#Função de inserção de clientes
def inserirClientes(id,nome, data_nasc, cidade, telefone, email):
    banco = sqlite3.connect('vendas.db')
    cursor = banco.cursor()
    cursor.execute('INSERT INTO cliente VALUES(?,?,?,?,?,?)',(None,nome, email, data_nasc, cidade, telefone))
    banco.commit()
    banco.close()


#Função de inserção para produtos
def inserirProdutos(id,nome, preco, marca, categoria, qtd):
    banco = sqlite3.connect('vendas.db')
    cursor = banco.cursor()
    cursor.execute('INSERT INTO produto VALUES(?,?,?,?,?,?)',(None,nome, preco, marca, categoria, qtd))
    banco.commit()        
    banco.close()

            
#Função de inserção de vendas
def inserirVendas(idvenda,data_venda, valor_total, idcliente, idprod, nomeFunc):
    banco = sqlite3.connect('vendas.db')
    cursor = banco.cursor()
    #Lógica para verificar a existência dos IDS
    if verificarID('cliente', 'idcliente', idcliente) and verificarID('produto', 'idprod', idprod):
        cursor.execute('INSERT INTO venda VALUES (?,?,?,?,?,?)',(None, data_venda, valor_total, idcliente, idprod, nomeFunc))
        banco.commit()
    else:
        print('DADOS INVÁLIDOS, TENTE NOVAMENTE')

