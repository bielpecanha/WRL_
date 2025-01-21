import threading
import tkinter as tk
from tkinter import ttk, messagebox, PhotoImage, Canvas
from customtkinter import *

class Splash(tk.Toplevel):
    def __init__(self, parent, callback):
        """
        Inicializa a janela de splash.

        :param parent: Janela pai (geralmente a janela principal).
        :param callback: Função a ser executada enquanto a barra de progresso carrega.
        """
        super().__init__(parent)
        self.title("Carregando...")

        self.geometry("1280x720")
        self.parent = parent
        self.callback = callback
        self.progress_value = 0
        self.overrideredirect(1)
        self.attributes("-alpha",0.5)

        # Barra de progresso
        self.progress = ttk.Progressbar(self, orient="horizontal", length=300, mode="determinate", maximum=100)
        self.progress.pack(expand=True,pady=50)

        # Inicia a thread para o carregamento
        self.start_loading()

    def start_loading(self):
        """Inicia o processo de carregamento em uma thread separada."""
        # Cria a thread para executar o callback
        self.thread = threading.Thread(target=self.run_task)
        self.thread.start()

        # Atualiza a barra de progresso
        self.update_loading_progress()

    def run_task(self):
        """Executa a função de callback enquanto atualiza a barra de progresso."""
        try:
            self.callback()  # Executa o código pesado
        except Exception as e:
            print(f"Erro durante o carregamento: {e}")

    def update_loading_progress(self):
        """Atualiza a barra de progresso na interface gráfica."""
        if self.thread.is_alive():

            self.progress_value = (self.progress_value + 1) % 101  # Incrementa progressivamente
            self.progress['value'] = self.progress_value
            self.after(50, self.update_loading_progress)

        else:
            self.progress['value'] = 100
            self.after(1000, self.destroy)  # Fecha a janela após 1 segundo

    def destroy_window(self):
        self.destroy

    '''tempo_inicial = time.time()
    tempo_decorrido = tempo_fim - tempo_inicial
    print(f"Tempo de execução: {tempo_decorrido:.4f} segundos")
    tempo_fim = time.time()
    tempo_decorrido = tempo_fim - tempo_inicial
    print(f"Tempo de execução: {tempo_decorrido:.4f} segundos")'''