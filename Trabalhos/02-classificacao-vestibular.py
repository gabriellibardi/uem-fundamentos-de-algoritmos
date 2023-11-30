from dataclasses import dataclass

# Análise

#   Projetar uma função que recebe como entrada uma lista de provas e um gabarito e devolver uma lista com o desempenho
# de cada candidato que não foi desclassificado na redação (não ficou com nota zero).
#   Sabe-se que as provas da lista possuem, além de uma lista com as respostas das questões da prova, a nota da redação
# entre 0 e 120 e o código do candidato que realizou a prova.
#   As questões são somatórias, onde cada alternativa entre 01, 02, 04, 08 e 16 podem ser assinadas ou não.
#   A nota das questões, de 0 a 6, é encontrada dependendo do número de alternativas assinadas. Onde, ao marcar uma errada, a nota
# é zero, de resto, é a razão entre alternativas certas assinaladas e do total de alternativas corretas, com excessão do
# caso de não ter nenhuma alternativa correta, nesse caso, ao não se assinalar nada, a nota será 6.
#   A quantidade de itens na lista de resposta e de cada candidato são iguais e podem variar.
#   A classificação final dos canditados na resposta são classificados por nota.

# Definição de tipo de dados

#   As provas serão representadas por um tipo composto.
#   O gabarito e as questões respondidas serão representados por uma lista de mesmo tamanho de números inteiros.
#   O desempenho dos candidatos será representado por um tipo composto.
#   As nota serão representadas por números flutuantes.
#   O código do candidato será representado por um número inteiro

@dataclass
class Prova:
    '''Prova feita por um candidato, contendo sua identificação'''
    codigo : int
    nota_redacao : float
    respostas : list[int]

@dataclass
class DesempenhoCandidato:
    '''Desempenho do candidato na prova'''
    codigo : int
    nota : float

def calcular_desempenhos(provas : list[Prova], gabarito: list[int]) -> list[DesempenhoCandidato]:
    '''
    Calcula a lista de desempenho dos candidatos que realizaram a prova, comparando as notas das *provas* com o *gabarito*
    e somando com a nota da redação dos candidatos.
    Caso o candidato tenha tirado 0 na redação, ele não estará na lista de desempenhos individuais.
    Requer que a lista de respostas de cada prova possua o mesmo tamanho do gabarito.
    Requer *gabarito* não vazio.

    Exemplos
    >>> calcular_desempenhos([], [14, 31, 0, 12])
    []
    >>> calcular_desempenhos([Prova(1234, 0.0, [4, 10, 4, 16, 10])], [21, 10, 8, 16, 15])
    []
    >>> calcular_desempenhos([Prova(3211, 80.0, [4, 10, 4, 16, 10]),\
                              Prova(7102, 0.0, [1, 2, 3, 4, 5]),\
                              Prova(1234, 90.0, [21, 8, 8, 8, 14]),\
                              Prova(5812, 32.0, [20, 0, 8, 16, 1]),\
                              Prova(9123, 0.0, [5, 4, 3, 2, 1])],\
                              [21, 10, 8, 16, 15])
    [DesempenhoCandidato(codigo=1234, nota=109.5), DesempenhoCandidato(codigo=3211, nota=97.0), DesempenhoCandidato(codigo=5812, nota=49.5)]
    '''
    assert gabarito != []
    desempenhos = []
    # consegue a lista de alternativas para cada questão do gabarito
    alternativas_gabarito = alternativas_por_questao(gabarito)
    for prova in provas:
        # certifica que a prova tem o mesmo número de questões do gabarito
        assert len(prova.respostas) == len(gabarito)
        # analisa se o candidato não zerou a redação
        if prova.nota_redacao > 0:
            nota_questoes = calcular_nota(prova.respostas, alternativas_gabarito, 0)
            nota_total = nota_questoes + prova.nota_redacao
            desempenhos.append(DesempenhoCandidato(prova.codigo, nota_total))
    ordenar_desempenhos(desempenhos)
    return desempenhos

def alternativas_por_questao(questoes: list[int]) -> list[list[int]]:
    '''
    Cria uma lista onde cada elemento é a lista de alternativas que somadas geram o resultado de cada questão na lista de *questões*.

    Exemplos
    >>> alternativas_por_questao([])
    []
    >>> alternativas_por_questao([0])
    [[]]
    >>> alternativas_por_questao([20, 0, 8, 16, 15])
    [[4, 16], [], [8], [16], [1, 2, 4, 8]]
    >>> alternativas_por_questao([21, 10, 8, 16, 15])
    [[1, 4, 16], [2, 8], [8], [16], [1, 2, 4, 8]]
    '''
    questoes_em_alternativas = []
    for questao in questoes:
        questoes_em_alternativas.append(somatorio_alternativas(questao))
    return questoes_em_alternativas

def somatorio_alternativas(s: int) -> list[int]:
    '''
    Calcula a lista de alternativas que somadas gera o somátorio *s*.
    Cada alternativa pode ser um dos valores: 1, 2, 4, 8, 16.
    Requer que *s* esteja no entre 0 e 31.

    Exemplos
    >>> somatorio_alternativas(0)
    []
    >>> somatorio_alternativas(1)
    [1]
    >>> somatorio_alternativas(21)
    [1, 4, 16]
    >>> somatorio_alternativas(10)
    [2, 8]
    >>> somatorio_alternativas(31)
    [1, 2, 4, 8, 16]
    '''
    assert s >= 0 and s <= 31
    alternativas = []
    alternativa = 1
    while s > 0:
        # verifica se alternativa faz parte do somatório s
        if s % 2 == 1:
            alternativas.append(alternativa)
        # divide todas as alternativas que compõe o somatório s por 2
        s = s // 2
        # procura a próxima alternativa
        alternativa = alternativa * 2
    return alternativas

def calcular_nota(respostas: list[int], gabarito: list[list[int]], n: int):
    '''
    Calcula a nota das questões de uma prova do vestibular de acordo com as *respostas* assinadas e com as
    alternativas corretas de cada questão no *gabarito*, somando a nota das questões a partir da questão *n*.
    Requer que o gabarito não seja vazio.
    Requer que 0 <= n <= len(respostas).

    Exemplos
    >>> calcular_nota([21, 8, 8, 8, 14],\
                     [[1, 4, 16], [2, 8], [8], [16], [1, 2, 4, 8]], 0)
    19.5
    >>> calcular_nota([4, 10, 4, 16, 10],\
                     [[1, 4, 16], [2, 8], [8], [16], [1, 2, 4, 8]], 0)
    17.0
    '''
    assert gabarito != []
    assert n >= 0 and n <= len(respostas)
    if n >= len(respostas):
        nota = 0.0
    else:    
        alternativas_assinadas = somatorio_alternativas(respostas[n])
        nota = nota_questao(alternativas_assinadas, gabarito[n]) + calcular_nota(respostas, gabarito, n + 1) 
    return nota

def nota_questao(assinadas: list[int], gabarito: list[int]) -> float:
    '''
    Calcula a nota de uma questão comparando as alternativas *assinadas* com as alternativas do *gabarito*, onde a nota
    varia entre 0 e 6.
    Caso o candidato tenha assinado uma alternativa que não está no gabarito, ele zera a questão.

    Exemplos
    >>> nota_questao([], [2, 4])
    0.0
    >>> nota_questao([1, 16], [1, 4, 8])
    0.0
    >>> nota_questao([], [])
    6.0
    >>> nota_questao([4, 16], [4, 16])
    6.0
    >>> nota_questao([2, 8], [2, 8, 16])
    4.0
    '''
    nota = 0.0
    if len(gabarito) > 0:
        # somatória diferente de 0
        nota_por_alternativa = 6.0 / len(gabarito)
        i = 0
        nao_errou = True
        while i < len(assinadas) and nao_errou:
            if assinadas[i] in gabarito:
                nota = nota + nota_por_alternativa
            else:
                nao_errou = False 
                nota = 0.0
            i = i + 1
    else:
        # somatória igual a 0
        if len(assinadas) == 0:
            nota = 6.0
    return nota

def ordenar_desempenhos(desempenhos: list[DesempenhoCandidato]):
    '''
    Ordena a lista dos *desempenhos* dos candidatos do vestibular em ordem de maior nota total para menor nota total.

    Exemplos
    >>> a = []
    >>> ordenar_desempenhos(a)
    >>> a
    []
    >>> b = [DesempenhoCandidato(1234, 103.5)]
    >>> ordenar_desempenhos(b)
    >>> b
    [DesempenhoCandidato(codigo=1234, nota=103.5)]
    >>> c = [DesempenhoCandidato(1234, 109.5),\
             DesempenhoCandidato(3211, 97.0),\
             DesempenhoCandidato(5812, 49.5)]
    >>> ordenar_desempenhos(c)
    >>> c
    [DesempenhoCandidato(codigo=1234, nota=109.5), DesempenhoCandidato(codigo=3211, nota=97.0), DesempenhoCandidato(codigo=5812, nota=49.5)]
    >>> d = [DesempenhoCandidato(1234, 109.5),\
             DesempenhoCandidato(3581, 34.2),\
             DesempenhoCandidato(3211, 97.0),\
             DesempenhoCandidato(5812, 49.5)]
    >>> ordenar_desempenhos(d)
    >>> d
    [DesempenhoCandidato(codigo=1234, nota=109.5), DesempenhoCandidato(codigo=3211, nota=97.0), DesempenhoCandidato(codigo=5812, nota=49.5), DesempenhoCandidato(codigo=3581, nota=34.2)]
    '''
    for i in range(len(desempenhos)):
        maior_nota = desempenhos[i].nota
        for j in range(i + 1, len(desempenhos)):
            if desempenhos[j].nota > maior_nota:
                maior_nota = desempenhos[j].nota
                # troca os elementos de lugar
                desempenho_temp = desempenhos[i]
                desempenhos[i] = desempenhos[j]
                desempenhos[j] = desempenho_temp