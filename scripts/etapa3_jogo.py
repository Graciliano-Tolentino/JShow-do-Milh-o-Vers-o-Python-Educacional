# etapa3_jogo.py (rascunho inicial)

from etapa2_perguntas import carregar_perguntas, sortear_pergunta

def apresentar_pergunta(pergunta_dict, numero):
    print(f"\nPergunta {numero}: {pergunta_dict['pergunta']}")
    for i, opcao in enumerate(pergunta_dict["opcoes"], 1):
        print(f"{i}. {opcao}")
    print("\n[D]ica  |  [P]ular  |  [E]liminar duas  |  [S]air")
    return input("Sua resposta (ou comando): ").strip().lower()
