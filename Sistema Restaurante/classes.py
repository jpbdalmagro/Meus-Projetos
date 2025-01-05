class Cliente:
    def __init__(self):
        self.nome = None
        self.cpf = None
        self.telefone = None
        self.endereco = None
        self.pedidos = []
        
    def cadastrar(self, nome, cpf, telefone, endereco):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.endereco = endereco
        
    def alterar_nome(self, nome):
        self.nome = nome
        
    def alterar_cpf(self, cpf):
        self.cpf = cpf
        
    def alterar_telefone(self, telefone):
        self.telefone = telefone
        
    def alterar_endereco(self, endereco):
        self.endereco = endereco
        
    def adicionar_pedido(self, pedido):
        self.pedidos.append(pedido)
        
    def __str__(self):
        return f'Nome: {self.nome}\nCPF: {self.cpf}\nTelefone: {self.telefone}\nEndereço: {self.endereco}\nPedidos: {self.pedidos}'
    
class Pratos:
    def __init__(self):
        self.nome = None
        self.preco = None
        self.ingredientes = None
        
    def cadastrar(self, nome, preco, ingredientes):
        self.nome = nome
        self.preco = preco
        self.ingredientes = ingredientes
        
    def alterar_nome(self, nome):
        self.nome = nome
        
    def alterar_preco(self, preco):
        self.preco = preco
        
    def alterar_ingredientes(self, ingredientes):
        self.ingredientes = ingredientes
        
    def __str__(self):
        return f'Nome: {self.nome}\nPreço: R${self.preco}\nIngredientes: {self.ingredientes}'
    

class Pedidos:
    def __init__(self, cliente):
        self.cliente = cliente
        self.pratos = []
        self.total = 0
        
    def adicionar_prato(self, prato):
        self.pratos.append(prato)
        self.total += prato.preco
        
    def __str__(self):
        return f'Cliente: {self.cliente.nome}\nPratos: {self.pratos}\nTotal: R${self.total}'
