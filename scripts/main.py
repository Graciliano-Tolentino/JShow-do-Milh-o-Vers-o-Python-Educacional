
from scripts.etapa1_intro import exibir_menu
from scripts.etapa3_jogo import jogar
from scripts.encerrar_jogo import mostrar_resultado_final

def iniciar_jogo():
    while True:
        exibir_menu()
        pontuacao = jogar()
        escolha = mostrar_resultado_final(pontuacao)
        if escolha != "s":
            print("Obrigado por jogar! Até a próxima.")
            break

if __name__ == "__main__":
    iniciar_jogo()
