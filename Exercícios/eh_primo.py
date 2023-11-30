# Análise
#
# Verificar se um número inteiro positivo n é primo. Um número inteiro é primo se ele tem exatamente dois divisores distintos, 1 e n.

# Definição de tipo de dados
#
# O número será um número inteiro positivo.

def eh_primo(n : int) -> bool:
    '''
    Verifica se um número inteiro *n* é primo.
    Requer *n* > 0 

    Exemplos
    >>> eh_primo(1)
    False
    >>> eh_primo(2)
    True
    >>> eh_primo(5)
    True
    >>> eh_primo(8)
    False
    >>> eh_primo(11)
    True
    >>> eh_primo(104729)
    True
    '''
    resposta = True
    i = 2
    if n == 1:
        resposta = False
    while i < (n//2) and resposta:
        if n % i == 0:
            resposta = False
        i = i + 1
    return resposta
