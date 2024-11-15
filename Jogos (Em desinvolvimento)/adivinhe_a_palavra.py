import json
import random
from os import system
from time import sleep

def choose_word() -> str:
    escolha = input("Escolha uma palavra: ")
    if escolha.isalpha():
        return escolha.lower()
    else:
        system("cls")
        print("\033[1;31mPalavra inválida. Tente novamente.\n\033[m")
        sleep(0.5)
        return choose_word()
    
def play():
    tentativas = 0
    dicas = []
    dica = ''
    
    with open('D:\Meus-Projetos\Jogos (Em desinvolvimento)\palavras_adivinhe.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    palavra = random.choice(list(data.keys()))
    palavra = palavra.lower()

    while True:
        while True:
            dica = random.choice(data[palavra])
            if dica not in dicas:
                dicas.append(dica)
                break
            else:
                continue
        print(f"Dica: {dica}")    
        print(f"A palavra tem {len(palavra)} letras.")
        print("-" * 30)
        
        tentativa = choose_word()
        tentativas += 1
        
        if tentativa == palavra:
            print(f"\033[1;32mParabéns! Você acertou a palavra\033[1;33m '{palavra.upper()}'\033[m com {tentativas} tentativas.")
            sleep(2)
            break
        else:
            print("\033[1;31mVocê errou. Tente novamente.\n\033[m")
            sleep(1)
            system("cls")
            continue
        