import sqlite3


def soma(a, b):
    return a + b


def buscar_usuario(nome):
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE nome = '" + nome + "'")
    return cursor.fetchall()


if __name__ == "__main__":
    print(soma(2, 3))
