# Análise
#
# Verificar se todos os elementos de uma lista de booleanos são falsos

# Definição de tipos de dados
# 
# A lista será uma lista de valores booleanos

def todos_falsos(lista: list[bool]) -> bool:
    '''Verifica se todos os elementos da *lista* são falsos.
    Caso a lista seja vazia, retorna False
    
    Exemplos
    >>> todos_falsos([])
    False
    >>> todos_falsos([False])
    True
    >>> todos_falsos([False, False, True, False])
    False
    >>> todos_falsos([False, False, False])
    True
    '''
    contador = 0
    if len(lista) > 0:
        for n in lista:
            if n == True:
                contador = contador + 1
    else:
        contador = 1
    return contador == 0
        