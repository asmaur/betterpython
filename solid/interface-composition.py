from abc import ABC, abstractmethod

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


class ProcessarPagamento(ABC):
    @abstractmethod
    def pagar(self, pedido):
        pass

class ValidadorSMS:
    valido = False
    
    def verificar_codigo(self, codigo):
        print(f"Validando codigo: {codigo}")
        self.valido = True
    
    def validado(self) -> bool:
        return self.valido


class PagamentoDebito(ProcessarPagamento):
    def __init__(self, codigo_validacao, validador: ValidadorSMS) -> None:
        self.codigo_validacao = codigo_validacao
        self.validador = validador   
    
    def pagar(self, pedido):
        if not self.validador.validado():
            raise Exception("Não Validado")
        print("Processando meio de pagamento: débito")
        print(f"Verificando codigo de segurança: {self.codigo_validacao}")
        pedido.estado == "pago"

class PagamentoCredito(ProcessarPagamento):
    def __init__(self, codigo_validacao) -> None:
        self.codigo_validacao = codigo_validacao    
    
    
    def pagar(self, pedido):        
        print("Processando meio de pagamento: crébito")
        print(f"Verificando codigo de segurança: {self.codigo_validacao}")
        pedido.estado = "pago"

class PagamentoPaypal(ProcessarPagamento): 
    def __init__(self, email, validador: ValidadorSMS) -> None:
        self.email = email
        self.validador = validador
        
    def pagar(self, pedido): 
        if not self.validador.validado():
            raise Exception("Não Validado")       
        print("Processando meio de pagamento: Paypal")
        print(f"Verificando endereço email: {self.email}")
        pedido.estado = "pago"
        
        
pedido = Pedido()
pedido.add_item("Teclado", 1, 50)
pedido.add_item("SSD", 1, 150)
pedido.add_item("Celular", 2, 5)

print(pedido.valor_total())
validador = ValidadorSMS()
validador.verificar_codigo("883883")
pagamento = PagamentoPaypal("hello@gmail.com", validador)
#pagamento.validar_sms("883883")
pagamento.pagar(pedido)