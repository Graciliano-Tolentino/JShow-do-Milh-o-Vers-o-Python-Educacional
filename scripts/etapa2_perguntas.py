import random
import json
import os

def carregar_perguntas():
    caminho = os.path.join(os.path.dirname(__file__), '..', 'perguntas_show_do_milhao.json')
    with open(caminho, 'r', encoding='utf-8') as f:
        return json.load(f)


# Lista de perguntas (exemplo com 5, depois podemos expandir)

# Função para sortear uma pergunta ainda não utilizada
def sortear_pergunta(perguntas, ja_usadas):
    opcoes_disponiveis = [i for i in range(len(perguntas)) if i not in ja_usadas]
    if not opcoes_disponiveis:
        return None
    escolhida = random.choice(opcoes_disponiveis)
    return escolhida, perguntas[escolhida]

# Teste local
if __name__ == "__main__":
    perguntas = carregar_perguntas()     # Carrega do JSON
    usadas = []                          # Lista de perguntas já sorteadas

    for _ in range(3):                   # Testar 3 sorteios
        resultado = sortear_pergunta(perguntas, usadas)
        if resultado:
            indice, pergunta = resultado
            usadas.append(indice)

            print("\nPergunta:", pergunta["pergunta"])
            for i, opcao in enumerate(pergunta["opcoes"], 1):
                print(f"{i}. {opcao}")
            print("Dica:", pergunta["dica"])
        else:
            print("Não há mais perguntas disponíveis.")
