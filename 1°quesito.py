class Carro:
    def __init__(self, marca, ano, cor):
        self.marca = marca
        self.ano = ano
        self.cor = cor

    def ligar(self):
        return f"{self.ligar} seu carro está ligado!"
    
    def desligar(self):
        return f"{self.desligar} seu carro está desligado!"
    
    def acelerar(self):
        return f"{self.acelerar} você acelerou seu carro!"
    
if __name__ == "__main__":
    carro1 = Carro("Renault", "2024", "Vermelho")

    print(carro1.ligar())
    print(carro1.desligar())
    print(carro1.acelerar())
    