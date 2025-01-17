
from tkinter import ttk, CENTER, Canvas
import tkinter as tk
import sqlite3 as sql
import colorama as color
import customtkinter
from PIL import Image, ImageTk
import pyrealsense2 as rs
import FUNCOES_BD
import FUNCOES_TKINTER
import FUNCOES_CAMERA_WRL as fun2 #Funcções para camêra
from direction import folder, pasta_bd


pasta = folder()

#CORES USADAS
verde = '#416951' #Cor botão
bege = '#C9B783' #Cor botão
marrom = '#68584A' 
verde_escuro = '#1F3422' #Titulos
fundo_branco = 'white' #fundo das letras em frames brancos

def selecao(inp_ID, inp_tipo): # {=========Leitura Grupo, SIte, BOF e ID(FRAME 1)=========}
    global ID
    
    inp_ID = int(inp_ID)
    ID = inp_ID
    
    conn, cursor = FUNCOES_BD.CONECTA_BD( fr"{pasta_bd()}\REGISTROS_WRL.db")
    comando = f"SELECT * FROM DADOS_EMPRESAS WHERE ID = {inp_ID} AND TIPO = '{inp_tipo}' "
    cursor.execute(comando)
    dados = cursor.fetchall()
    FUNCOES_BD.DESCONECTA_BD(conn)
    
    grupo_completo = list(dados[0])
    dados = [item for sublist in dados for item in sublist]
    grupo_completo = grupo_completo[0]
    lista_grupo = grupo_completo.split('/')
    
    return  dados, lista_grupo

def tabela(int_arquivo): # {=========Informações da tabela(FRAME 2)=========}
    global registro_foto
    
    conn, cursor = FUNCOES_BD.CONECTA_BD( fr"{pasta_bd()}\REGISTROS_WRL.db")
    comando = f"SELECT * FROM B6 WHERE ARQUIVO = '{int_arquivo}' "
    cursor.execute(comando)
    dados2 = cursor.fetchone()
    FUNCOES_BD.DESCONECTA_BD(conn)
    registro_foto = int_arquivo
    return dados2

def imagens(registro_foto):  # {=========Informações para imagens(FRAME 2)=========}
    
    endereco_pastafotos =  fr"{pasta}\FOTOS_ANALISE"
    endereco_pastaguias =  fr"{pasta}\FOTOS_SEGMENTADA"
        
    arquivofoto = endereco_pastafotos +'\\' +registro_foto
    arquivoguia = endereco_pastaguias +'\\' +registro_foto
        
    return arquivofoto, arquivoguia

def voltar_menu(aba_menu, insp_1,insp_2, insp_3):
    aba_menu.deiconify()  # Exiba a janela da aba 1
    insp_3.destroy()  # Destrua a janela da aba 2
    insp_2.destroy()  # Destrua a janela cadastro
    insp_1.destroy()

def adicionar_detalhes(inp_menu):
    largura = inp_menu.winfo_screenwidth()
    altura = inp_menu.winfo_screenheight()

    # Cria um Frame para o Canvas, que ficará no fundo
    canvas_frame = tk.Frame(inp_menu, width=largura, height=altura, bg=fundo_branco)
    canvas_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    canvas = Canvas(canvas_frame, width=largura, height=altura, highlightthickness=0)
    canvas.pack(fill=tk.BOTH, expand=True)

    # Triângulo vermelho no canto superior direito
    canvas.create_polygon(largura, 0, largura, 300, largura-300, 0, fill="#94031E", outline="#94031E")

    # Triângulo verde no canto inferior esquerdo
    canvas.create_polygon(0, altura, 0, altura-300, 300, altura, fill=verde, outline=verde)

def tela(inp_janela): # {=======================Configuração de tela=========================}
    inp_janela.title("DADOS DA INSPECÇÃO")
    inp_janela.configure(background= fundo_branco)
    inp_janela.attributes("-fullscreen", True)
    
def frames_da_tela(inp_janela): 
    global frame_1, frame_2
    # {=======================Frame da Direita=========================}
    frame_1 = tk.Frame(inp_janela, bd=2,
                            bg= fundo_branco,
                            highlightthickness=1)
    frame_1.place(relx=0.4, rely=0.02,relwidth=0.59, relheight=0.96)
    
    # {=======================Frame da Esquerda=========================}
    frame_2 = tk.Frame(inp_janela, bd=2,
                            bg= fundo_branco,
                            highlightthickness=1)
    frame_2.place(relx=0.01, rely=0.02,relwidth=0.38, relheight=0.96)
    
    return frame_1, frame_2

def componentes_frame1(inp_ID, inp_tipo, int_arquivo,inp_menu, janela_cadastro1,janela_cadastro2,inp_janela):
    dados, lista_grupo = selecao(inp_ID,inp_tipo)
    
    grupo = dados[1]
    site = dados[2]
    BOF = dados[3]
    # tipo = dados[4]
    ID = dados[5]
    vida = dados[6]
    
    # {=======================Título=========================}
    titulo1_pg1 = FUNCOES_TKINTER.CRIAR_LABEL(frame_1, "Dados do Bico",fundo_branco,"#2F4F4F",'arial', '25', 'bold')
    titulo1_pg1.place(relx=0.32, rely=0.03)
    
    # {=======================Grupo=========================}
    grupo_pg1 = FUNCOES_TKINTER.CRIAR_LABEL(frame_1,"Grupo:",fundo_branco,verde_escuro,'verdana', '20','bold')
    grupo_pg1.place(relx=0.05, rely=0.15)

    grupo_pg1 = tk.Label(frame_1,
                            text = grupo,
                            font=('verdana', '20'),
                            bg= fundo_branco,
                            fg=verde_escuro)
    grupo_pg1.place(relx=0.2, rely=0.15)

    # {=======================Site=========================}
    site_pg1 = FUNCOES_TKINTER.CRIAR_LABEL(frame_1,"Site:",fundo_branco,verde_escuro,'verdana', '20','bold')
    site_pg1.place(relx=0.05, rely=0.25)

    site_pg1 = tk.Label(frame_1,
                            text=site,
                            font=('verdana', '20'),
                            bg= fundo_branco,
                            fg=verde_escuro)
    site_pg1.place(relx=0.15, rely=0.25)

    # {=======================BOF=========================}
    BOF_pg1 = FUNCOES_TKINTER.CRIAR_LABEL(frame_1,"BOF:",fundo_branco,verde_escuro,'verdana', '20','bold')
    BOF_pg1.place(relx=0.05, rely=0.35)

    site_pg1 = tk.Label(frame_1,
                        text=BOF,
                        font=('verdana', '20'),
                        bg= fundo_branco,
                        fg=verde_escuro)
    site_pg1.place(relx=0.15, rely=0.35)
    
    # {=======================ID=========================}
    ID_pg1 = FUNCOES_TKINTER.CRIAR_LABEL(frame_1,"ID:",fundo_branco,verde_escuro,'verdana', '20','bold')
    ID_pg1.place(relx=0.05, rely=0.45)

    ID_informado_pg1 = tk.Label(frame_1,
                                text = ID,
                                font=('verdana', '20'),
                                bg= fundo_branco,
                                fg=verde_escuro)
    ID_informado_pg1.place(relx=0.12, rely=0.45)
    
    # {=======================Data=========================}
    dados2 = tabela(int_arquivo)
    data_foto = dados2[9] 
    hora_foto = dados2[10] 
    medidas_foto = dados2[11:] 

    Data_pg1 = FUNCOES_TKINTER.CRIAR_LABEL(frame_1,"Data:",fundo_branco,verde_escuro,'verdana', '20','bold')
    Data_pg1.place(relx=0.05, rely=0.6)

    Data_informado_pg1 = tk.Label(frame_1,
                                text = data_foto,
                                font=('verdana', '20'),
                                bg= fundo_branco,
                                fg=verde_escuro)
    Data_informado_pg1.place(relx=0.17, rely=0.6)
    
    # {=======================Hora=========================}
    Hora_pg1 = FUNCOES_TKINTER.CRIAR_LABEL(frame_1,"Hora:",fundo_branco,verde_escuro,'verdana', '20','bold')
    Hora_pg1.place(relx=0.05, rely=0.7)

    Hora_informado_pg1 = tk.Label(frame_1,
                                text = hora_foto,
                                font=('verdana', '20'),
                                bg= fundo_branco,
                                fg=verde_escuro)
    Hora_informado_pg1.place(relx=0.17, rely=0.7)

    # {=======================Vida=========================}
    Vida_pg1 = FUNCOES_TKINTER.CRIAR_LABEL(frame_1,"Vida:",fundo_branco,verde_escuro,'verdana', '20','bold')
    Vida_pg1.place(relx=0.05, rely=0.8)

    Vida_informado_pg1 = tk.Label(frame_1,
                                text = vida,
                                font=('verdana', '20'),
                                bg= fundo_branco,
                                fg=verde_escuro)
    Vida_informado_pg1.place(relx=0.17, rely=0.8)
    
    # {=======================Botão Continuar=========================}
    btContinuar_pg1 = tk.Button(frame_1,
                                    text='MENU',
                                    cursor = "hand2",
                                    bd = 4,
                                    bg = verde,
                                    fg = bege,
                                    font= ("arial", 13,'bold'),
                                    command= lambda: voltar_menu( inp_menu,janela_cadastro1,janela_cadastro2, inp_janela))
    btContinuar_pg1.place(relx=0.55, rely=0.9, relwidth=0.12, relheight=0.08)
    
    # {=======================Registros=========================}

    tabela_pg1 = ttk.Treeview(frame_1, height=12,column=("col1", "col2"),style="mystyle.Treeview")

    style = ttk.Style()
    style.configure("Treeview.Heading", font=('Verdana', 15,'bold'))
    style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Verdana', 13))

    tabela_pg1.column("#0", width=0, stretch=tk.NO)  # Ocultando a primeira coluna
    tabela_pg1.heading("#0", text="")

    tabela_pg1.heading("#1", text="Classe")
    tabela_pg1.heading("#2", text="Diametro(mm)")
    
    tabela_pg1.column("#1", width=150, anchor='center')
    tabela_pg1.column("#2", width=200, anchor='center')
    
    i = 1
    for dado in medidas_foto:
        if i == 1:
            tabela_pg1.insert("", tk.END, values=('Bico', dado))
        else:
            tabela_pg1.insert("", tk.END, values=(f'Furo {i-1}', dado))
        i += 1
                
    tabela_pg1.place(relx=0.45, rely=0.35, relwidth=0.5, relheight=0.5)


def componentes_frame2(inp_janela): # {=========Componentes da direita=========}
    
    arquivofoto, arquivoguia = imagens(registro_foto)
    print('\nArquivo_foto=',arquivofoto,'\nArquivo guia = ', arquivoguia)
    
    # {=======================Imagem 1=========================}
    img1_pg1 = tk.PhotoImage(file = arquivofoto)
    img1_pg1 = img1_pg1.subsample(2, 2)
    
    fotoimg1_pg1 = tk.Label(frame_2,
                            borderwidth=3,
                            highlightthickness=4,
                            highlightbackground='gray',
                            bg= fundo_branco,
                            image = img1_pg1)
    fotoimg1_pg1.place(relx=0.5, rely=0.25, anchor=CENTER)

    # {=======================Imagem 2=========================}
    img2_pg1 = tk.PhotoImage(file = arquivoguia)
    img2_pg1 = img2_pg1.subsample(2, 2)

    fotoimg2_pg1 = tk.Label(frame_2,
                            borderwidth=3,
                            highlightthickness=4,
                            highlightbackground='gray',
                            bg= fundo_branco,
                            image = img2_pg1)
    fotoimg2_pg1.place(relx=0.5, rely=0.7, anchor=CENTER)

    # {=======================WRL=========================}
    titulo2_pg1 = tk.Label(frame_2,
                            text="Wear Register Lances (WRL)",
                            font=('italic', '18'),
                            bg= fundo_branco,
                            fg="#94031E")
    titulo2_pg1.place(relx=0.01, rely=0.94)
    
    inp_janela.mainloop()

def aba_dados(inp_janela,inp_ID,inp_tipo, int_arquivo,inp_menu,janela_cadastro1):
    # janela = tk.Tk()
    janela = tk.Toplevel(inp_janela)
    tela(janela)
    adicionar_detalhes(janela)
    frames_da_tela(janela)
    componentes_frame1(inp_ID, inp_tipo, int_arquivo,inp_menu,janela_cadastro1,inp_janela,janela)
    componentes_frame2(janela)
    
    janela.transient(inp_janela) #TOPLEVEL
    janela.focus_force() #TOPLEVEL
    janela.grab_set() #TOPLEVEL
    
    return janela
    
print("\n\n", color.Fore.GREEN + "Iniciando o código - Dados do bico" + color.Style.RESET_ALL)
print(color.Fore.RED + "Finalizando o código - Dados do bico" + color.Style.RESET_ALL, "\n")