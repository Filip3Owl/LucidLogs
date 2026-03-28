import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
import sys

# Importa as funções do nosso script principal
try:
    from analisador_logs import analisar_log, gerar_relatorio
except ImportError:
    print("Erro: O arquivo 'analisador_logs.py' precisa estar na mesma pasta.")
    sys.exit(1)

class AnalisadorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("LogLens - Extrator de Logs")
        self.master.geometry("500x300")
        self.master.resizable(False, False)
        
        # Variáveis para armazenar os caminhos
        self.caminho_log = None
        self.caminho_saida = None

        self.criar_widgets()

    def criar_widgets(self):
        # Título
        lbl_titulo = tk.Label(self.master, text="📊 Analisador de Logs", font=("Arial", 16, "bold"))
        lbl_titulo.pack(pady=15)

        # Seção: Selecionar Arquivo de Entrada
        frame_entrada = tk.Frame(self.master)
        frame_entrada.pack(fill="x", padx=20, pady=5)
        
        btn_selecionar_log = tk.Button(frame_entrada, text="1. Selecionar Log", width=20, command=self.selecionar_log)
        btn_selecionar_log.pack(side="left")
        
        self.lbl_log_selecionado = tk.Label(frame_entrada, text="Nenhum arquivo selecionado", fg="gray")
        self.lbl_log_selecionado.pack(side="left", padx=10)

        # Seção: Selecionar Pasta de Saída
        frame_saida = tk.Frame(self.master)
        frame_saida.pack(fill="x", padx=20, pady=15)
        
        btn_selecionar_saida = tk.Button(frame_saida, text="2. Onde Salvar Relatório", width=20, command=self.selecionar_saida)
        btn_selecionar_saida.pack(side="left")
        
        self.lbl_saida_selecionada = tk.Label(frame_saida, text="Nenhum destino selecionado", fg="gray")
        self.lbl_saida_selecionada.pack(side="left", padx=10)

        # Botão de Ação Principal
        self.btn_analisar = tk.Button(self.master, text="🚀 Analisar e Gerar Relatório", font=("Arial", 12, "bold"), 
                                      bg="#4CAF50", fg="black", state="disabled", command=self.executar_analise)
        self.btn_analisar.pack(pady=30, ipadx=10, ipady=5)

    def selecionar_log(self):
        arquivo = filedialog.askopenfilename(
            title="Selecione o arquivo de log",
            filetypes=(("Arquivos de Log", "*.log"), ("Arquivos de Texto", "*.txt"), ("Todos os Arquivos", "*.*"))
        )
        if arquivo:
            self.caminho_log = Path(arquivo)
            # Mostra apenas o nome do arquivo na interface para não poluir
            self.lbl_log_selecionado.config(text=self.caminho_log.name, fg="black")
            self.verificar_prontidao()

    def selecionar_saida(self):
        pasta = filedialog.askdirectory(title="Selecione a pasta para salvar o relatório")
        if pasta:
            # Define que o relatório será salvo na pasta escolhida com este nome
            self.caminho_saida = Path(pasta) / "relatorio_erros.txt"
            self.lbl_saida_selecionada.config(text=f".../{self.caminho_saida.parent.name}/{self.caminho_saida.name}", fg="black")
            self.verificar_prontidao()

    def verificar_prontidao(self):
        """Habilita o botão de analisar apenas se entrada e saída foram escolhidas."""
        if self.caminho_log and self.caminho_saida:
            self.btn_analisar.config(state="normal")

    def executar_analise(self):
        try:
            # Reutilizando a lógica do nosso script principal!
            contagem, erros = analisar_log(self.caminho_log)
            gerar_relatorio(self.caminho_saida, contagem, erros)
            
            messagebox.showinfo("Sucesso!", f"Análise concluída com sucesso!\n\nRelatório salvo em:\n{self.caminho_saida}")
            
            # Limpa a interface após o sucesso
            self.caminho_log = None
            self.caminho_saida = None
            self.lbl_log_selecionado.config(text="Nenhum arquivo selecionado", fg="gray")
            self.lbl_saida_selecionada.config(text="Nenhum destino selecionado", fg="gray")
            self.btn_analisar.config(state="disabled")

        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro durante a análise:\n{str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AnalisadorGUI(root)
    root.mainloop()