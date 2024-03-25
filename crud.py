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
               nomeFunc TEXT,
               FOREIGN KEY (idcliente) references cliente(idcliente),
               FOREIGN KEY (idprod) references produto(idprod)
)''')


#Função para verificar se existe o ID na tabela
def verificarID(tabela, coluna, id):
    banco = sqlite3.connect('vendas.db', check_same_thread=False)
    cursor = banco.cursor()

    cursor.execute(f'SELECT {coluna} FROM {tabela}')
    lista = cursor.fetchall()
    for i in range (len(lista)):
        if id == lista[i][0]:
            return True  
        else:
            i=+1


#Função de inserção para Clientes
def inserirClientes(id,nome, data_nasc, cidade, telefone, email):
    cursor.execute('INSERT INTO cliente VALUES(?,?,?,?,?,?)',(None,nome, data_nasc, cidade, telefone, email))
    banco.commit()


#Função de inserção para produtos
def inserirProdutos(id,nome, preco, marca, categoria, qtd):
    cursor.execute('INSERT INTO produto VALUES(?,?,?,?,?,?)',(None,nome, preco, marca, categoria, qtd))
    banco.commit()        

            
#Função de inserção de vendas
def inserirVendas(idvenda,data_venda, valor_total, idcliente, idprod, nomeFunc):
    #Lógica para verificar a existência dos IDS
    if verificarID('cliente', 'idcliente', idcliente) and verificarID('produto', 'idprod', idprod):
        cursor.execute('INSERT INTO venda VALUES (?,?,?,?,?,?)',(None, data_venda, valor_total, idcliente, idprod, nomeFunc))
        banco.commit()
    else:
        print('DADOS INVÁLIDOS, TENTE NOVAMENTE')


#Deletar alguma venda
def delRegistroVendas(id):
    if verificarID('venda', 'idvenda', id):
        cursor.execute(f'DELETE FROM venda WHERE idvenda={id}')
        banco.commit()
    else:
        print('ID INVÁLIDO, TENTE NOVAMENTE')


#Deletar algum produto
def delRegistroProduto(id):
    if verificarID('produto', 'idprod', id):
        cursor.execute(f'DELETE FROM produto WHERE idprod={id}')
        banco.commit()
    else:
        print('ID INVÁLIDO, TENTE NOVAMENTE')


#Deletar algum cliente
def delRegistroCliente(id):
    if verificarID('cliente', 'idcliente', id):
        cursor.execute(f'DELETE FROM produto WHERE cliente={id}')
        banco.commit()
    else:
        print('ID INVÁLIDO, TENTE NOVAMENTE')


#INSERÇÃO DE DADOS

inserirClientes(1,"João Silva", "1990-05-15", "São Paulo", "123456789", "joao@email.com")
inserirClientes(1,"Maria Santos", "1985-08-20", "Rio de Janeiro", "987654321", "maria@email.com")
inserirClientes(1,"Pedro Oliveira", "1978-03-10", "Belo Horizonte", "555666777", "pedro@email.com")
inserirClientes(1,"Ana Souza", "1995-11-25", "Salvador", "111222333", "ana@email.com")
inserirClientes(1,"Lucas Costa", "1980-09-05", "Porto Alegre", "999888777", "lucas@email.com")

'''clientes = [
    ("João Silva", "1990-05-15", "São Paulo", "123456789", "joao@email.com"),
    ("Maria Santos", "1985-08-20", "Rio de Janeiro", "987654321", "maria@email.com"),
    ("Pedro Oliveira", "1978-03-10", "Belo Horizonte", "555666777", "pedro@email.com"),
    ("Ana Souza", "1995-11-25", "Salvador", "111222333", "ana@email.com"),
    ("Lucas Costa", "1980-09-05", "Porto Alegre", "999888777", "lucas@email.com")
]


produtos_supermercado = [
    ("Arroz", 12.99, "Tio João", "Alimentos", 50),
    ("Feijão", 8.99, "Camil", "Alimentos", 40),
    ("Leite", 3.49, "Nestlé", "Laticínios", 60),
    ("Pão de Forma", 5.99, "Wickbold", "Padaria", 30),
    ("Óleo de Soja", 4.79, "Soya", "Alimentos", 20)
]

vendas = [
    (None, '2024-03-24', 150.00, 1, 1, 'João'),
    (None, '2024-03-24', 250.00, 2, 3, 'Maria'),
    (None, '2024-03-25', 50.00, 3, 2, 'Pedro'),
    (None, '2024-03-25', 120.00, 1, 4, 'Ana'),
    (None, '2024-03-26', 80.00, 2, 5, 'Lucas')
]'''

