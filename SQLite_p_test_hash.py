#script para criar o banco de ddos e a tabela
import sqlite3
conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE usuario(nome TEXT NOT NULL, senha TEXT NOT NULL);')
