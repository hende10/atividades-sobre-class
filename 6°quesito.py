class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura
    
    def definir(self):
        return f'seu nome é:{self.nome}, sua idade é:{self.idade}, sua altura é: {self.altura}'
    
    
    def cumprimentar(self):
        return f'{self.nome} falou com você'
    
if __name__ == '__main__':
    Pessoa1 = Pessoa('Hendeson', '16 anos', '1,88')
    
    print(Pessoa1.definir())
    print(Pessoa1.cumprimentar())
    