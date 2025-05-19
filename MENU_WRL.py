import threading
import tkinter as tk
import sqlite3 as sql
import colorama as color
from tkinter import ttk, messagebox, PhotoImage, Canvas
from customtkinter import *
from PIL import Image, ImageTk
import subprocess
import FUNCOES_TKINTER
from direction import folder
import Splash_screen as Loading
import os

print("\n\n", color.Fore.GREEN + "Iniciando o código - Tela do Menu" + color.Style.RESET_ALL)

pasta = folder()

#CORES USADAS
verde = '#416951' #Cor botão
bege = '#C9B783' #Cor botão
marrom = '#68584A' 
verde_escuro = '#1F3422' #Titulos

def menu_WRL():
    Janela_menu = tk.Tk()
    tela(Janela_menu)
    adicionar_detalhes(Janela_menu)
    frames_da_tela(Janela_menu)
    componentes_frame1(Janela_menu)
    Janela_menu.mainloop()

def tela(inp_menu): # {=======================Configuração de tela=========================}
    inp_menu.title("MENU - Wear Register Lances (WRL)")
    inp_menu.configure(background= verde_escuro)
    inp_menu.attributes("-fullscreen", True)
    #inp_menu.rowconfigure(0, weight=1)
    #inp_menu.columnconfigure(0, weight=1)
    
def ABA_CADASTRO_BICO(inp_menu):
    from CADASTRO_BICO_WRL import aba_cadastro_bico
    janela_cadastrar_bico = aba_cadastro_bico(inp_menu)
    janela_cadastrar_bico.deiconify()

def INICIAR_INSPECAO(inp_menu):

    #Inicia o processo de inspeção com uma tela de splash.
    
    def carregar_inspecao():
        from INSPECAO_1_WRL import aba_cadastro
        import FUNCOES_CAMERA_WRL as fun2  # Funções para câmera
        janela_cadastro = aba_cadastro(inp_menu)  # Executa o código pesado
        janela_cadastro.deiconify()

    # Abre o Splash e passa o código pesado como callback
    splash = Loading.Splash(inp_menu, carregar_inspecao)

    splash.grab_set()  # Bloqueia interação com outras janelas

    splash.protocol("WM_DELETE_WINDOW")

def ABA_CADASTRO_USINA(inp_menu):
    from CADASTRO_USINA_WRL import aba_cadastro_usina
    janela_cadastrar_bico = aba_cadastro_usina(inp_menu)
    janela_cadastrar_bico.deiconify()
    
def abrir_streamlit():
    comando = ['streamlit', 'run', fr'{pasta}\SITE\site_WRL.py']
    subprocess.Popen(comando)
    
def frames_da_tela(inp_menu):
    global frame_1

    frame_1 = FUNCOES_TKINTER.CRIAR_FRAME(inp_menu, 'white', '#668B8B')
    #frame_1.grid(row=0, column=0, sticky="nsew") 
    frame_1.place(relx=0.01, rely=0.02,relwidth=0.98, relheight=0.96)
    #frame_1.rowconfigure((0, 1, 2, 3, 4), weight=0)
    #frame_1.columnconfigure((0, 1, 2, 3, 4), weight=1)

def adicionar_detalhes(inp_menu):
    largura = inp_menu.winfo_screenwidth()
    altura = inp_menu.winfo_screenheight()

    canvas = tk.Canvas(inp_menu, bg='white', highlightthickness=0)
    #.grid(row=0, column=0, sticky="nsew")

    # Cria um Frame para o Canvas, que ficará no fundo
    canvas_frame = tk.Frame(inp_menu, width=largura, height=altura, bg='white')
    #canvas.grid(row=0, column=0, sticky="nsew")
    canvas_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    canvas = Canvas(canvas_frame, width=largura, height=altura, highlightthickness=0)
    canvas.pack(fill=tk.BOTH, expand=True)

    # Triângulo vermelho no canto superior direito
    canvas.create_polygon(largura, 0, largura, 300, largura-300, 0, fill="#94031E", outline="#94031E")

    # Triângulo verde no canto inferior esquerdo
    canvas.create_polygon(0, altura, 0, altura-300, 300, altura, fill=verde, outline=verde)


def componentes_frame1(inp_menu):
    # {=======================Título=========================}
    titulo = FUNCOES_TKINTER.CRIAR_LABEL(frame_1, "Wear\n     Register\n  Lances", 'white', verde_escuro, 'calibri', '50', 'bold')
    #titulo.pack(side='left', fill='x', padx=10)
    #titulo.grid(row=1, column=3, rowspan=2, padx=50, pady=50, sticky='s')
    titulo.grid(row=0, column=3, rowspan=1, padx=5, pady=5, sticky='nsw')
    #titulo.place(relx=0.23, rely=0.05)
    
    # {=======================Imagem IFES=========================}
    img1_pg1 = tk.PhotoImage(file=os.path.join(pasta, "ICONES_FOTOS", "ifes.png"))
    img1_pg1 = img1_pg1.subsample(3,3)

    fotoimg1_pg1 = tk.Label(frame_1,
                            bg = 'white',
                            bd = 0,
                            image = img1_pg1)
    
    #fotoimg1_pg1.pack(side='left', before=titulo, fill='x', padx=10)

    fotoimg1_pg1.grid(row=0, column=1, padx=20, pady=20, sticky='s')
    #fotoimg1_pg1.grid(row=0, column=1, rowspan=1, padx=20, pady=20, sticky='nsw')
    #fotoimg1_pg1.grid(row=1, column=1, rowspan=2, padx=50, pady=50, sticky='nsw')
    #fotoimg1_pg1.place(relx=0.15, rely=0.22, anchor=CENTER)
    
    # {=======================Botões de Cadastro=========================}
    bt_cadastro_lanca = FUNCOES_TKINTER.CRIAR_BOTAO(frame_1,'Cadastrar Bico',verde, bege,3,'38','bold',"hand2",lambda:ABA_CADASTRO_BICO(inp_menu))
    bt_cadastro_lanca.place(relx=0.55, rely=0.44, relwidth=0.4, relheight=0.2)

    bt_cadastro_funcionario = FUNCOES_TKINTER.CRIAR_BOTAO(frame_1,'Cadastrar Usina',verde,bege,3,'38','bold',"hand2",lambda:ABA_CADASTRO_USINA(inp_menu))
    bt_cadastro_funcionario.place(relx=0.55, rely=0.69, relwidth=0.4, relheight=0.2)

    # {=======================Botões de Visualização=========================}
    bt_visualizar_site = FUNCOES_TKINTER.CRIAR_BOTAO(frame_1,'SITE WRL',verde,bege,4,'38','bold',"hand2", lambda:abrir_streamlit())
    bt_visualizar_site.place(relx=0.55, rely=0.19, relwidth=0.4, relheight=0.2)
    
    # {=======================Botão Iniciar Inspeção=========================}
    icone_camera = file=os.path.join(pasta,"ICONES_FOTOS","png_cam.png")
    bt_iniciar_camera = FUNCOES_TKINTER.CRIAR_BOTAO(frame_1,'Iniciar Inspeção',bege,verde,4,'38','bold',"circle", lambda:INICIAR_INSPECAO(inp_menu),inp_imagem=icone_camera, imagem_posicao='bottom')
    bt_iniciar_camera.place(relx=0.07, rely=0.44, relwidth=0.4, relheight=0.45)
    
    # {=======================FECHAR ABA=========================}
    img_fechar = PhotoImage(file=r"C:\Users\20221CECA0402\Documents\GitHub\WRL_\ICONES_FOTOS\fechar.png")
    #C:\Users\20221CECA0402\Documents\GitHub\WRL_\ICONES_FOTOS\fechar.png
     
    bt_fechar_aba_menu = tk.Button(frame_1, image=img_fechar, command=inp_menu.destroy,compound=tk.CENTER, bg="#DE1804", bd=3)
    bt_fechar_aba_menu.place(relx=0.94, rely=0.02, relwidth=0.04, relheight=0.06)
        
    inp_menu.mainloop()

menu_WRL()
print(color.Fore.RED + "Finalizando o código - Tela do Menu" + color.Style.RESET_ALL, "\n")