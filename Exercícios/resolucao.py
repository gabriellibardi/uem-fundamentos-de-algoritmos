from dataclasses import dataclass
from enum import Enum, auto

@dataclass
class Resolucao:
    '''
    Resolução de uma tela.
    Requer valores positivos.
    '''
    largura : int
    altura : int

class Possibilidade(Enum):
    '''
    Possibilidade de uma imagem ser exibida em uma tela.
    '''
    PODE = auto()
    NAO_PODE = auto()

class Aspecto(Enum):
    '''
    Aspecto de uma resolução (razão entre a largura e a altura)
    '''
    A_4P3 = auto()
    A_16P9 = auto()
    A_16P10 = auto()
    INVALIDO = auto()

# EXERCÍCIO A

# Análise
#
# Determinar quantos mega pixels uma imagem possui dada a sua resolução. O número de megapixel pode ser caculado
# multiplicando-se a altura e largura e dividindo-se por 1 milhão.

# Definição de tipo de dados
#
# A altura e a largura da tela são dados pela sua resolução, que é uma estrutura própria

def qnt_megapixels(resolucao : Resolucao) -> float:
    '''
    Determina quantos mega pixels uma imagem possui de acordo com sua *resolucao*. O número de megapixel é encontrado
    multiplicando a altura e largura da imagem e dividindo por 1 milhão.

    Exemplos
    >>> qnt_megapixels(Resolucao(1920, 1080))
    2.0736
    >>> qnt_megapixels(Resolucao(1080, 720))
    0.7776
    '''
    return resolucao.altura * resolucao.largura / 1000000

# EXERCÍCIO B

# Análise

# Verificar se uma imagem pode ser exibida completamente na tela sem a necessidade de rotação ou redução de tamanho
# levando em conta a resolução delas.

# Definição de tipo de dados

# As duas resoluções são representadas por uma estrutura composta

def pode_exibir(resolucao_imagem: Resolucao, resolucao_tela: Resolucao) -> Possibilidade:
    '''
    Verifica se uma imagem pode ser exibida completamente na tela sem a necessidade de rotação ou redução de tamanho
    levando em conta a resolução delas.

    Exemplos
    >>> pode_exibir(Resolucao(1920, 720), Resolucao(1920, 1080)).name
    'PODE'
    >>> pode_exibir(Resolucao(1920, 1080), Resolucao(1080, 720)).name
    'NAO_PODE'
    '''
    possibilidade_exibir = Possibilidade.NAO_PODE
    if resolucao_imagem.altura <= resolucao_tela.altura:
        if resolucao_imagem.largura <= resolucao_tela.largura:
            possibilidade_exibir = Possibilidade.PODE
    return possibilidade_exibir

# EXERCÍCIO C

# Análise
#
# Indicar se uma resolução tem aspecto(razão entre largura e altura) de 4:3, 16:9 ou 16:10. Por exemplo, a
# resolução 1080 x 1920 tem aspecto 16:9, pois 1080 x 16 = 1920 x 9

# Definição de tipo de dados
#
# A resolução é indicada por um tipo composto

def aspecto_resolucao(resolucao: Resolucao) -> Aspecto:
    '''
    Retorna o aspecto da *resolucao*. Caso a resolução não possuir um dos aspectos principais, ela é considerada inválida

    Exemplos
    >>> aspecto_resolucao(Resolucao(1920, 1080)).name
    'A_16P9'
    >>> aspecto_resolucao(Resolucao(1440, 900)).name
    'A_16P10'
    >>> aspecto_resolucao(Resolucao(1600, 1200)).name
    'A_4P3'
    >>> aspecto_resolucao(Resolucao(1920, 1000)).name
    'INVALIDO'
    '''
    aspecto = Aspecto.INVALIDO
    if resolucao.altura * 4 == resolucao.largura * 3:
        aspecto = Aspecto.A_4P3
    elif resolucao.altura * 16 == resolucao.largura * 9:
        aspecto = Aspecto.A_16P9
    elif resolucao.altura * 16 == resolucao.largura * 10:
        aspecto = Aspecto.A_16P10
    return aspecto