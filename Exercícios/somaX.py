# Análise
#
# Criar uma nova lista somando um valor x especificado a cada elemento de uma lista de inteiros.

# Definição de tipo de dados
#
# A lista será uma lista de inteiros.
# O valor x será um número inteiro.

def somaX(lista: list[int], x : int) -> list[int]:
    ''' 
    Retorna uma lista de inteiros, somando cada elemento da *lista* por *x*
    Caso a lista seja vazia, retorna a própria lista vazia.
    
    Exemplos
    >>> somaX([32, 412, 3412, 41], 3)
    [35, 415, 3415, 44]
    >>> somaX([], 5)
    []
    >>> somaX([543, 412, 414, 56], 0)
    [543, 412, 414, 56]
    '''
    nova_lista = []
    for e in lista:
        nova_lista.append(e+x)
    return nova_lista