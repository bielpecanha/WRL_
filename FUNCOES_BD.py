import sqlite3 as sql
from customtkinter import *

def CONECTA_BD(inp_caminho):
    conn = sql.connect(inp_caminho)
    cursor = conn.cursor(); print("\nConectando ao BD - FUNCOES_WRL")
    return conn, cursor
    
def DESCONECTA_BD(conn):
    conn.close(); print("Desconectando do BD - FUNCOES_WRL\n")
