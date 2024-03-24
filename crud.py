import sqlite3

#CREATING DB
banco = sqlite3.connect('vendas.db')

#DEPENDECY INJECTION
cursor = banco.cursor()

#tabela cliente
cursor.execute('''CREATE TABLE IF NOT EXISTS cliente (
                    idcliente INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    email TET,
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
               FOREIGN KEY (idcliente) references cliente(idcliente),
               FOREIGN KEY (idprod) references produto(idprod)
)''')

def verificarID(tabela, coluna, id):
    cursor.execute(f'SELECT {coluna} FROM {tabela}')
    lista = cursor.fetchall()
    listaIds = list()
    for i in range (len(lista)):
        if id == lista[i][0]:
            return True  
        else:
            i=+1

def inserirClientes(id,nome, data_nasc, cidade, telefone, email):
    cursor.execute('INSERT INTO cliente VALUES(?,?,?,?,?,?)',(None,nome, data_nasc, cidade, telefone, email))
    banco.commit()
def inserirProdutos(id,nome, preco, marca, categoria, qtd):
    cursor.execute('INSERT INTO produto VALUES(?,?,?,?,?,?)',(None,nome, preco, marca, categoria, qtd))
    banco.commit()        

def verificarID(tabela, coluna, id):
    cursor.execute(f'SELECT {coluna} FROM {tabela}')
    lista = cursor.fetchall()
    for i in range (len(lista)):
        if id == lista[i][0]:
            return True  
        else:
            i=+1
            
def inserirVendas(idvenda,data_venda, valor_total, idcliente, idprod, nomeFunc):
    if verificarID('cliente', 'idcliente', idcliente) and verificarID('produto', 'idprod', idprod):
        cursor.execute('INSERT INTO venda VALUES (?,?,?,?,?,?)',(None, data_venda, valor_total, idcliente, idprod, nomeFunc))
        banco.commit()
    else:
        print('DADOS INVÁLIDOS, TENTE NOVAMENTE')

inserirVendas(1,'2024-01-03', 758.50, 4 ,5 ,'Gabriel')

