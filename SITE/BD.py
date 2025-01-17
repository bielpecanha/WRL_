import sqlite3
import pandas as pd

# cursor.execute(""" CREATE TABLE Lanca_4F(

#     id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#     Data TEXT,
#     Primeiro INTEGER,
#     Segundo INTEGER,
#     Terceiro INTEGER,
#     Quarto INTEGER

#     ) """)
# banco = sqlite3.connect('simu.db')
# cursor = banco.cursor()
# cursor.execute("INSERT INTO banco VALUES(?,?,?,?,?,?)",(1 , 'AMERICA DO SUL' , 'BRASIL' , 'Usiminas' , 'Ipatinga 1', '1-3' ))
# cursor.execute("INSERT INTO banco VALUES(?,?,?,?,?,?)",(2 , 'AMERICA DO SUL' , 'BRASIL' , 'Usiminas' , 'Ipatinga 1', '1-2' ))
# cursor.execute("INSERT INTO banco VALUES(?,?,?,?,?,?)",(3 , 'AMERICA DO SUL' , 'BRASIL' , 'Usiminas' , 'Ipatinga 2', '1-4' ))
# cursor.execute("INSERT INTO banco VALUES(?,?,?,?,?,?)",(4 , 'AMERICA DO SUL' , 'BRASIL' , 'Usiminas' , 'Ipatinga 2', '2-3' ))
# cursor.execute("INSERT INTO banco VALUES(?,?,?,?,?,?)",(5 , 'AMERICA DO SUL' , 'BRASIL' , 'Usiminas' , 'Ipatinga 2','2-4' ))
# cursor.execute("INSERT INTO banco VALUES(?,?,?,?,?,?)",(6 , 'AMERICA DO SUL' , 'BRASIL' , 'Usiminas' , 'Ipatinga 2', '4-5' ))
# cursor.execute("INSERT INTO banco VALUES(?,?,?,?,?,?)",(7 , 'AMERICA DO SUL' , 'BRASIL' , 'ArcelorMITTAL' , 'Bloco 1', '1-2' ))
# cursor.execute("INSERT INTO banco VALUES(?,?,?,?,?,?)",(8 , 'AMERICA DO SUL' , 'BRASIL' , 'ArcelorMITTAL' , 'Bloco 1', '2-3' ))
# cursor.execute("INSERT INTO banco VALUES(?,?,?,?,?,?)",(9 , 'AMERICA DO SUL' , 'BRASIL' , 'ArcelorMITTAL' , 'Bloco 1', '2-4'))
# cursor.execute("INSERT INTO banco VALUES(?,?,?,?,?,?)",(10 , 'AMERICA DO SUL' , 'BRASIL' , 'ArcelorMITTAL' , 'Bloco 1', '3-5' ))
# cursor.execute("DELETE FROM banco")
# banco.commit()



# cursor.execute("INSERT INTO Lanca_4F VALUES(?,?,?,?,?,?)",(3 , '15/09' , 4.1 , 4.6 , 4.8 , 4.4 ))
# cursor.execute("INSERT INTO Lanca_4F VALUES(?,?,?,?,?,?)",(4 , '22/09' , 4.3 , 4.7 , 5.1 , 4.4 ))
# cursor.execute("INSERT INTO Lanca_4F VALUES(?,?,?,?,?,?)",(5 , '29/09' , 4.5 , 4.9 , 5.3 , 4.4 ))

# banco.commit()

# def valor_datas():
#     banco = sqlite3.connect('banquinho.db')
#     cursor = banco.cursor() 

#     col_datas = cursor.execute("SELECT Data FROM Lanca_4F")
#     banco.commit()

#     datas = []
#     for i in col_datas:
#         data = str(i)
#         data = data[2:-3]
#         datas.append(data)
    
#     banco.close()
    
#     return datas

# def dia_1():
#     banco = sqlite3.connect('banquinho.db')
#     cursor = banco.cursor()

#     col_dia1 = cursor.execute("SELECT Primeiro FROM Lanca_4F")
#     banco.commit()

#     col_dia1 = cursor.fetchall()

#     Lista_dia1=[]
#     for j in col_dia1:
#         diametro1 = str(j)
#         diametro1 = diametro1[1:-2]
#         diametro1 = float(diametro1)
#         Lista_dia1.append(diametro1)

#     banco.close()    

#     return Lista_dia1

# def dia_2():
#     banco = sqlite3.connect('banquinho.db')
#     cursor = banco.cursor()

#     col_dia2 = cursor.execute("SELECT Segundo FROM Lanca_4F")
#     banco.commit()

#     col_dia2 = cursor.fetchall()

#     Lista_dia2=[]
#     for j in col_dia2:
#         diametro2 = str(j)
#         diametro2 = diametro2[1:-2]
#         diametro2 = float(diametro2)
#         Lista_dia2.append(diametro2)

#     banco.close()    

#     return Lista_dia2

# def dia_3():
#     banco = sqlite3.connect('banquinho.db')
#     cursor = banco.cursor()

#     col_dia3 = cursor.execute("SELECT Terceiro FROM Lanca_4F")
#     banco.commit()

#     col_dia3 = cursor.fetchall()

#     Lista_dia3=[]
#     for j in col_dia3:
#         diametro3 = str(j)
#         diametro3 = diametro3[1:-2]
#         diametro3 = float(diametro3)
#         Lista_dia3.append(diametro3)

#     banco.close()    

#     return Lista_dia3

# def dia_4():
#     banco = sqlite3.connect('banquinho.db')
#     cursor = banco.cursor()

#     col_dia4 = cursor.execute("SELECT Quarto FROM Lanca_4F")
#     banco.commit()

#     col_dia4 = cursor.fetchall()

#     Lista_dia4=[]
#     for j in col_dia4:
#         diametro4 = str(j)
#         diametro4 = diametro4[1:-2]
#         diametro4 = float(diametro4)
#         Lista_dia4.append(diametro4)

#     banco.close()    

#     return Lista_dia4

# def tudo():
#     banco = sqlite3.connect('banquinho.db') 

#     dados = "SELECT * FROM Lanca_4F"
#     df = pd.read_sql(dados,banco)

#     banco.close()

#     return df












# banco = sqlite3.connect('banquinho.db')
# cursor = banco.cursor()

# cursor.execute(""" CREATE TABLE Quatro_Furos(

#     id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#     Data TEXT,
#     Diâmetro INTEGER

#     ) """)

# id = int(input("id: "))
# data = input('Data: ')
# valor = int(input('Diâmetro: '))

# cursor.execute("INSERT INTO Quatro_Furos VALUES(?,?,?)",(5,'29/09',5.2))
# banco.commit()

# a=b=2
# if a>1:
#     col_datas = cursor.execute("SELECT Data FROM Quatro_Furos")
#     banco.commit()

#     datas = []
#     for i in col_datas:
#         data = str(i)
#         data=data[2:]
#         data=data[:-3]
#         datas.append(data)

#     print(datas)
#     a-=2

# if b>1:
#     col_dia4 = cursor.execute("SELECT Diâmetro FROM Quatro_Furos")
#     banco.commit()

#     col_dia4 = cursor.fetchall()

#     diametros_4F=[]
#     for j in col_dia4:
#         diametro = str(j)
#         diametro = diametro.replace(',','')
#         diametro = diametro[1:]
#         diametro = diametro[:-1]
#         diametro = float(diametro)
#         diametros_4F.append(diametro)
    
#     print(diametros_4F)
#     b-=2
    


# print(diametros_4F)
# cursor.execute("DROP TABLE Quatro_Furos")
print('executado')