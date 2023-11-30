# Análise
#
# Criar uma lista de números a partir de uma lista de strings, onde cada string representa
# um número válido.

# Definição de tipo de dados
#
# A lista de strings será uma lista de str onde cada valor representa um número válido
# A lista de números será representada por uma lista de valores flutuantes

def lista_str_para_float (lista_str : list[str]) -> list[float]:
    '''
    Transforma a *lista_str* em uma lista de números, onde cada valor da *lista_str* é convertido 
    para um valor numérico equivalente.

    Exemplos
    >>> lista_str_para_float(['32.312', '-93', '7372.2', '9183', '0'])
    [32.312, -93.0, 7372.2, 9183.0, 0.0]
    '''
    assert len(lista_str) != 0
    lista_float : list[float] = []
    for v in lista_str:
        lista_float.append(float(v))
    return lista_float