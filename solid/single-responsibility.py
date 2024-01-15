class Pedido:
    def __init__(self) -> None:
        self.itens = []
        self.quantidades = []
        self.precos = []
        self.estado = "aberto"
    
    def add_item(self, nome, quantidade, preco):
        self.itens.append(nome)
        self.precos.append(preco)
        self.quantidades.append(quantidade)
    
    def valor_total(self) -> float:
        total = 0
        for i in range(len(self.itens)):
            total += self.quantidades[i] * self.precos[i]
        return total

class ProcessarPagamento:     
    def debito(self, pedido, codigo_validacao):
        print("Processando meio de pagamento: débito")
        print(f"Verificando codigo de segurança: {codigo_validacao}")
        pedido.estado == "pago"
        
    def credito(self, pedido, codigo_validacao):        
        print("Processando meio de pagamento: crébito")
        print(f"Verificando codigo de segurança: {codigo_validacao}")
        pedido.estado = "pago"
        
    
pedido = Pedido()
pedido.add_item("Teclado", 1, 50)
pedido.add_item("SSD", 1, 150)
pedido.add_item("Celular", 2, 5)

print(pedido.valor_total())
pagamento = ProcessarPagamento()
pagamento.debito(pedido, "0372846")