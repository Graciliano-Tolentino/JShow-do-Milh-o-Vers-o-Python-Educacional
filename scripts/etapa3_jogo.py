
import random
from etapa2_perguntas import carregar_perguntas, sortear_pergunta

# Controle de ajudas
ajudas = {
    "dica": 1,
    "pular": 1,
    "eliminar": 1
}

# Função para apresentar a pergunta e opções
def apresentar_pergunta(pergunta_dict, numero):
    print(f"\nPergunta {numero}: {pergunta_dict['pergunta']}")
    for i, opcao in enumerate(pergunta_dict["opcoes"], 1):
        print(f"{i}. {opcao}")
    print("\n[D]ica  |  [P]ular  |  [E]liminar duas  |  [S]air")
    return input("Sua resposta (ou comando): ").strip().lower()

# Função para eliminar duas opções erradas
def eliminar_duas(pergunta_dict):
    correta = pergunta_dict["resposta"]
    opcoes = pergunta_dict["opcoes"]
    erradas = [op for op in opcoes if op != correta]
    eliminadas = random.sample(erradas, 2)
    print("Duas alternativas incorretas foram eliminadas:")
    for op in opcoes:
        if op not in eliminadas:
            print(f"- {op}")

# Função principal do jogo
def jogar():
    perguntas = carregar_perguntas()
    usadas = []
    pontuacao = 0
    rodada = 1

    while rodada <= 10:
        resultado = sortear_pergunta(perguntas, usadas)
        if not resultado:
            print("Todas as perguntas foram utilizadas.")
            break

        indice, pergunta = resultado
        usadas.append(indice)

        while True:
            resposta = apresentar_pergunta(pergunta, rodada)

            if resposta == "d":
                if ajudas["dica"] > 0:
                    print(f"Dica: {pergunta['dica']}")
                    ajudas["dica"] -= 1
                else:
                    print("Você já usou sua dica.")
            elif resposta == "p":
                if ajudas["pular"] > 0:
                    print("Pergunta pulada.")
                    ajudas["pular"] -= 1
                    break
                else:
                    print("Você já usou o pulo.")
            elif resposta == "e":
                if ajudas["eliminar"] > 0:
                    eliminar_duas(pergunta)
                    ajudas["eliminar"] -= 1
                else:
                    print("Você já usou a eliminação.")
            elif resposta == "s":
                print("Você escolheu encerrar o jogo.")
                print(f"Sua pontuação final foi: {pontuacao}")
                return
            elif resposta.isdigit() and int(resposta) in range(1, 5):
                escolha = pergunta["opcoes"][int(resposta)-1]
                if escolha == pergunta["resposta"]:
                    print("Resposta correta!")
                    pontuacao += 10
                else:
                    print(f"Errado! A resposta correta era: {pergunta['resposta']}")
                rodada += 1
                break
            else:
                print("Entrada inválida. Tente novamente.")

    print(f"Fim de jogo! Sua pontuação final foi: {pontuacao}")
