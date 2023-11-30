# Análise
#
# Contar quantas vezes o valor mínimo de uma lista de inteiros aparece na lista. A lista não pode ser vazia

# Análise de tipo de dados
#
# A lista será uma lista de inteiros

def repeticoes_do_min(lista : list[int]) -> int:
    '''
    Indica quantas vezes o valor mínimo da *lista* aparece nela

    Exemplos
    >>> repeticoes_do_min([1])
    1
    >>> repeticoes_do_min([3, 2, 1, 1, 4, 1])
    3
    >>> repeticoes_do_min([2, 3, 1, 3, 0, 1, 1, 1])
    1
    '''
    assert len(lista) != 0
    valor_min = lista[0]
    qnt_min = 0
    for n in lista:
        if n < valor_min:
            valor_min = n
    for n in lista:
        if n == valor_min:
            qnt_min = qnt_min + 1
    return qnt_min