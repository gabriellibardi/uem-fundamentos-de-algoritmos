from enum import Enum, auto

# Análise
#
# Determinar um valor final a ser pago por um consumidor dado seu consumo em quilowatt-hora,
# a tarifa básica do quilowatt-hora e a bandeira tarifária. Onde a bandeira verde não acrescenta
# nenhum valor na tarifa, a amarela acrescenta R$0,01874, a vermelha-patamar 1 R$0,03971 e a
# vermelha-patamar 2 R$0,09492.

# Projeto de tipo de dados
#
# O consumo estará em kWh, e será um número flutuante não negativo
# A tarifa básica é dada em reais, um número flutuante não negativo
# A bandeira tarifária será um tipo de dado enumerado

class Bandeira(Enum):
    VERDE = auto()
    AMARELO = auto()
    VERMELHO1 = auto()
    VERMELHO2 = auto()

TARIFA_VERDE : float = 0.0
TARIFA_AMARELO : float = 0.01874 
TARIFA_VERMELHO1 : float = 0.03971
TARIFA_VERMELHO2 : float = 0.09492

def valorConsumoEnergia(consumo : float, tarifa : float, bandeira : Bandeira) -> float:
    '''
    Determina o valor de consumo de energia a ser pago levando em conta o *consumo* em kwH,
    a *tarifa* e a *bandeira* tarifária.
    Bandeira verde: sem acréscimo na tarifa
    Bandeira amarela: acréscimo de R$0,01874 na tarifax1
    Bandeira vermelha-patamar 1: acréscimo de R$0,03971 na tarifa
    Bandeira vermelha-patamar 2: acréscimo de R$0,09492 na tarifa.

    Exemplos
    >>> round(valorConsumoEnergia(200, 0.57, Bandeira.VERDE), 1)
    114.0
    >>> round(valorConsumoEnergia(200, 0.57, Bandeira.AMARELO), 1)
    117.7
    >>> round(valorConsumoEnergia(200, 0.57, Bandeira.VERMELHO1), 1)
    121.9
    >>> round(valorConsumoEnergia(200, 0.57, Bandeira.VERMELHO2), 1)
    133.0
    '''
    if bandeira.name == 'VERDE':
        tarifaFinal = TARIFA_VERDE + tarifa
    if bandeira.name == 'AMARELO':
        tarifaFinal = TARIFA_AMARELO + tarifa
    if bandeira.name == 'VERMELHO1':
        tarifaFinal = TARIFA_VERMELHO1 + tarifa
    if bandeira.name == 'VERMELHO2':
        tarifaFinal = TARIFA_VERMELHO2 + tarifa
    return tarifaFinal * consumo