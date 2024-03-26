
import sqlite3

banco = sqlite3.connect('vendas.db')

    #DEPENDECY INJECTION
cursor = banco.cursor()

def criarTabelas():#CREATING DB
    banco = sqlite3.connect('vendas.db')

    #DEPENDECY INJECTION
    cursor = banco.cursor()

    #tabela cliente
    cursor.execute('''CREATE TABLE IF NOT EXISTS cliente (
                        idcliente INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        email TEXT,
                        data_nasc DATE,
                        cidade TEXT,
                        telefone TEXT
                )''')


    #tabela produto
    cursor.execute('''CREATE TABLE IF NOT EXISTS produto(
                        idprod INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        preco REAL NOT NULL,
                        marca TEXT NOT NULL,
                        categoria TEXT NOT NULL,
                        qtd INTEGER NOT NULL
                )''')


    #tabela venda
    cursor.execute('''CREATE TABLE IF NOT EXISTS venda(
                idvenda INTEGER PRIMARY KEY AUTOINCREMENT,
                data_venda DATE NOT NULL,
                valor_total REAL NOT NULL,
                idcliente INTEGER,
                idprod INTEGER,
                nomeFunc TEXT,
                FOREIGN KEY (idcliente) references cliente(idcliente),
                FOREIGN KEY (idprod) references produto(idprod)
    )''')

def dropTables():
    banco = sqlite3.connect('vendas.db')
    cursor = banco.cursor()
    cursor.execute('DROP TABLE cliente')
    cursor.execute('DROP TABLE produto')
    cursor.execute('DROP TABLE venda')


#Função para verificar se existe o ID na tabela
def verificarID(tabela, coluna, id):
    banco = sqlite3.connect('vendas.db')
    cursor = banco.cursor()

    resultado = None

    cursor.execute(f'SELECT {coluna} FROM {tabela}')
    lista = cursor.fetchall()
    for i in range (len(lista)):
        if id == lista[i][0]:
            resultado = True

    return resultado


#Função de inserção para Clientes
def inserirClientes(id,nome, data_nasc, cidade, telefone, email):
    banco = sqlite3.connect('vendas.db')
    cursor = banco.cursor()
    cursor.execute('INSERT INTO cliente VALUES(?,?,?,?,?,?)',(None,nome, data_nasc, cidade, telefone, email))
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


#Deletar alguma venda
def delRegistroVendas(id):
    banco = sqlite3.connect('vendas.db')
    cursor = banco.cursor()
    if verificarID('venda', 'idvenda', id):
        cursor.execute(f'DELETE FROM venda WHERE idvenda={id}')
        banco.commit()
    else:
        print('ID INVÁLIDO, TENTE NOVAMENTE')


#Deletar algum produto
def delRegistroProduto(id):
    banco = sqlite3.connect('vendas.db')
    cursor = banco.cursor()
    if verificarID('produto', 'idprod', id):
        cursor.execute(f'DELETE FROM produto WHERE idprod={id}')
        banco.commit()
    else:
        print('ID INVÁLIDO, TENTE NOVAMENTE')


#Deletar algum cliente
def delRegistroCliente(id):
    banco = sqlite3.connect('vendas.db')
    cursor = banco.cursor()
    if verificarID('cliente', 'idcliente', id):
        cursor.execute(f'DELETE FROM produto WHERE cliente={id}')
        banco.commit()
    else:
        print('ID INVÁLIDO, TENTE NOVAMENTE')
        
if verificarID('cliente', 'idcliente', 5) and verificarID('produto', 'idprod', 7):
    print('Tem IDS')
    cursor.execute('UPDATE venda SET data_venda=?, valor_total=?, idcliente=?, idprod=?, nomeFunc=? WHERE idvenda = ?',('2023-01-02', 450, 5, 7, 'patas', 1))
    banco.commit()
    banco.close()
else:
    print('Não tem')