# Análise
#
# Classificar o nome de uma pessoal entre curto, mediano ou longo. Um nome curto tem no máximo 4 letras,
# um mediano, entre 5 e 8 e um longo, mais que 8.

# Definição de dados
#
# O nome é um texto só com letras, nesse caso, uma string, já o tamanho será especificado em uma variável
# própria, por meio de um Enum.

from enum import Enum, auto

class Tamanho(Enum):
    CURTO = auto()
    MEDIANO = auto()
    LONGO = auto()

def tamanhoNome(nome : str) -> Tamanho:
    '''
    Classifica *nome* entre curto, mediano e longo. Sendo curto para o tamanho do *nome* <= 4,
    mediano se >= 5 *nome* <= 8 e longo se *nome* >= 8.

    Exemplos
    >>> tamanhoNome('Alex').name
    'CURTO'
    >>> tamanhoNome('Gabriel').name
    'MEDIANO'
    >>> tamanhoNome('Adenilson').name
    'LONGO'
    '''
    if len(nome) <= 4:
        resultado = Tamanho.CURTO
    elif len(nome) > 8:
        resultado = Tamanho.LONGO
    else:
        resultado = Tamanho.MEDIANO
    return resultado
