import random
import json
from os import system
from time import sleep

def show_class() -> None:
    system("cls")
    print("\033[1;93m-\033[m" * 30)
    print("{:^30}".format("Classes"))
    print("\033[1;93m-\033[m" * 30)
    print("{:^30}".format("1 - Animais"))
    print("{:^30}".format("2 - Cores"))
    print("{:^30}".format("3 - Frutas"))
    print("{:^30}".format("4 - TI"))
    print("\033[1;93m-\033[m" * 30)
    sair = input("Pressione ENTER para sair")

def choose_class() -> int:
    while True:
        print("\033[1;93m-\033[m" * 30)
        print("{:^30}".format("Defina a classe"))
        print("\033[1;93m-\033[m" * 30)
        print("{:^30}".format("1 - Animais"))
        print("{:^30}".format("2 - Cores"))
        print("{:^30}".format("3 - Frutas"))
        print("{:^30}".format("4 - TI"))
        print("\033[1;93m-\033[m" * 30)
        classe = input("Escolha uma opção: ")

        if classe in ["1", "2", "3", "4"]:
            print("Você escolheu a classe: ", classe)
            return int(classe)
        else:
            system("cls")
            print("\033[1;31mOpção inválida. Tente novamente.\n\033[m")
            sleep(0.5)
            continue

def choose_letter() -> str:
    letra = input("Escolha uma letra: ")
    if letra.isalpha() and len(letra) == 1:
        return letra.upper()
    else:
        print("\033[1;31mDigite apenas uma letra.\n\033[m")
        sleep(0.5)
        return choose_letter()

def play(classe: int) -> None:
    classes = ['animais', 'cores', 'frutas', 'TI']
    tentativas = []
    erros = 0

    with open("D:\Meus-Projetos\Jogos (Em desinvolvimento)\palavras_forca.json", "r") as file:
        palavras = json.load(file)
        palavras_jogo = palavras[classes[classe - 1]]
        
    palavra = random.choice(palavras_jogo)
    palavra = palavra.upper()

    while True:
        print("Você escolheu a classe: ", classes[int(classe) - 1])
        print("\033[1;90m-\033[m" * 30)
        print("Palavra: ", end="")
        
        for letra in palavra:
            if letra in tentativas:
                print(letra, end=" ")
            else:
                print("_", end=" ")

        print("")
        print("\033[1;90m-\033[m" * 30)
        
        if erros > 0:
            print(f"Número de erros: {erros}")
            
        if tentativas:
            print("Letras utilizadas: ", end="")
            for letra in tentativas:
                print(letra, end=" ")
            print("")    
        
        escolha = choose_letter()
        
        if escolha in tentativas:
            print("\033[1;31mVocê já escolheu essa letra. Tente novamente.\n\033[m")
            sleep(1)
            system("cls")
            continue
        else:
            tentativas.append(escolha)
            
            if escolha in palavra:
                print("\033[1;32mVocê acertou!\n\033[m")
                sleep(1)
            else:
                print("\033[1;31mVocê errou!\n\033[m")
                erros += 1
                sleep(1)
                
        system("cls")

        if all(letra in tentativas for letra in palavra):
            print("\033[1;32mParabéns! Você acertou a palavra:\033[1;33m {}\033[m".format(palavra))
            print("Você errou {} vez(es).".format(erros))
            sleep(2)
            break
            
        if erros == 10:
            print("\033[1;31mVocê perdeu! A palavra era: {}\n\033[m".format(palavra))
            sleep(2)
            break
