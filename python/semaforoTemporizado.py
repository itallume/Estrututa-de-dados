from temporizador import Temporizador
from enum import Enum

class estado(Enum):
    vermelho = 1
    amarelo = 2
    verde = 3
class semaforoTemporizado:
    def __init__(self, estadoInicial:estado = estado.verde):
        self.estadoatual = estadoInicial
        self.timer = Temporizador()
        self.tempoDeTrasicao = {estado.vermelho:20, estado.amarelo:5, estado.verde:10}

    def getEstadoAtual(self) ->estado:
        return self.estadoatual
    def __str__(self):
        return f'''
        +-------+
        |  ({"X" if self.estadoatual == estado.vermelho else " "})  |
        |  ({"X" if self.estadoatual == estado.amarelo else " "})  |
        |  ({"X" if self.estadoatual == estado.verde else " "})  |
        +-------+ 
        '''
    def setup(self, tempoVermelho:int, tenpoAmarelo:int, tempoVerde:int):
        '''
        Método que permite ajustar o tempo dis estados do semaforo.

        Argumentos
        ----------
        tempoVermelho(int): tempo em segundos de permanência no vemrelho
        tempoAmarelo(int): tempo em segundos de permanência no amarelo
        tempoVerde(int): tempo em segundos de permanência no verde
        '''