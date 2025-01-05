from classes import *
import json
import os 

def menu():
    print("""\nSelecione a opção desejada:
1 - Fazer pedido
2 - Cadastrar cliente
3 - Cadastrar prato
4 - Listar clientes
5 - Listar pratos
6 - Listar pedidos
7 - Alterar cliente
8 - Alterar prato
9 - Fechar caixa
0 - Sair
""")    

    while True:
        opcao = input("Digite a opção desejada: ")
        if opcao in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            return opcao
        else:
            print("Opção inválida")


def cadastrar_cliente(clientes):
    print("Cadastro de cliente")
    print("Preencha os dados abaixo")
    
    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    for i in clientes:
        if i.cpf == cpf:
            print("Cliente já cadastrado")
            return
        
    while True:    
        telefone = input("Digite o telefone do cliente: ")
        for i in clientes:
            if i.telefone == telefone:
                print("Telefone já cadastrado")
                return    
        else:
            break

    endereco = input("Digite o endereço do cliente: ")
    
    clientes[cpf] = Cliente()
    clientes[cpf].cadastrar(nome, cpf, telefone, endereco)

    with open('Sistema Restaurante\\arquivos\clientes.json', 'w') as arquivo:
        json.dump(clientes, arquivo, indent=4)
        
    print("Cliente cadastrado com sucesso")


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    while True:
        print("Bem vindo ao sistema de restaurante")
        escolha = menu()

        with open('Sistema Restaurante\\arquivos\clientes.json', 'r') as arquivo:
            clientes = json.load(arquivo)
        
        with open('Sistema Restaurante\\arquivos\pratos.json', 'r') as arquivo:
            pratos = json.load(arquivo)
            
        with open('Sistema Restaurante\\arquivos\pedidos.json', 'r') as arquivo:
            pedidos = json.load(arquivo)

        match escolha:
            case '1':
                print("Fazer pedido")
            case '2':
                cadastrar_cliente(clientes)
            case '3':
                print("Cadastrar prato")
            case '4':
                print("Listar clientes")
            case '5':
                print("Listar pratos")
            case '6':
                print("Listar pedidos")
            case '7':
                print("Alterar cliente")
            case '8':
                print("Alterar prato")
            case '9':
                print("Fechar caixa")
            case '0':
                print("Saindo do sistema")
                break


if __name__ == "__main__":
    main()
