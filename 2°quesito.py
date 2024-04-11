class Animal:
    def __init__(self, nome, idade, especie):
        self.nome = nome
        self.idade = idade
        self.especie = especie

    def emitirsom(self):
        return f"{self.emitirsom} AU au!"
    
    def informacoes(self):
        return f"{self.informacoes} O Pastor-alemão tem personalidade forte, é extremamente protetor e atencioso com a própria família."
        
if __name__ == "__main__":
    animal1 = Animal("Marley", "11", "Pastor Alemão")
    print({animal1.nome}, {animal1.especie}, {animal1.idade})
    print(animal1.emitirsom())
    print(animal1.informacoes())