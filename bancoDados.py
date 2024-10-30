import sqlite3

def criar_banco():
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def adicionar_usuario(username, password):
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    try:
        c.execute('INSERT INTO usuarios (username, password) VALUES (?, ?)', (username, password))
    except sqlite3.IntegrityError:
        print(f"Usuário '{username}' já existe.")
    conn.commit()
    conn.close()

def validar_login(username, password):
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    c.execute('SELECT * FROM usuarios WHERE username = ? AND password = ?', (username, password))
    usuario = c.fetchone()
    conn.close()
    return usuario is not None
