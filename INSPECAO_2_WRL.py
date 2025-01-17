import tkinter as tk
import colorama as color
import cv2
from tkinter.constants import *
from tkinter import Canvas
from customtkinter import *
from PIL import Image, ImageTk
from ultralytics import YOLO
import keyboard
import FUNCOES_TKINTER
import FUNCOES_CAMERA_WRL as fun2 #Funcções para camêra
from FUNCOES_CAMERA_WRL import DepthCamera
import numpy as np
from INSPECAO_3_WRL import aba_dados
from direction import folder
import sys

print("\n\n", color.Fore.GREEN + "Iniciando o código - Tela da câmera" + color.Style.RESET_ALL)
pasta = folder()

#CORES USADAS
verde = '#416951' #Cor botão
bege = '#C9B783' #Cor botão
marrom = '#68584A' 
verde_escuro = '#1F3422' #Titulos
fundo_branco = 'white' #fundo das letras em frames brancos

model = YOLO(fr'{pasta}\pesos\best.pt')

# # Define a classe 
# Initialize the DepthCamera
# Define global variables for storing the results

global nome_arquivo, caminho_fotoBW, caminho_fotoColorida, nome_arquivo_BW, stop
nome_arquivo = caminho_fotoBW = caminho_fotoColorida = nome_arquivo_BW = None
stop = False
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

def tela(inp_janela):
    inp_janela.title("Camêra WRL")
    inp_janela.configure(background=fundo_branco)
    inp_janela.attributes("-fullscreen", True)
    
def frames_da_tela(inp_janela):
    global frame_um, frame_dois
    
    frame_um = tk.Frame(inp_janela, bd=2, bg=fundo_branco, highlightbackground='#668B8B', highlightthickness=1)
    frame_um.place(relx=0.72, rely=0.02, relwidth=0.27, relheight=0.96)
    
    frame_dois = tk.Frame(inp_janela, bd=2, bg=fundo_branco, highlightbackground='#668B8B', highlightthickness=1)
    frame_dois.place(relx=0.01, rely=0.02, relwidth=0.7, relheight=0.96)
    
    return frame_um, frame_dois

def componentes_frame1(inp_frame,inp_janela, inp_menu, dc):
    bt_voltar = FUNCOES_TKINTER.CRIAR_BOTAO(inp_frame, "Voltar",verde, bege,3,'15','bold',"hand2", lambda: (dc.release(), FUNCOES_TKINTER.BOTAO_VOLTAR(inp_menu, inp_janela))) # #TOPLEVEL
    bt_voltar.place(relx=0.05, rely=0.88, relwidth=0.2, relheight=0.08)
    
    #OBS: por a opção de clicar aqui e tirar a foto
    btfoto_pg2 = tk.Button(inp_frame, text='CTRL', relief="ridge", cursor="circle", bd=4, bg='#545454', fg='white', font=("arial", 13))
    btfoto_pg2.place(relx=0.5, rely=0.93, anchor=CENTER)

def componentes_frame2(inp_frame, lista_dados_inspecao, dc):
    
    global nome_arquivo, caminho_fotoBW, caminho_fotoColorida, nome_arquivo_BW, stop

    borda = tk.Label(inp_frame, bg="white")
    borda.place(relx=0, rely=0, relwidth=1, relheight=1)

    def exibir_video():
    
        global nome_arquivo, caminho_fotoBW, caminho_fotoColorida, nome_arquivo_BW, stop, lista_APP, qtd_furos, Abertura, infra_image, centro, depth_frame
        
        ret, color_image, infra_image = dc.get_simple_frame()
    
        back_frame = fun2.sobrepor_molde(infra_image)
        
        lista_APP, id_bico, qtd_furos = fun2.organizar_dados_app(lista_dados_inspecao)
        
        stop = False

        if ret:
            frame = cv2.cvtColor(back_frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            altura = borda.winfo_height()
            largura = borda.winfo_width()
            img = img.resize((largura, altura))
            image = ImageTk.PhotoImage(image=img)
            borda.configure(image=image)
            borda.image = image
            centro = fun2.definir_centro(altura, largura)
            if keyboard.is_pressed('ctrl') or keyboard.is_pressed('right control') or keyboard.is_pressed('q'):
                ret, depth_frame, color_frame, infra_image, Abertura = dc.get_frame()
                nome_arquivo, caminho_fotoBW, caminho_fotoColorida, nome_arquivo_BW = fun2.tirar_foto(color_frame, infra_image, id_bico)
                stop = True
                dc.release()
                return
            ret, color_image, infra_image = dc.get_simple_frame()
        if not stop:
            borda.after(10, exibir_video)

    exibir_video()
    

def aba_camera(inp_janela, dados, inp_menu):#OBS: envez de usar 'dados' por o nome dsa variavel de forma intuitiva
    global nome_arquivo, caminho_fotoBW, caminho_fotoColorida, nome_arquivo_BW, stop, lista_APP, qtd_furos, Abertura, infra_image, centro
    
    lista_dados_inspecao = dados
    janela_tres = tk.Toplevel()
    
    dc = DepthCamera()

    tela(janela_tres)
    adicionar_detalhes(janela_tres)
    frames_da_tela(janela_tres)
    componentes_frame1(frame_um,janela_tres, inp_janela, dc)
    componentes_frame2(frame_dois, lista_dados_inspecao, dc)

    janela_tres.focus_force() #TOPLEVEL
    janela_tres.grab_set() #TOPLEVEL

    inp_janela.withdraw()

    stop = False
    def aba_camera2():
        # Esperar até que a variável `stop` seja definida como True

        while not stop:    
            janela_tres.update_idletasks()
            janela_tres.update()

        janela_tres.destroy()

        return nome_arquivo, caminho_fotoBW, caminho_fotoColorida, nome_arquivo_BW, lista_APP, qtd_furos, Abertura, infra_image, centro

    nome_arquivo, caminho_fotoBW, caminho_fotoColorida, nome_arquivo_BW, lista_APP, qtd_furos, Abertura, infra_image, centro = aba_camera2()
    
    inp_janela.deiconify()

    """Remerson meu amigo eu, agora temos que verificar a demora no momento de reabrir a tela que foi fechada enquanto se executava a ABA CAMERA,
    pensei em colocar uma tela de carregamento tambem, e hoje (amanha) é dia de fazer uma tela mais bonitinha tbm, essa barra de carregamento
    tosca nao da né pai, foco no progresso"""



    #Depth_Frame = fun2.obter_depth_frame(dc)
    lista_dh = fun2.extrair_data_e_hora(nome_arquivo[0])
    
    lista_diametros, mascaras, resultados = fun2.analisar_imagem(model, cv2.imread(caminho_fotoBW), nome_arquivo[0], depth_frame, Abertura)
    caixas_detectadas, nomes_classes = fun2.extrair_dados(resultados, mascaras, nome_arquivo_BW)
 
    # Extrair coordenadas e centro das caixas delimitadoras
    lista_pontos = fun2.extrair_coordenadas_centro(caixas_detectadas, nomes_classes)
    # Filtrar o ponto central se detectado como furo
    lista_pontos = fun2.filtrar_ponto_central(lista_pontos, centro)
    fun2.enumerar_furos(lista_pontos, qtd_furos, cv2.imread(caminho_fotoBW), nome_arquivo[0])


    for dado in lista_dh:
        nome_arquivo.append(dado)

    print("\n(insp_2)LISTA APP",lista_APP,"\nNOME ARQUIVO",nome_arquivo, "\nLISTA DIAMETROS", lista_diametros)
    lista_completa = fun2.reunir_dados(lista_APP, nome_arquivo, lista_diametros)
    
    ## SITE ##
    estados = fun2.identificar_estados(lista_completa)
    estado_bico = fun2.estado_geral_bico(estados)
    fun2.salvar_registros_desgaste(lista_completa, estados, lista_diametros, estado_bico)
    ##########

    fun2.salvar_registros(lista_completa, qtd_furos)

    janela_cadastro = aba_dados(inp_janela, dados[5], dados[4], nome_arquivo[0],inp_menu,inp_janela )
    janela_cadastro.deiconify()


    return janela_tres

print(color.Fore.RED + "Finalizando o código - Tela da câmera" + color.Style.RESET_ALL, "\n")