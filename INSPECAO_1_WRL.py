from tkinter import ttk
import tkinter as tk
from tkinter import messagebox, Canvas
import colorama as color
import FUNCOES_BD
import FUNCOES_TKINTER
from direction import pasta_bd

print("\n\n", color.Fore.GREEN + "Iniciando o código - Registro pre-medição" + color.Style.RESET_ALL)

def tabela(filtro_id=None):

    conn, cursor = FUNCOES_BD.CONECTA_BD(fr'{pasta_bd()}\REGISTROS_WRL.db')
    comando = "SELECT * FROM DADOS_EMPRESAS"
    cursor.execute(comando)
    dados_tabela = cursor.fetchall()
    FUNCOES_BD.DESCONECTA_BD(conn)

    return dados_tabela

def ENTRY_INT(inp_text):
    if inp_text == "": return True
    try:
        value = int(inp_text)
    except ValueError: return False
    
    return 0 <= value <= 100000000000 #Qual a vida máxima geralmente?

def validador(input):
    comando = (input.register(ENTRY_INT), "%P") 
    return comando

def ENTRY_STRING(inp_text):
    return all(char.isalpha() or char.isspace() for char in inp_text) or inp_text == ""

def comandos_botao_continuar(inp_janela, inp_usina_grupo, inp_site, inp_BOF, inp_ID, inp_tipo, inp_furos, inp_vida, inp_usuario, inp_menu): 
    
    conn, cursor = FUNCOES_BD.CONECTA_BD(fr'{pasta_bd()}\REGISTROS_WRL.db')
    comando = f"SELECT * FROM DADOS_EMPRESAS WHERE ID = '{inp_ID.get()}' AND TIPO = '{inp_tipo.get()}' "
    cursor.execute(comando)
    dados = cursor.fetchone()
    FUNCOES_BD.DESCONECTA_BD(conn)

    ultima_vida_registrada = dados[6]
    
    if inp_vida.get() < ultima_vida_registrada:#OBS: deixar de fechar a tela
        messagebox.showwarning("AVISO",f"A vida têm que\nser maior que a\nultima registrada ({ultima_vida_registrada})")
    
    else:
        DADOS_INSERIDOS = []
        
        DADOS_INSERIDOS.append(inp_furos.get())
        DADOS_INSERIDOS.append(inp_usina_grupo.get())
        DADOS_INSERIDOS.append(inp_site.get())
        DADOS_INSERIDOS.append(inp_BOF.get())
        DADOS_INSERIDOS.append(inp_tipo.get())
        DADOS_INSERIDOS.append(inp_ID.get())
        DADOS_INSERIDOS.append(inp_usuario.get().upper())
        DADOS_INSERIDOS.append(inp_vida.get())

        param = 0
        for dado in DADOS_INSERIDOS:
            if dado == '':
                param += 1

        if param > 0:
            messagebox.showwarning("AVISO","Preencha todos os espaços")

        if DADOS_INSERIDOS[-1] == ultima_vida_registrada:
            msg_box = tk.messagebox.askquestion("VIDA EXISTENTE", "Esta já é a ultima vida registrada,\ndeseja continuar mesmo assim?", icon="warning")
           
            if msg_box == "yes":
                from INSPECAO_2_WRL import aba_camera
                janela_cadastro = aba_camera(inp_janela, DADOS_INSERIDOS, inp_menu)
                janela_cadastro.deiconify()

        else:
            from INSPECAO_2_WRL import aba_camera
            janela_cadastro = aba_camera(inp_janela, DADOS_INSERIDOS, inp_menu)
            janela_cadastro.deiconify()
    
def OnClick(event, listaCli, usina, site, BOF, ID, Furos, Tipo):
    selected_items = listaCli.selection()
    if not selected_items:
        return
    
    for n in selected_items:
        col1, col2, col3, col4, col5, col6, col7 = listaCli.item(n, 'values')
        
        usina.delete(0, tk.END)
        site.delete(0, tk.END)
        BOF.delete(0, tk.END)
        ID.delete(0, tk.END)
        Furos.delete(0, tk.END)
        Tipo.delete(0, tk.END)
        
        usina.insert(tk.END, col2)
        site.insert(tk.END, col3)
        BOF.insert(tk.END, col4)
        ID.insert(tk.END, col6)
        Furos.insert(tk.END, col1)
        Tipo.insert(tk.END, col5)
                        
#CORES USADAS
verde = '#416951' #Cor botão
bege = '#C9B783' #Cor botão
marrom = '#68584A' 
verde_escuro = '#1F3422' #Titulos
fundo_branco = 'white' #fundo das letras em frames brancos

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

    inp_janela.title("INICIAR INSPECÇÃO")
    inp_janela.configure(background= fundo_branco)
    inp_janela.attributes("-fullscreen", True)
    
def frames_da_tela(inp_janela): 
        global frame_1
        
        frame_1 = tk.Frame(inp_janela, bg= fundo_branco)
        frame_1.place(relx=0.01, rely=0.02,relwidth=0.98, relheight=0.96)
        
        return frame_1

def componentes_frame1(inp_frame,inp_janela, inp_menu):# #TOPLEVEL
    # {=======================Título=========================}
    titulo = FUNCOES_TKINTER.CRIAR_LABEL(inp_frame, "Selecionar Bico", fundo_branco, verde_escuro, 'arial', '35', 'bold')
    titulo.place(relx=0.5, rely=0.05,anchor='center') 
    
    # {=======================USINA=========================}
    label_usina = FUNCOES_TKINTER.CRIAR_LABEL(inp_frame, "Usina/Grupo: ", fundo_branco, marrom, 'arial', '20', 'bold')
    label_usina.place(relx=0.05, rely=0.15)

    input_usina = tk.Entry(inp_frame, validate= "key",font=("Arial", 20)) # validatecommand="key"
    input_usina.place(relx=0.05, rely=0.2, relwidth=0.3, relheight=0.06)

    # {=======================SITE=========================}
    label_site = FUNCOES_TKINTER.CRIAR_LABEL(inp_frame, "Site: ", fundo_branco, marrom, 'arial', '20', 'bold')
    label_site.place(relx=0.05, rely=0.3)

    input_site = tk.Entry(inp_frame, validate= "key",font=("Arial", 20))
    input_site.place(relx=0.05, rely=0.35, relwidth=0.3, relheight=0.06)

    # {======================= BOF =========================}
    label_BOF = FUNCOES_TKINTER.CRIAR_LABEL(inp_frame, "BOF: ", fundo_branco, marrom, 'arial', '20', 'bold')
    label_BOF.place(relx=0.05, rely=0.45)

    input_BOF = tk.Entry(inp_frame, validate= "key",font=("Arial", 20))
    input_BOF.place(relx=0.05, rely=0.5, relwidth=0.3, relheight=0.06)
    
    # {======================= ID =========================}
    label_ID = FUNCOES_TKINTER.CRIAR_LABEL(inp_frame, "ID: ", fundo_branco, marrom, 'arial', '20', 'bold')
    label_ID.place(relx=0.05, rely=0.6)

    input_ID = tk.Entry(inp_frame, validate= "key",font=("Arial", 20))
    input_ID.place(relx=0.05, rely=0.65, relwidth=0.13, relheight=0.06)
    
    # {======================= FUROS =========================}
    label_Furos = FUNCOES_TKINTER.CRIAR_LABEL(inp_frame, "Furos: ", fundo_branco, marrom, 'arial', '20', 'bold')
    label_Furos.place(relx=0.22, rely=0.6)

    input_Furos = tk.Entry(inp_frame, validate= "key",font=("Arial", 20), validatecommand= validador(inp_frame))
    input_Furos.place(relx=0.22, rely=0.65, relwidth=0.13, relheight=0.06)

    # {======================= TIPO =========================}
    label_tipo = FUNCOES_TKINTER.CRIAR_LABEL(inp_frame, "Tipo: ", fundo_branco, marrom, 'arial', '20', 'bold')
    label_tipo.place(relx=0.05, rely=0.75)

    input_tipo = tk.Entry(inp_frame, validate= "key",font=("Arial", 20))
    input_tipo.place(relx=0.05, rely=0.8, relwidth=0.13, relheight=0.06)
    
    # {======================= VIDA =========================}
    label_vida = FUNCOES_TKINTER.CRIAR_LABEL(inp_frame, "Vida: ", fundo_branco, marrom, 'arial', '20', 'bold')
    label_vida.place(relx=0.22, rely=0.75)

    input_vida = tk.Entry(inp_frame, validate= "key",font=("Arial", 20), validatecommand= validador(inp_frame) )
    input_vida.place(relx=0.22, rely=0.8, relwidth=0.13, relheight=0.06)

    # {======================= Divisória =========================}
    label_divisor = FUNCOES_TKINTER.CRIAR_LABEL(inp_frame, "", bege, marrom, 'arial', '20', 'bold')
    label_divisor.place(relx=0.37, rely=0.15, relwidth=0.005, relheight=0.71)
    
    # {======================= Usuário =========================}
    label_usuario = FUNCOES_TKINTER.CRIAR_LABEL(inp_frame, "Usuário: ", fundo_branco, marrom, 'arial', '20', 'bold')
    label_usuario.place(relx=0.4, rely=0.75)

    input_usuario = tk.Entry(inp_frame, validate= "key",font=("Arial", 20))
    input_usuario.place(relx=0.4, rely=0.8, relwidth=0.55, relheight=0.06)
    
    vcmd = (input_usuario.register(ENTRY_STRING), '%P')
    input_usuario.config(validatecommand=vcmd)

    # {=======================Botão Voltar e Continuar=========================}
    bt_voltar = FUNCOES_TKINTER.CRIAR_BOTAO(inp_frame, "MENU",verde, bege,3,'20','bold',"hand2", lambda: FUNCOES_TKINTER.BOTAO_VOLTAR( inp_menu, inp_janela))# #TOPLEVEL
    bt_voltar.place(relx=0.05, rely=0.9, relwidth=0.13, relheight=0.06)

    bt_continuar = FUNCOES_TKINTER.CRIAR_BOTAO(inp_frame, "PRÓXIMO",verde, bege,3,'20','bold',"hand2",lambda: comandos_botao_continuar(inp_janela,input_usina,input_site,input_BOF,input_ID,input_tipo,input_Furos,input_vida,input_usuario,inp_menu))
    bt_continuar.place(relx=0.82, rely=0.9, relwidth=0.13, relheight=0.06)
    
    # {=======================FECHAR ABA=========================}
    # bt_fechar_aba_menu = tk.Button(inp_frame, text="X", command=inp_janela.destroy, bg="red").place(relx=0.96, rely=0.02, relwidth=0.03, relheight=0.04) #AVISO ->tirar esta linha pro tk.tk

    # {=======================Tabela=========================}
    label_aviso = FUNCOES_TKINTER.CRIAR_LABEL(inp_frame, "Clique sobre a\nlinha desejada", bege, verde, 'calibri', '18', 'bold')
    label_aviso.place(relx=0.8, rely=0.15)
    
    filtrar_ID = tk.Entry(inp_frame, validate="key", font=("Arial", 20), validatecommand=validador(inp_frame))
    filtrar_ID.place(relx=0.4, rely=0.2, relwidth=0.1, relheight=0.06)

    bt_buscar = FUNCOES_TKINTER.CRIAR_BOTAO(inp_frame, "Buscar ID",  bege,verde, 3, '20', "", "hand2", lambda: buscar_id(filtrar_ID.get()))
    bt_buscar.place(relx=0.5, rely=0.2, relwidth=0.13, relheight=0.06)

    def buscar_id(id_filtro):
        Tabela.delete(*Tabela.get_children()) 
        conn, cursor = FUNCOES_BD.CONECTA_BD(fr'{pasta_bd()}\REGISTROS_WRL.db')

        if not id_filtro: 
            comando = "SELECT * FROM DADOS_EMPRESAS"
            cursor.execute(comando)
            dados_tabela = cursor.fetchall()
            FUNCOES_BD.DESCONECTA_BD(conn)

            for dado in dados_tabela:
                Tabela.insert("", tk.END, values=dado)

        else:
            comando = "SELECT * FROM DADOS_EMPRESAS WHERE ID = ?"
            cursor.execute(comando, (id_filtro,))
            dados_filtrados = cursor.fetchall()
            FUNCOES_BD.DESCONECTA_BD(conn)

            if not dados_filtrados:
                messagebox.showwarning("ID Não Encontrado", f"O ID '{id_filtro}' não foi encontrado na base de dados.") 

                comando = "SELECT Grupo, Site, BOF, TIPO, ID, ULTIMA_VIDA FROM DADOS_EMPRESAS"
                cursor.execute(comando)
                dados_tabela = cursor.fetchall()
                FUNCOES_BD.DESCONECTA_BD(conn)
                for dado in dados_tabela:
                    Tabela.insert("", tk.END, values=dado)

            else:
                for dado in dados_filtrados:
                    Tabela.insert("", tk.END, values=dado)

    Tabela = ttk.Treeview(inp_frame, height=10, column=("col1", "col2", "col3", "col4", "col5", "col6", "col7"), style="mystyle.Treeview")

    style = ttk.Style()
    style.configure("Treeview.Heading", font=('Verdana', 12, 'bold'))
    style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Verdana', 11))

    Tabela.column("#0", width=0, stretch=tk.NO)  # Ocultando a primeira coluna
    Tabela.heading("#0", text="")

    Tabela.heading("#1", text="Furos")
    Tabela.heading("#2", text="Grupo")
    Tabela.heading("#3", text="Site")
    Tabela.heading("#4", text="BOF")
    Tabela.heading("#5", text="TIPO")
    Tabela.heading("#6", text="ID")
    Tabela.heading("#7", text="Ult. Vida")

    Tabela.column("#1", width=15, anchor='center')
    Tabela.column("#2", width=150)
    Tabela.column("#3", width=75)
    Tabela.column("#4", width=10, anchor='center')
    Tabela.column("#5", width=15, anchor='center')
    Tabela.column("#6", width=10, anchor='center')
    Tabela.column("#7", width=15, anchor='center')

    for dado in tabela():
        Tabela.insert("", tk.END, values=(dado[0], dado[1], dado[2], dado[3], dado[4], dado[5], dado[6]))

    Tabela.place(relx=0.4, rely=0.29, relwidth=0.55, relheight=0.45)
    scroolLista = tk.Scrollbar(inp_frame, orient='vertical', command=Tabela.yview)
    Tabela.configure(yscrollcommand=scroolLista.set)
    scroolLista.place(relx=0.95, rely=0.29, relwidth=0.01, relheight=0.45)
    Tabela.bind("<ButtonRelease-1>", lambda event: OnClick(event, Tabela, input_usina, input_site, input_BOF, input_ID, input_Furos, input_tipo))  

def aba_cadastro(inp_janela):
    
    janela_dois = tk.Toplevel(inp_janela) #TOPLEVEL
    
    tela(janela_dois)
    adicionar_detalhes(janela_dois)
    frames_da_tela(janela_dois)
    componentes_frame1(frame_1,janela_dois,inp_janela) #TOPLEVEL
    
    inp_janela.withdraw()

    janela_dois.transient(inp_janela) #TOPLEVEL
    janela_dois.focus_force() #TOPLEVEL
    janela_dois.grab_set() #TOPLEVEL

    return janela_dois
    
print(color.Fore.RED + "Finalizando o código - Registro pre-medição" + color.Style.RESET_ALL, "\n")