import sqlite3

banco = sqlite3.connect('vendas.db')

def updateCliente(id, nome, email, data, cidade, tel):
    banco = sqlite3.connect('vendas.db')
    cursor = banco.cursor()
    cursor.execute(f'''UPDATE cliente SET nome='{nome}', email='{email}', data_nasc='{data}', cidade='{cidade}', telefone={tel} WHERE idcliente={id}''')
    banco.commit()
    banco.close()

def updateProduto(id, nome, preco, marca, categoria, qtd):
    banco = sqlite3.connect('vendas.db')
    cursor = banco.cursor()
    cursor.execute(f'''UPDATE produto SET nome='{nome}', preco='{preco}', marca='{marca}', categoria='{categoria}', qtd={qtd} WHERE idprod={id}''')
    banco.commit()
    banco.close()

def updateVenda(idvenda, data_venda, valor_total, idcliente, idprod, nomeFunc):
    banco = sqlite3.connect('vendas.db')
    cursor = banco.cursor()
    cursor.execute(f'''UPDATE venda SET data_venda='{data_venda}', valor_total='{valor_total}', idcliente='{idcliente}', idprod='{idprod}', nomeFunc='{nomeFunc}' WHERE idvenda={idvenda}''')
    banco.commit()
    banco.close()