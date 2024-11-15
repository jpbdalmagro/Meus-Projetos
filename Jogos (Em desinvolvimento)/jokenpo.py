from os import system
from random import choice
from time import sleep

def escolha_jogador(score_jogador, score_pc):
    print("\033[1;93m-\033[m" * 30)
    print("{:^30}".format("Escolha uma opção:"))
    print("\033[1;93m-\033[m" * 30)
    print("{:^30}".format("1 - PEDRA"))
    print("{:^30}".format("2 - PAPEL"))
    print("{:^30}".format("3 - TESOURA"))
    print("\033[1;93m-\033[m" * 30)
    
    while True:
        try:
            print(f"Placar: Jogador {score_jogador} x {score_pc} PC")
            escolha = int(input("Digite o número correspondente a sua escolha: "))
            if escolha in [1, 2, 3, 666]:
                break
            else:
                print("\033[1;91mOpção inválida!\033[m")
        except:
            print("\033[1;91mOpção inválida!\033[m")
    
    if escolha == 1:
        return 'PEDRA'
    elif escolha == 2:
        return 'PAPEL'
    elif escolha == 666:
        return 'flag'
    else:
        return 'TESOURA'
    
def jokenpo(jogador, pc):
    if jogador == pc:
        return "EMPATE"
    elif jogador == 'PEDRA' and pc == 'TESOURA':
        return "JOGADOR"
    elif jogador == 'PAPEL' and pc == 'PEDRA':
        return "JOGADOR"
    elif jogador == 'TESOURA' and pc == 'PAPEL':
        return "JOGADOR"
    else:
        return "PC"
    


def play():
    score_jogador = 0
    score_pc = 0
    while score_jogador < 3 and score_pc < 3:
        
        escolhas = ['PEDRA', 'PAPEL', 'TESOURA']
        escolha_pc = choice(escolhas)
        
        print("Vamos jogar Jokenpo! Quem fizer 3 pontos primeiro vence!")
        print("\033[1;93m-\033[m" * 30)
        
        print("Vou fazer a minha escolha", end=" ")
        sleep(1)
        print("PRONTO!")
        
        
        escolha = escolha_jogador(score_jogador, score_pc)
        
        if escolha == 'flag':
            break
        
        print(f"Você escolheu {escolha}")
        print(f"Eu escolhi {escolha_pc}")
        
        resultado = jokenpo(escolha, escolha_pc)
        if resultado == "EMPATE":
            print("\033[1;93mEMPATE!\033[m")
        elif resultado == "JOGADOR":
            print("\033[1;92mVocê venceu!\033[m")
            score_jogador += 1
        else:
            print("\033[1;91mEu venci!\033[m")
            score_pc += 1

        print(f"Placar: Jogador {score_jogador} x {score_pc} PC")
        print("\033[1;93m-\033[m" * 30)
        sleep(2)
        system('cls')
        
    if score_jogador == 3:
        print("\033[1;92mVocê venceu o jogo!\033[m")
        print(f"Placar: Jogador {score_jogador} x {score_pc} PC")
    elif score_pc == 3:
        print("\033[1;91mEu venci o jogo!\033[m")
        print(f"Placar: Jogador {score_jogador} x {score_pc} PC")
    
    sleep(2)