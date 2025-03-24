import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import json
import random
import os

CAMINHO_JSON = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'perguntas_show_do_milhao.json'))
CAMINHO_LOGO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Logo-Fatec-1200x800-1.jpg'))

with open(CAMINHO_JSON, 'r', encoding='utf-8') as f:
    perguntas = json.load(f)

class ShowDoMilhaoApp:
    def __init__(self, master):
        self.master = master
        master.title("Show do Milhão - Fatec")
        master.geometry("700x500")
        master.configure(bg="#ffffff")

        self.perguntas = perguntas
        self.usadas = []
        self.ajudas = {"dica": 1, "pular": 1, "eliminar": 1}
        self.pontuacao = 0
        self.rodada = 0

        self.frame = tk.Frame(master, bg="#ffffff")
        self.frame.pack(expand=True, fill='both')

        logo = Image.open(CAMINHO_LOGO)
        logo = logo.resize((200, 100), Image.LANCZOS)
        self.logo_fatec = ImageTk.PhotoImage(logo)

        logo_label = tk.Label(self.frame, image=self.logo_fatec, bg="#ffffff")
        logo_label.pack(pady=10)

        tk.Label(self.frame, text="Show do Milhão", font=("Helvetica", 22, "bold"), bg="#ffffff", fg="#333333").pack(pady=10)

        self.start_button = tk.Button(
            self.frame, text="Começar Jogo", font=("Helvetica", 14),
            bg="#A71930", fg="#ffffff", padx=20, pady=10,
            command=self.iniciar_jogo, cursor="hand2"
        )
        self.start_button.pack(pady=20)

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

        tk.Label(
            self.frame, text=f"Pergunta {self.rodada}: {self.pergunta_atual['pergunta']}",
            wraplength=600, font=("Helvetica", 16, "bold"), bg="#ffffff"
        ).pack(pady=20)

        tk.Label(
            self.frame, text=f"Pontuação: {self.pontuacao}", font=("Helvetica", 12), bg="#ffffff", fg="#555555"
        ).pack()

        self.botoes_opcoes = []
        for opcao in self.pergunta_atual['opcoes']:
            btn = tk.Button(
                self.frame, text=opcao, width=60, font=("Helvetica", 12),
                bg="#E0E0E0", fg="#333333", padx=5, pady=5,
                command=lambda o=opcao: self.verificar_resposta(o), cursor="hand2"
            )
            btn.pack(pady=5)
            self.botoes_opcoes.append((btn, opcao))

        ajuda_frame = tk.Frame(self.frame, bg="#ffffff")
        ajuda_frame.pack(pady=20)

        for ajuda in [("Dica", self.usar_dica), ("Pular", self.usar_pular), ("Eliminar Duas", self.usar_eliminar)]:
            tk.Button(
                ajuda_frame, text=ajuda[0], width=15, font=("Helvetica", 10),
                bg="#A71930", fg="#ffffff", padx=5, pady=5,
                command=ajuda[1], cursor="hand2"
            ).pack(side='left', padx=5)

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
            messagebox.showinfo("Aviso", "Você já usou a eliminação.")

    def fim_de_jogo(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        tk.Label(
            self.frame, text=f"Fim de jogo! Sua pontuação foi: {self.pontuacao}",
            font=("Helvetica", 18, "bold"), bg="#ffffff"
        ).pack(pady=20)
        tk.Button(self.frame, text="Jogar Novamente", command=self.reiniciar).pack()

    def reiniciar(self):
        self.frame.destroy()
        self.__init__(self.master)

if __name__ == "__main__":
    root = tk.Tk()
    app = ShowDoMilhaoApp(root)
    root.mainloop()
