from abc import ABC, abstractmethod
from random import choice


class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass


class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo está buscando o cliente...')


class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro de popular está buscando o cliente...')


class MotoPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto está buscando o cliente...')


class MotoLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto de Luxo está buscando o cliente...')


class VeiculoFactory(ABC):
    def __init__(self, tipo):
        self.carro = self.get_carro(tipo)

    @staticmethod
    @abstractmethod
    def get_carro(tipo: str) -> Veiculo: pass

    def buscar_cliente(self):
        self.carro.buscar_cliente()


class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'luxo':
            return CarroLuxo()
        if tipo == 'popular':
            return CarroPopular()
        if tipo == 'moto':
            return MotoPopular()
        if tipo == 'moto_luxo':
            return MotoLuxo()
        assert 0, 'Veículo não existe'


class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo):
        if tipo == 'popular':
            return CarroPopular()
        if tipo == 'moto':
            return MotoPopular()
        assert 0, 'Veículo não existe'


if __name__ == '__main__':
    vaiculos_disponiveis_zona_norte = ['luxo', 'popular', 'moto', 'moto_luxo']
    vaiculos_disponiveis_zona_sul = ['popular', 'moto']

    for i in range(10):
        carro = ZonaNorteVeiculoFactory(
            choice(vaiculos_disponiveis_zona_norte))
        carro.buscar_cliente()

    print()

    for i in range(10):
        carro = ZonaSulVeiculoFactory(
            choice(vaiculos_disponiveis_zona_sul))
        carro.buscar_cliente()
