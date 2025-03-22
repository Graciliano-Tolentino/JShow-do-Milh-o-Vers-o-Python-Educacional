import tkinter as tk
from tkinter import messagebox
import json
import random
import os

# Caminho para o JSON

CAMINHO_JSON = os.path.join(os.path.dirname(__file__), '..', 'perguntas_show_do_milhao.json')


# Carregar perguntas
with open(CAMINHO_JSON, 'r', encoding='utf-8') as f:
    perguntas = json.load(f)

class ShowDoMilhaoApp:
    def __init__(self, master):
        self.master = master
        master.title("Show do Milhão - Python Educacional")
        master.geometry("600x400")

        self.perguntas = perguntas
        self.usadas = []
        self.ajudas = {"dica": 1, "pular": 1, "eliminar": 1}
        self.pontuacao = 0
        self.rodada = 0

        self.frame = tk.Frame(master)
        self.frame.pack(expand=True)

        self.label = tk.Label(self.frame, text="Show do Milhão", font=("Helvetica", 18))
        self.label.pack(pady=20)

        self.start_button = tk.Button(self.frame, text="Começar Jogo", command=self.iniciar_jogo)
        self.start_button.pack()

    def iniciar_jogo(self):
        self.start_button.destroy()
        self.nova_pergunta()

    def nova_pergunta(self):
        if self.rodada >= 10:
            self.fim_de_jogo()
            return

        indices_disponiveis = [i for i in range(len(self.perguntas)) if i not in self.usadas]
        if not indices_disponiveis:
            messagebox.showinfo("Fim", "Acabaram as perguntas.")
            return

        self.rodada += 1
        self.indice_atual = random.choice(indices_disponiveis)
        self.pergunta_atual = self.perguntas[self.indice_atual]
        self.usadas.append(self.indice_atual)

        for widget in self.frame.winfo_children():
            widget.destroy()

        tk.Label(self.frame, text=f"Pergunta {self.rodada}: {self.pergunta_atual['pergunta']}", wraplength=500).pack(pady=10)

  

                self.botoes_opcoes = []  # Guardar os botões para manipular depois

        for i, opcao in enumerate(self.pergunta_atual['opcoes']):
            btn = tk.Button(self.frame, text=opcao, width=50,
                            command=lambda o=opcao: self.verificar_resposta(o))
            btn.pack(pady=2)
            self.botoes_opcoes.append((btn, opcao))



# Criar um sub-frame apenas para os botões de ajuda
ajuda_frame = tk.Frame(self.frame)
ajuda_frame.pack(pady=20)

tk.Button(ajuda_frame, text="Dica", width=15, command=self.usar_dica).pack(side='left', padx=10)
tk.Button(ajuda_frame, text="Pular", width=15, command=self.usar_pular).pack(side='left', padx=10)
tk.Button(ajuda_frame, text="Eliminar Duas", width=15, command=self.usar_eliminar).pack(side='left', padx=10)


    def verificar_resposta(self, opcao):
        if opcao == self.pergunta_atual['resposta']:
            self.pontuacao += 10
            messagebox.showinfo("Correto!", "Você acertou!")
        else:
            messagebox.showinfo("Errado!", f"A resposta correta era: {self.pergunta_atual['resposta']}")
        self.nova_pergunta()

    def usar_dica(self):
        if self.ajudas['dica'] > 0:
            messagebox.showinfo("Dica", self.pergunta_atual['dica'])
            self.ajudas['dica'] -= 1
        else:
            messagebox.showinfo("Aviso", "Você já usou sua dica.")

    def usar_pular(self):
        if self.ajudas['pular'] > 0:
            self.ajudas['pular'] -= 1
            self.nova_pergunta()
        else:
            messagebox.showinfo("Aviso", "Você já usou seu pulo.")

    def usar_eliminar(self):
    if self.ajudas['eliminar'] > 0:
        self.ajudas['eliminar'] -= 1

        corretas = self.pergunta_atual['resposta']
        erradas = [op for op in self.pergunta_atual['opcoes'] if op != corretas]
        eliminadas = random.sample(erradas, 2)

        for btn, texto in self.botoes_opcoes:
            if texto in eliminadas:
                btn.config(state='disabled', text="(Eliminada)", fg='gray')
    else:
        messagebox.showinfo(\"Aviso\", \"Você já usou a eliminação.\")


    def fim_de_jogo(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        tk.Label(self.frame, text=f"Fim de jogo! Sua pontuação foi: {self.pontuacao}", font=("Helvetica", 16)).pack(pady=20)
        tk.Button(self.frame, text="Jogar Novamente", command=self.reiniciar).pack()

    def reiniciar(self):
        self.perguntas = perguntas
        self.usadas = []
        self.ajudas = {"dica": 1, "pular": 1, "eliminar": 1}
        self.pontuacao = 0
        self.rodada = 0
        self.nova_pergunta()

if __name__ == "__main__":
    root = tk.Tk()
    app = ShowDoMilhaoApp(root)
    root.mainloop()
