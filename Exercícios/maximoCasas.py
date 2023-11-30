from enum import Enum, auto
from dataclasses import dataclass

# Análise
#
# Indica o número de casas possíveis que um jogador pode avançar em um jogo de tabuleiro dependendo da sua posição. O tabuleiro possui 10 linhas e 10 colunas. O jogador fica virado para
# uma das quatro direções (norte, sul, leste e oeste) e pode avançar o máximo de casas que puder naquela direção, sem sair no tabuleiro.

# Projeto de tipo de dados
#
# As linha e coluna em que o jogador está serão representadas por um número inteiro de 1 até 10 dentro de uma estrutura composta
# As direções em que o jogador está virado será representada por uma estrutura enumerada

@dataclass
class Posicao:
    '''Posição de um jogador em um tabuleiro(a casa em que ele está), representado pela linha e coluna ocupadas.
    Linha e coluna precisam ser um valor inteiro entre 1 e 10'''
    linha : int
    coluna : int

class Direcao(Enum):
    '''Direcação em que um jogador está virado em um jogo de tabuleiro'''
    NORTE = auto()
    SUL = auto()
    LESTE = auto()
    OESTE = auto()

def maximoCasas(posicao: Posicao, direcao : Direcao) -> int:
    '''
    Indica o número máximo de casas que um jogador pode andar em um tabuleiro 10x10, levando em conta sua *posicao* no tábuleiro,
    indicada pela sua linha e coluna, além da *direção* em que o jogador está virado.

    Exemplos
    >>> maximoCasas(Posicao(5, 4), Direcao.NORTE)
    4
    >>> maximoCasas(Posicao(5, 4), Direcao.LESTE)
    6
    >>> maximoCasas(Posicao(10, 10), Direcao.SUL)
    0
    >>> maximoCasas(Posicao(10, 10), Direcao.OESTE)
    9
    '''
    numeroCasas = 0
    if direcao.name == 'NORTE':
        numeroCasas = posicao.linha - 1
    elif direcao.name == 'SUL':
        numeroCasas = 10 - posicao.linha
    elif direcao.name == 'LESTE':
        numeroCasas = 10 - posicao.coluna
    elif direcao.name == 'OESTE':
        numeroCasas = posicao.coluna - 1
    return numeroCasas 