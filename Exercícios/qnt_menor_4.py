# Análise
#
# Verificar se a quantidade de elementos de uma lista de floats é menor que 4

# Análise de tipo de dados
#
# A lista é uma lista de floats

def qnt_menor_4(lista: list[float]) -> bool:
    '''
    Verifica se a quantidade de elementos da *lista* é menor que 4

    Exemplos
    >>> qnt_menor_4([])
    True
    >>> qnt_menor_4([32.3, 31.4, 53.6])
    True
    >>> qnt_menor_4([9232.354, 8321.9, 0.0, 438.2])
    False
    >>> qnt_menor_4([32.0, 4.2, 15.335, 1.0, 133.2, 43.1])
    False
    '''
    return len(lista) < 4
    