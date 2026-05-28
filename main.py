import sqlite3


def soma(a, b):
    return a + b


def buscar_usuario(nome):
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    query = "SELECT * FROM usuarios WHERE nome = '" + nome + "'"
    cursor.execute(query)
    return cursor.fetchall()


if __name__ == "__main__":
    print(soma(2, 3))
    nome = input("Digite o nome: ")
    buscar_usuario(nome)
