class Carro:
    def __init__(self, placa, modelo, ano):
        self.placa = placa
        self.modelo = modelo
        self.ano = ano
       
if __name__ == '__main__':
    tipo = input("Qual carro é seu? ")

    match tipo:
        case "palio":
            palio = Carro(input("digite a placa do seu carro (palio): "), 
                          input("digite o modelo do seu carro (palio): "), 
                          input("digite o ano do seu carro (palio): "))
            print(f"A placa do seu {tipo} é {palio.placa}") 
            print(f"O modelo é {palio.modelo}") 
            print(f"E o ano do seu carro é {palio.ano}")
        case "duster":
            duster = Carro(input("digite a placa do seu carro (duster): "), 
                           input("digite o modelo do seu carro(duster): "), 
                           input("digite o ano do seu carro(duster): "))
            print(f"A placa do seu {tipo} é {duster.placa} \no modelo é {duster.modelo} \ne o ano do seu carro é {duster.ano}")

        case "vectra":
            vectra = Carro(input("digite a placa do seu carro (vectra): "), 
                           input("digite o modelo do seu carro (vectra): "), 
                           input("digite o ano do seu carro (vectra): "))
            print(f"A placa do seu {tipo} é: {vectra.placa} \no modelo é {vectra.modelo} \ne o ano do seu carro é {vectra.ano}")