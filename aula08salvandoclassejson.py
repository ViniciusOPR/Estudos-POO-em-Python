# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json, os
CAMINHO_ARQUIVO = 'aula08.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('John Wick', 35)
p2 = Pessoa('Trinity', 25)
p3 = Pessoa('Harleen Quinzell', 27)


banco = [vars(p1), vars(p2), vars(p3)]

def salvar():
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo:
        print('Salvando')
        json.dump(banco, arquivo, indent=2, ensure_ascii=False)
    

if __name__ == '__main__':
    salvar()