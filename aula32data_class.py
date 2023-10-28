# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html

from dataclasses import asdict, astuple, dataclass, field, fields


# é possivel definir o init da Dataclass como False = (Init = False)
@dataclass(repr=True)
class Pessoa:
    nome: str = field(default='MISSING', repr=False)
    sobrenome: str = 'Not Sent'
    idade: int = 100

    def __post_init__(self):
        self.nome_completo = f'{self.nome} {self.sobrenome}'
# Se o Init da Dataclass for definido como False o post init não vai funcionar
# E o Init precisará ser criado manualmente

    # def__init__(self, nome, sobrenome):
    # self.nome = nome
    # self.sobrenome = ' '.join(sobrenome)
    # self.sobrenome = sobrenome
    # self.nome_completo = f'{self.nome} {self.sobrenome}'

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

    @nome_completo.setter
    def nome_completo(self, valor):
        nome, *sobrenome = valor.split()
        self.nome = nome
        self.sobrenome = ' '.join(sobrenome)


if __name__ == '__main__':
    p1 = Pessoa('Luiz', 'Otávio', 30)
    p2 = Pessoa('Luiz', 'Otávio', 30)
    print(p1 == p2)
    p3 = Pessoa('Vinicius', 'Ouro Preto', 20)
    p3.nome_completo = 'Maria Helena'
    print(p3)
    print(p3.nome_completo)

    print('--')

    lista = [Pessoa('A', 'Z', 1), Pessoa('B', 'Y', 2)]
    ordenadas = sorted(lista, reverse=False, key=lambda p: p.sobrenome)
    print(ordenadas)

    print('--')

    print(asdict(p1).keys())
    print(asdict(p1).values())
    print(asdict(p1).items())
    print(astuple(p1)[0])

    print('--')

    print(fields(p1))
