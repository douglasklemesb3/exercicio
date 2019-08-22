class Pessoa:
    def __init__(self,nome,idade,rg):
        self.nome = nome
        self.idade = idade
        self.rg = rg

    def dados(self):
        print('jorge,20,544503247')


class Medico(Pessoa):
    def __init__(self,nome,idade,rg,crm):
        super().__init__(nome,idade,rg)
        self.crm = crm
    def CRM(self):
        print(1420)

class Paciente(Pessoa):
    def __init__(self,nome,idade,rg,sintomas):
        super().__init__(idade,nome,rg)
        self.sintomas = sintomas

    def sintomas(self):
        print('dor de cabeça')

pessoa = Pessoa('jorge',20 ,544503247)
medico = Medico('samuel', 45,544503247, 1420)
paciente = Paciente('thiago',17,544503235,'cancer')

print(dados)
print(CRM)
print(sintomas)