import sqlite3

# Conecta ao banco de dados (ou cria se não existir)
conn = sqlite3.connect('desafio_dio.db')

# Cria um objeto cursor
cursor = conn.cursor()

# Obtem os dados do usuário
nome = input("Digite o nome do cliente: ")
cpf = input("Digite o CPF do cliente: ")
endereco = input("Digite o endereço do cliente: ")

# Cria a tabela "Cliente" (caso não exista)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Cliente (
        id INTEGER PRIMARY KEY,
        Nome TEXT,
        cpf TEXT,
        endereco TEXT
    )
''')

# Insere os dados do cliente na tabela "Cliente"
cursor.execute('''
    INSERT INTO Cliente (Nome, cpf, endereco)
    VALUES (?, ?, ?)
''', (nome, cpf, endereco))

# Comitando as alterações
conn.commit()

# Obtem os dados da conta
id_cliente = cursor.lastrowid
id_conta = input("Digite o ID da conta: ")
tipo_conta = input("Digite o tipo de conta: ")
agencia = input("Digite a agência: ")
numero_conta = input("Digite o número da conta: ")
saldo = float(input("Digite o saldo: "))

# Cria a tabela "Conta" (caso não exista)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Conta (
        id_cliente INTEGER,
        id TEXT,
        tipo TEXT,
        agencia TEXT,
        numero INTEGER,
        saldo DECIMAL,
        FOREIGN KEY (id_cliente) REFERENCES Cliente (id)
    )
''')

# Insere os dados da conta na tabela "Conta"
cursor.execute('''
    INSERT INTO Conta (id_cliente, id, tipo, agencia, numero, saldo)
    VALUES (?, ?, ?, ?, ?, ?)
''', (id_cliente, id_conta, tipo_conta, agencia, numero_conta, saldo))

# Comitando as alterações
conn.commit()

# Consulta na tabela "Cliente" e "Conta"
cursor.execute('''
    SELECT Cliente.*, Conta.*
    FROM Cliente
    LEFT JOIN Conta ON Cliente.id = Conta.id_cliente
''')
resultados = cursor.fetchall()

# Imprime os resultados
print("Dados dos Clientes e suas Contas:")
for resultado in resultados:
    print("ID do Cliente:", resultado[0])
    print("Nome:", resultado[1])
    print("CPF:", resultado[2])
    print("Endereço:", resultado[3])
    if resultado[4] is not None:
        print("ID da Conta:", resultado[4])
        print("Tipo de Conta:", resultado[5])
        print("Agência:", resultado[6])
        print("Número da Conta:", resultado[7])
        print("Saldo:", resultado[8])
    else:
        print("Cliente não possui conta associada")
    print("-------------------------")

# Fecha a conexão
conn.close()
