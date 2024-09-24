import sqlite3

# Conecta ao banco de dados
conn = sqlite3.connect('desafio_dio.db')

# Cria um objeto cursor
cursor = conn.cursor()

# Obtem o ID da conta a ser apagada
id_conta = int(input("Digite o ID da conta que deseja apagar: "))

# Verifica se a conta existe
cursor.execute("SELECT * FROM Conta WHERE id = ?", (id_conta,))
conta = cursor.fetchone()

if conta is None:
    print("Conta não encontrada.")
else:
    id_cliente = conta[1]
    
    # Apaga a conta
    cursor.execute("DELETE FROM Conta WHERE id = ?", (id_conta,))
    
    # Verifica se o cliente associado à conta possui outras contas
    cursor.execute("SELECT * FROM Conta WHERE id_cliente = ?", (id_cliente,))
    outras_contas = cursor.fetchall()
    
    if len(outras_contas) == 0:
        # Apagar o cliente se ele não tiver outras contas
        cursor.execute("DELETE FROM Cliente WHERE id = ?", (id_cliente,))
        
    # Comitando as alterações
    conn.commit()
    
    print("Conta e cliente associado apagados com sucesso.")

# Fechando a conexão
conn.close()
