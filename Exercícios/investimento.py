# Análise
#
# Calcular o valor que um investimento irá render em um banco no tempo de um ano. A taxa de correção anual 
# para valores até R$2000 é de 10%, para valores entre 2000R$ e 5000R$ é de 12% e para valores maiores 
# que R$5000, de 13%

# Definição dos tipos de dados
#
# Os valores serão expressados em números flutuantes(float), por possuir parte decimal.

def investimento1ano(valorInvestido : float) -> float:
    '''
    Calcula o valor que rendirá em um banco no tempo de 1 ano, com uma taxa de correção anual, onde
    para um *valorInvestido* < 2000.00, a taxa será de 10%. Para 2000.00 <= *valorInvestido*  <= 5000.00, a
    taxa será de 12% e para um *valorInvestido* > 5000.00, a taxa será de 13%.

    Exemplos:
    >>> round(investimento1ano(1387.23), 2)
    1525.95
    >>> round(investimento1ano(3092.32), 2)
    3463.4
    >>> round(investimento1ano(6354.99), 2)
    7181.14
    '''
    if valorInvestido < 2000.00:
        valorFinal = valorInvestido + valorInvestido * (10/100)
    elif valorInvestido > 5000.00:
        valorFinal = valorInvestido + valorInvestido * (13/100)
    else:
        valorFinal = valorInvestido + valorInvestido * (12/100)
    return valorFinal