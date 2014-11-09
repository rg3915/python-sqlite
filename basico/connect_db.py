# connect_db.py
import sqlite3

# conectando...
conn = sqlite3.connect('clientes.db')
# desconectando...
conn.close()
