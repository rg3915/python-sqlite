# 12_read_sql.py
import sqlite3
import io

conn = sqlite3.connect('clientes_recuperado.db')
cursor = conn.cursor()

f = io.open('clientes_dump.sql', 'r')
sql = f.read()
cursor.executescript(sql)

print('Banco de dados recuperado com sucesso.')
print('Salvo como clientes_recuperado.db')

conn.close()
