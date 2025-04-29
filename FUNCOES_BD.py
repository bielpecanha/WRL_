import sqlite3 as sql
from customtkinter import *

conexao = sql.connect('DADOS_EMPRESAS.db')
cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS DADOS_EMPRESAS(
    ID TEXT NOT NULL,
    Usina TEXT NOT NULL,
    Site TEXT NOT NULL,
    País TEXT NOT NULL,
    Estado TEXT NOT NULL,
    Grupo TEXT NOT NULL,
    Furos TEXT NOT NULL,
    BOF TEXT NOT NULL,
    Tipo TEXT NOT NULL,
    Ult vida TEXT NOT NULL
    )
'''
)

def CONECTA_BD(inp_caminho):
    conn = sql.connect(inp_caminho)
    cursor = conn.cursor(); print("\nConectando ao BD - FUNCOES_WRL")
    return conn, cursor
    
def DESCONECTA_BD(conn):
    conn.close(); print("Desconectando do BD - FUNCOES_WRL\n")
