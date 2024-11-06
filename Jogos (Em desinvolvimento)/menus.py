from os import system
from time import sleep

import forca, adivinhe_o_numero, adivinhe_a_palavra

def main_menu() -> str:
    while True:
        print("\033[1;93m-\033[m" * 30)
        print("{:^30}".format("1 - Jogo da Forca"))
        print("{:^30}".format("2 - Adivinhe o número"))
        print("{:^30}".format("3 - Adivinhe a Palavra"))
        print("{:^30}".format("4 - JoKenPo"))
        print("{:^30}".format("5 - Sair"))
        print("\033[1;93m-\033[m" * 30)
        opcao = input("Escolha uma opção: ")
        
        if opcao in ["1", "2", "3", "4", "5"]:
            return opcao
        else:
            system("cls")
            print("\033[1;31mOpção inválida. Tente novamente.\n\033[m")
            sleep(0.5)
            continue

def play_again_menu() -> str:
    print("\033[1;93m-\033[m" * 30)
    print("{:^30}".format("1 - Jogar novamente"))
    print("{:^30}".format("2 - Voltar"))
    print("\033[1;93m-\033[m" * 30)
    opcao = input("Escolha uma opção: ")
    
    if opcao in ["1", "2"]:
        system("cls")
        return opcao
    else:
        system("cls")
        print("\033[1;31mOpção inválida. Tente novamente.\n\033[m")
        sleep(0.5)
        return play_again_menu()
    
def forca_menu() -> None:
    while True:
        print("{:^30}".format("Jogo da Forca"))
        print("\033[1;93m-\033[m" * 30)
        print("{:^30}".format("1 - Jogar"))
        print("{:^30}".format("2 - Ver classes"))
        print("{:^30}".format("3 - Voltar"))
        print("\033[1;93m-\033[m" * 30)
        opcao = input("Escolha uma opção: ")
        
        if opcao in ["1", "2", "3"]:
            if opcao == "1":
                system("cls")
                classe = forca.choose_class()
                system("cls")
                forca.play(classe)
                if play_again_menu() == '2':
                    break
                continue
            elif opcao == "2":
                forca.show_class()
                continue
            elif opcao == "3":
                break
        else:
            system("cls")
            print("\033[1;31mOpção inválida. Tente novamente.\n\033[m")
            sleep(0.5)
            continue  

def adivinhe_numero_menu() -> str:
    while True:
        print("{:^30}".format("Adivinhe o Número"))
        print("\033[1;93m-\033[m" * 30)
        print("{:^30}".format("1 - Jogar"))
        print("{:^30}".format("2 - Voltar"))
        print("\033[1;93m-\033[m" * 30)
        opcao = input("Escolha uma opção: ")
        
        if opcao in ["1", "2"]:
            if opcao == "1":
                system("cls")
                dificuldade = adivinhe_o_numero.choose_dificulty()
                system("cls")
                adivinhe_o_numero.play(dificuldade)
                if play_again_menu() == '2':
                    break
            if opcao == "2":
                break
            continue
        
        else:
            system("cls")
            print("\033[1;31mOpção inválida. Tente novamente.\n\033[m")
            sleep(0.5)
            continue
        
def adivinhe_palavra_menu() -> None:
    while True:
        print("{:^30}".format("Adivinhe a Palavra"))
        print("\033[1;93m-\033[m" * 30)
        print("{:^30}".format("1 - Jogar"))
        print("{:^30}".format("2 - Voltar"))
        print("\033[1;93m-\033[m" * 30)
        opcao = input("Escolha uma opção: ")
        
        if opcao in ["1", "2"]:
            if opcao == "1":
                system("cls")
                adivinhe_a_palavra.play()
                system("cls")
                if play_again_menu() == '2':
                    break
                continue
            elif opcao == "2":
                break
        else:
            system("cls")
            print("\033[1;31mOpção inválida. Tente novamente.\n\033[m")
            sleep(0.5)
            continue
        
def jokenpo_menu() -> None:
    while True:
        print("{:^30}".format("JoKenPo"))
        print("\033[1;93m-\033[m" * 30)
        print("{:^30}".format("Em desenvolvimento"))
        print("\033[1;93m-\033[m" * 30)
        print("Voltando ao menu principal...")
        sleep(2)
        system("cls")
        break