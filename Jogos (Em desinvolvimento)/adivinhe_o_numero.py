from random import randint
from os import system
from time import sleep

def choose_dificulty() -> int:
    while True:
        print("\033[1;93m-\033[m" * 30)
        print("{:^30}".format("Escolha a dificuldade"))
        print("\033[1;93m-\033[m" * 30)
        print("{:^30}".format("1 - Fácil"))
        print("{:^30}".format("2 - Médio"))
        print("{:^30}".format("3 - Difícil"))
        print("\033[1;93m-\033[m" * 30)
        dificuldade = input("Escolha uma opção: ")

        if dificuldade in ["1", "2", "3"]:
            return int(dificuldade)
        else:
            system("cls")
            print("\033[1;31mOpção inválida. Tente novamente.\n\033[m")
            sleep(0.5)
            continue

def chose_number(max: int, min: int) -> int:
    try:
        tentativa = int(input("Tente adivinhar o número entre {} e {}: ".format(min, max)))
    except ValueError:
        print("\033[1;31mDigite um número inteiro.\033[m")
        sleep(0.5)
        return chose_number(max, min)
    else:
        return tentativa

def play(dificuldade: int) -> None:
    tentativas = 0
    
    if dificuldade == 1:
        maximo = 10
    elif dificuldade == 2:
        maximo = 50
    elif dificuldade == 3:
        maximo = 100
    
    menor = 1
    maior = maximo
    
    numero = randint(1, maximo)
    
    while True: #faca as mensagens de acerto verde
        tentativa = chose_number(maximo, menor)
        tentativas += 1
        
        if tentativa == numero:
            print("\033[1;32mParabéns! Você acertou!\033[m")
            print(f"Você acertou em {tentativas} tentativas.")
            break
        elif tentativa < numero:
            print("Tente um número maior.")
        elif tentativa > numero:
            print("Tente um número menor.")
        sleep(0.5)
