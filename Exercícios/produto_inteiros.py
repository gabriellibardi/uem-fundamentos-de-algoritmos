# Análise
#
# Calcular o produto de todos os elementos de uma lista de inteiros

# Definição dos tipos de dados
#
# A lista será uma lista de inteiros

def produto_inteiros(lista: list[int]) -> int:
    '''Calcular o produto de todos os elementos da *lista* e caso a lista seja vazia, retorna 0
    
    Exemplos
    >>> produto_inteiros([])
    0
    >>> produto_inteiros([321])
    321
    >>> produto_inteiros([32, 1, 2, 5])
    320
    '''
    produto = 1
    if len(lista) == 0:
        produto = 0
    else:
        for n in lista:
            produto = produto * n
    return produto