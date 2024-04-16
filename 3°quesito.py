class Contabancaria:
    def __init__(self, conta, saldo, titular):
        self.conta = conta
        self.saldo = saldo
        self.titular = titular

    def depositardinheiro(self):
        return f'{self.depositardinheiro} Você está depositando!'
    def sacardinheiro(self):
        return f'{self.sacardinheiro} Você sacou dinheiro!'
    def mostarsaldoatual(self):
        return f'{self.mostarsaldoatual} Este é seu saldo atual: {self.saldo}'
    
if __name__ == '__main__':
    conta1 = Contabancaria(input("digite sua conta: "), "5678,90", (input("digite o nome do titular: ")))
    
    print(f'{conta1.conta} \n {conta1.titular}\n {conta1.saldo}')
    print(f'{conta1.depositardinheiro()} \n{conta1.mostarsaldoatual()} \n{conta1.sacardinheiro}')
