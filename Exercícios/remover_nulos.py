# Análise
#
# Criar uma nova lista removendo os valores números de uma lista de inteiros

# Definição de tipo de dados
#
# A lista será uma lista de inteiros

def remover_nulos(lista: list[int]) -> list[int]:
    '''
    Retorna uma nova lista com os valores nulos da *lista* removidos
    Requer que a lista não seja vazia

    Exemplos
    >>> remover_nulos([32, 312, 41, 4132, 54, 1, 43, 512])
    [32, 312, 41, 4132, 54, 1, 43, 512]
    >>> remover_nulos([0])
    []
    >>> remover_nulos([342, 412, 0, 42, 1, 0, 23, 93, 0])
    [342, 412, 42, 1, 23, 93]
    '''
    assert len(lista) != 0
    nova_lista = []
    for n in lista:
        if n != 0:
            nova_lista.append(n)
    return nova_lista