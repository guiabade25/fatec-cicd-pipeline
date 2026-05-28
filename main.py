import sqlite3


def soma(a, b):
    return a + b


def buscar_usuario(nome):
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    query = "SELECT * FROM usuarios WHERE nome = '" + nome + "'"
    cursor.execute(query)
    return cursor.fetchall()


def login(usuario, senha):
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM users WHERE username='" + usuario +
        "' AND password='" + senha + "'"
    )
    return cursor.fetchone()


if __name__ == "__main__":
    print(soma(2, 3))
    