from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int


print(Pessoa(nome='Eduardo', idade= 29))

#Mesmo passando tipos errados, não acontecerá nada.
#MyPy faria a validação estática (static typing).
print(Pessoa(nome='Eduardo', idade= 'ABC'))

