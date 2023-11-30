def main():
    print('Programa que retorna a hipotenusa de um triângulo retangulo com dois catetos informados.')
    # Entrada
    cateto1 : float = float(input('Digite o valor para o primeiro cateto: '))
    cateto2 : float = float(input('Digite o valor para o segundo cateto: '))
    # Processamento
    hip : float = hipotenusa(cateto1, cateto2)
    # Saída
    print('O valor da hipotenusa do triângulo de catetos', cateto1, 'e', cateto2, 'é', hip)
    
def hipotenusa(cateto1 : float, cateto2 : float) -> float:
    '''
    Calcula a hipotenusa de um triângulo retângulo considerando os valores do *cateto1* e do *cateto2*.

    Exemplos
    >>> # (3.0 ** 2.0 + 4.0 ** 2.0) ** (1.0 / 2.0)
    >>> hipotenusa(3.0, 4.0)
    5.0
    '''
    return (cateto1 ** 2.0 + cateto2 ** 2.0) ** (1.0 / 2.0)

main()
