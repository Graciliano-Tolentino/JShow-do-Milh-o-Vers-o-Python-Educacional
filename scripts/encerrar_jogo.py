def mostrar_resultado_final(pontuacao):
    print("\n" + "="*50)
    print("          FIM DE JOGO - RESULTADO FINAL")
    print("="*50)
    print(f"Sua pontuação final foi: {pontuacao}")
    print()

    if pontuacao == 100:
        print("Parabéns! Você acertou todas as perguntas. Excelente desempenho!")
    elif pontuacao >= 70:
        print("Muito bom! Você demonstrou ótimo domínio dos conteúdos.")
    elif pontuacao >= 40:
        print("Bom esforço! Ainda dá para melhorar com mais prática.")
    else:
        print("Não desanime! Use esse resultado como ponto de partida para evoluir.")

    print("\nDeseja jogar novamente?")
    print("[S]im  |  [N]ão")

    return input("Escolha: ").strip().lower()
