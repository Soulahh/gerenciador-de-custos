import sqlite3
import os

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def criar_database():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute(f'''CREATE TABLE IF NOT EXISTS despesas(ID integer PRIMARY KEY AUTOINCREMENT, descricao VARCHAR(255) NOT NULL, valor DECIMAL(10,2) NOT NULL, data DATE NOT NULL);''')
    con.commit()


def get_connection():
    return sqlite3.connect('database.db')

def inserir_despesa(descricao, valor, data):
    con = get_connection()
    cur = con.cursor()
    cur.execute("INSERT INTO despesas (descricao, valor, data) VALUES (?,?,?)",(descricao,valor,data))
    con.commit()
    con.close()

def listar_despesas():
    con = get_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM despesas")
    rows = cur.fetchall()
    con.close()
    return rows

def imprimir_despesas():
    for row in listar_despesas():
        print(f"{row[0]:>3}: {row[1]:<20} | {row[2]:>8.2f} | {row[3]}")

def imprimir_menu():
    print(f" GERENCIADOR DE CUSTOS ")
    print(f"-------------------------")
    print(f"Opções: ")
    print(f'''1 - Inserir Despesa\n2 - Listar Despesas\n3- Remover Despesa
4-Alterar Despesa\n5-Fechar Aplicativo''')

def receber_despesa():
    descricao = input("Descreva a despesa: ")
    valor = float(input("Insira o valor da despesa: "))
    data = input("Insira a data de contracao da despesa: ")
    return descricao, valor, data

def receber_id_despesa():
    return int(input("Insira o ID da despesa: "))

def remover_despesa(id):
    con = get_connection()
    cur = con.cursor()
    cur.execute(f"DELETE FROM despesas WHERE ID = ?", (id,))
    con.commit()
    con.close()

def atualizar_despesa(id_despesa):
    con = get_connection()
    cur = con.cursor()
    despesa = receber_despesa()
    cur.execute(f"UPDATE despesas SET descricao = ?, valor = ?, data = ? WHERE id = ?",(despesa[0],despesa[1],despesa[2],id_despesa))
    con.commit()
    con.close()

def iniciar_programa():
    criar_database()
    continuar = True
    while continuar:
        imprimir_menu()
        opcao = int(input("Insira sua opcao: "))
        limpar_tela()
        match opcao:
            case 1:
                despesa = receber_despesa()
                inserir_despesa(despesa[0], despesa[1],despesa[2])
            case 2:
                imprimir_despesas()
            case 3:
                id_despesa = receber_id_despesa()
                remover_despesa(id_despesa)
            case 4:
                id_despesa = receber_id_despesa()
                atualizar_despesa(id_despesa)
            case 5:
                print(f"\nEncerrando o Programa!")
                continuar = False
criar_database()
inserir_despesa("Almoço", 25.31,'2001-10-19')
inserir_despesa("Janta",19.09,'2025-11-22')