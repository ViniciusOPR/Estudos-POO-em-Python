from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia: int, numero_conta: int, saldo: float = 0) -> None:
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor: float) -> float:
        pass

    def depositar(self, valor: float) -> float:
        if not isinstance(valor, (int, float)):
            raise ValueError('Valor do Depósito precisa ser numérico')

        self.saldo += valor
        self.detalhes(f'DEPÓSITO {valor}')
        return self.saldo

    def detalhes(self, msg: str = '') -> None:
        print(f'Agência: {self.agencia}')
        print(f'Número da conta: {self.numero_conta}')
        print(f'Saldo: {self.saldo: .2f} {msg}')
        print('--')

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.numero_conta!r}, {self.saldo!r})'
        return f'{class_name}{attrs}'


class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self.saldo

        print('Não foi possível sacar o valor desejado')
        self.detalhes(f'(SAQUE NEGADO {valor})')


class ContaCorrente(Conta):
    def __init__(self, agencia: int, numero_conta: int, saldo: float = 0, limite: float = 100):
        super().__init__(agencia, numero_conta, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    def sacar(self, valor: float) -> float:
        if (self.saldo + self.limite) < valor:
            print('Não foi possível sacar o valor desejado')
            self.detalhes(f'(SAQUE NEGADO {valor})')
            return self.saldo

        self.saldo -= valor
        self.detalhes(f'(SAQUE {valor})')
        return self.saldo

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.numero_conta!r}, {
            self.saldo!r}, {self.limite!r})'
        return f'{class_name}{attrs}'


if __name__ == '__main__':
    cp1 = ContaPoupanca(111, 222)
    cp1.sacar(1)
    cp1.depositar(1)
    cp1.sacar(1)
    cp1.sacar(1)
    print('##')
    cc1 = ContaCorrente(111, 222, 0, 100)
    cc1.sacar(1)
    cc1.depositar(1)
    cc1.sacar(1)
    cc1.sacar(1)
    cc1.sacar(98)
    cc1.sacar(1)
    print('##')
