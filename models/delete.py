import sqlite3
from models.crud import verificarID
banco = sqlite3.connect('vendas.db')

#DEPENDECY INJECTION
cursor = banco.cursor()

def delRegistroVenda(id):
    banco = sqlite3.connect('vendas.db')
    cursor = banco.cursor()

    cursor.execute(f'DELETE FROM venda WHERE idvenda={id}')
    banco.commit()
    banco.close()

#Deletar algum produto
def delRegistroProduto(id):
    banco = sqlite3.connect('vendas.db')
    cursor = banco.cursor()

    cursor.execute(f'DELETE FROM produto WHERE idprod={id}')
    banco.commit()
    banco.close()
    

#Deletar algum cliente
def delRegistroCliente(id):
    banco = sqlite3.connect('vendas.db')
    cursor = banco.cursor()

    cursor.execute(f'DELETE FROM cliente WHERE idcliente={id}')
    banco.commit()
    banco.close()
