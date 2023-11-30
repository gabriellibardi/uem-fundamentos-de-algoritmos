# Análise
#
# Concatenar todos os elementos de uma lista de strings

# Definição de tipos de dados
#
# A lista que será concatenada será uma lista com palavras

def concatenar_strings(lista : list[str]) -> str:
    '''Concatena uma *lista* de strings e retorna uma string com os elementos concatenados

    Exemplos
    >>> concatenar_strings([])
    ''
    >>> concatenar_strings(['Matheus','ama','comer','bananas'])
    'Matheusamacomerbananas'
    '''
    resultado = ''
    for elemento in lista:
        resultado = resultado + elemento
    return resultado
