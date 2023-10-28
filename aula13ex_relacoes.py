# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
    def __init__(self, nome):
        self.nome_carro = nome
        self._motor_carro = None
        self._fabricante_carro = None

    @property
    def motor(self):
        return self._motor_carro

    @motor.setter
    def motor(self, valor):
        self._motor_carro = valor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor

class Motor:
    def __init__(self, nome):
        self.nome_motor = nome
       

class Fabricante:
    def __init__(self, nome):
        self.nome_fabricante = nome

volkswagen = Fabricante('Volkswagen')
fusca = Carro('fusca')
motor_2_0_turbo = Motor('2.0 turbo')
fusca.motor = motor_2_0_turbo
fusca.fabricante = volkswagen
print(fusca.nome_carro, fusca.fabricante.nome_fabricante, fusca.motor.nome_motor)

