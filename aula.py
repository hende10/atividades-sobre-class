class Pessoa:
    def __init__(self, nome, sexo, matricula, idade):
        self.nome = nome
        self.sexo = sexo
        self.matricula = matricula
        self.idade = idade
    
        def comer(self):
         return f"{self.nome} está comendo."
    
    def beber(self):
        return f"{self.nome} está bebendo."
    
    def falar(self, mensagem):
        return f"{self.nome} está falando: {mensagem} "
    
    def correr(self):
        return f"{self.nome} está correndo."


if __name__ == '__main__':
    pessoa1 = Pessoa(input("digite seu nome: "), input("digite seu sexo: "), input("digite sua matrícula: "), input("digite sua idade: "))
    print(pessoa1.nome)
    print(pessoa1.idade)
    print(pessoa1.sexo)
    print(pessoa1.matricula)
