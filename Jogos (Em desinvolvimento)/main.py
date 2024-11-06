from os import system
from time import sleep

import menus

def main():
    while True:
        opcao = menus.main_menu()
        
        match(opcao):
            case "1":
                system("cls")
                menus.forca_menu()
            case "2":
                system("cls")
                menus.adivinhe_numero_menu()
            case "3":
                system("cls")
                menus.adivinhe_palavra_menu()
            case "4":
                system("cls")
                menus.jokenpo_menu()
            case "5":
                print("Obrigado por jogar!")
                sleep(1)
                break

if __name__ == "__main__":
    main()