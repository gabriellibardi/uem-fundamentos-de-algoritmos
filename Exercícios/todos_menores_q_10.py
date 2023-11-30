# Análise
#
# Verificar se todos os valores de uma lista de inteiros são menores que 10

# Definição de tipo de dados
#
# A lista será uma lista de números inteiros 

def todos_menores_q_10(lista: list[int]) -> bool:
    '''
    Verifica se todos os valores da *lista* são menores que 10
    Requer que a lista não seja vazia

    Exemplos
    >>> todos_menores_q_10([4, 5, 1, 4, 7 ,1, 3, 9])
    True
    >>> todos_menores_q_10([3, 4, 1, 4, 1, 11, 2])
    False
    '''
    assert len(lista) != 0
    qnt_maiores_ou_iguais = 0
    for v in lista:
        if v >= 10:
            qnt_maiores_ou_iguais = qnt_maiores_ou_iguais + 1
    return qnt_maiores_ou_iguais == 0 