# Análise
#
# Definir o sinal de um número indicado. Devolvendo -1 para números negativos, 0 para o 0 e +1 para números positivos

# Definição dos tipos de dados
#
# O número indicado poderá ser qualquer número flutuante

def sinal(valor : float) -> int:
    '''
    Indica o sinal de um *valor*, retornando -1 para números negativos, 0 para 0 e 1 para positivos 

    Exemplos
    >>> sinal(42.0)
    1
    >>> sinal(-3213.675)
    -1
    >>> sinal(0.0)
    0
    '''
    if valor > 0.0:
        resultado = 1
    elif valor < 0:
        resultado = -1
    else:
        resultado = 0
    return resultado
