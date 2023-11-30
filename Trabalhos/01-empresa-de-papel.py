from enum import Enum, auto
from dataclasses import dataclass

# Monitoramento de níveis de estoque

# Análise
#   Processar os pedidos dos clientes de uma empresa, onde dada uma lista com os pedidos feitos pelos clientes,
# levando em conta o nome do produto e sua quantidade, totalizar a demanda de cada produto.
#   ALém disso, descobrir se algum produto causará uma ruptura no estoque, ou seja, se algum produto possui mais 
# demanda do que a quantidade disponível no estoque.

# Definição de tipo de dados
#   Os tipos dos produtos serão representados por uma estrutura enumerada.
#   Os pedidos serão representodos por uma lista de pedidos, que por sua vez será representado por uma estrutura composta,
# indicando o tipo do produto e sua quantidade.
#   A totalização dos pedidos será representada por uma estrutura composta.
#   O estoque e a demanda serão representados pelo mesmo tipo de estrutura composta da totalização.

class TipoProduto(Enum):
    '''Representa o tipo(nome) dos produtos produzidos na empresa'''
    BOBINA = auto()
    CHAPA = auto()
    PAINEL = auto()

@dataclass
class Pedido:
    '''Pedido possível de ser feito de um produto, onde a quantidade precisa ser um número positivo maior que 0'''
    tipo: TipoProduto
    quantidade: int

@dataclass
class Totalizacao:
    '''Totalização de alguma quantidade de todos os produtos da empresa, representada por um número positivo'''
    bobina: int
    chapa: int
    painel: int

def totaliza_pedidos(pedidos: list[Pedido]) -> Totalizacao:
    '''
    Produz uma estrutura que totaliza a demanda de cada produto a partir de *pedidos*.

    Exemplos
    >>> totaliza_pedidos([])
    Totalizacao(bobina=0, chapa=0, painel=0)
    >>> totaliza_pedidos([Pedido(TipoProduto.BOBINA, 500), Pedido(TipoProduto.CHAPA, 100),\
                          Pedido(TipoProduto.BOBINA, 50), Pedido(TipoProduto.PAINEL, 1000),\
                          Pedido(TipoProduto.PAINEL, 200)])
    Totalizacao(bobina=550, chapa=100, painel=1200)
    >>> totaliza_pedidos([Pedido(TipoProduto.CHAPA, 400), Pedido(TipoProduto.PAINEL, 100),\
                          Pedido(TipoProduto.CHAPA, 200)])
    Totalizacao(bobina=0, chapa=600, painel=100)
    >>> totaliza_pedidos([Pedido(TipoProduto.PAINEL, 600), Pedido(TipoProduto.BOBINA, 3000),\
                          Pedido(TipoProduto.BOBINA, 200)])
    Totalizacao(bobina=3200, chapa=0, painel=600)
    >>> totaliza_pedidos([Pedido(TipoProduto.BOBINA, 50), Pedido(TipoProduto.CHAPA, 1000),\
                          Pedido(TipoProduto.BOBINA, 50)])
    Totalizacao(bobina=100, chapa=1000, painel=0)
    '''
    bobina = 0
    chapa = 0
    painel = 0
    for p in pedidos:
        if p.tipo.name == 'BOBINA':
            bobina = bobina + p.quantidade
        elif p.tipo.name == 'CHAPA':
            chapa = chapa + p.quantidade
        elif p.tipo.name == 'PAINEL':
            painel = painel + p.quantidade
    return Totalizacao(bobina, chapa, painel)

def ha_ruptura(estoque: Totalizacao, demanda: Totalizacao) -> list[TipoProduto]:
    '''
    Gera a partir do *estoque* e *demanda*, uma lista com os tipos de produtos com ruptura do estoque.

    Exemplos
    >>> # sem ruptura
    >>> ha_ruptura(Totalizacao(2000, 3218, 3920), Totalizacao(1600, 2032, 3291))
    []
    >>> # ruptura na bobina
    >>> ha_ruptura(Totalizacao(2000, 3218, 3920), Totalizacao(2500, 3218, 3201))
    [<TipoProduto.BOBINA: 1>]
    >>> # ruptura na chapa
    >>> ha_ruptura(Totalizacao(2000, 3218, 3920), Totalizacao(1020, 3282, 1000))
    [<TipoProduto.CHAPA: 2>]
    >>> # ruptura no painel
    >>> ha_ruptura(Totalizacao(2000, 3218, 3920), Totalizacao(2000, 1000, 4050))
    [<TipoProduto.PAINEL: 3>]
    >>> # ruptura em dois produtos
    >>> ha_ruptura(Totalizacao(2000, 3218, 3920), Totalizacao(2000, 4020, 5060))
    [<TipoProduto.CHAPA: 2>, <TipoProduto.PAINEL: 3>]
    >>> # ruptura em todos os produtos
    >>> ha_ruptura(Totalizacao(2000, 3218, 3920), Totalizacao(9900, 7483, 6823))        
    [<TipoProduto.BOBINA: 1>, <TipoProduto.CHAPA: 2>, <TipoProduto.PAINEL: 3>]
    '''
    produtos_com_ruptura = []
    if estoque.bobina < demanda.bobina:
        produtos_com_ruptura.append(TipoProduto.BOBINA)
    if estoque.chapa < demanda.chapa:
        produtos_com_ruptura.append(TipoProduto.CHAPA)
    if estoque.painel < demanda.painel:
        produtos_com_ruptura.append(TipoProduto.PAINEL)    
    return produtos_com_ruptura

# Vendas

# Análise
#   Determinar a receita e o lucro líquido da empresa a partir do relatório de vendas, onde cada venda possui uma nota que
# indica o nome do vendendor, o produto, a quantidade e o valor com desconto, desconto esse que pode ser oferecido aos clientes
# em cima de um preço de venda preestabelecido em uma tabela dos produtos em estoque. Vale notar que o preço ofertado com desconto
# não pode ser inferior ao preço de custo do produto.
#   Além disso, determinar os três vendedores que geraram mais lucro no mês, sabendo que cada vendedor pode fazer mais de uma venda
# mensal. Onde, no caso de empate de lucro dos vendedores, a ordenação será por ordem de venda, onde, caso a venda no *relatorio_vendas* 
# tenha sido processada antes, esse vendedor ficará na frente de quem ele empatou com.

# Definição de tipo de dados
#   O relatório de vendas será representaddo por uma lista de notas de venda.
#   As notas de venda serão representadas por uma estrutura composta, contendo o nome do vendedor, uma string, o tipo do produto,
# que já está sendo representado por uma estrutura enumerada, a quantidade do produto, representado por um número inteiro não negativo,
# e o valor com desconto, representado em reais, um número flutuante positivo.
#   Tanto a receita e o lucro líquido da empresa serão dados juntos em uma estrutura composta, ambos representados em reais.
#   O lucro que cada vendedor conseguiu ao mês será representado por uma estrutura composta, a fim de separar melhor as vendas.
#   Os três melhores vendedores serão dados por uma lista de nomes com ordem do melhor ao pior vendedor entre os três.

@dataclass
class NotaDeVenda:
    '''Nota de uma venda feita por um vendedor da empresa
    Caso o produto seja bobina, o valor com desconto deve ser maior que 50,00
    Caso o produto seja chapa, o valor com desconto deve ser maior que 40,00
    Caso o produto seja painél, o valor com desconto deve ser maior que 75,00
    '''
    vendedor: str
    produto: TipoProduto
    quantidade: int
    valor_com_desconto: float

@dataclass
class Faturamento:
    '''Faturamento de uma empresa, separado entre a receita bruta e o lucro líquido, que é a receita descontada os custos.'''
    receita: float
    lucro_liquido : float

@dataclass
class LucroIndividual:
    '''Lucro individual mensal de cada vendedor da empresa'''
    vendedor: str
    lucro: float

def calcular_lucro(venda: NotaDeVenda) -> float:
    '''
    Calcula o lucro de uma *venda* com base no valor com desconto cobrado e de acordo com o tipo do produto, levando
    como base o preço de custo de cada produto na empresa:
    Preço de custo da bobina = 50.0
    Preço de custo da chapa = 40.0
    Preço de custo do painél = 75.0
    Requer venda.valor_com_desconto maior que o preço de custo de cada produto.
    Requer venda.quantidade maior que 0

    Exemplos
    >>> calcular_lucro(NotaDeVenda('Wagner',TipoProduto.BOBINA, 300, 54.0))
    1200.0
    >>> calcular_lucro(NotaDeVenda('Andressa', TipoProduto.CHAPA, 143, 43.0))
    429.0
    >>> calcular_lucro(NotaDeVenda('Pedro', TipoProduto.PAINEL, 150, 83.0))
    1200.0
    '''
    assert venda.quantidade > 0
    if venda.produto.name == 'BOBINA':
        assert venda.valor_com_desconto > 50.0
        lucro = (venda.valor_com_desconto - 50.0) * venda.quantidade
    elif venda.produto.name == 'CHAPA':
        assert venda.valor_com_desconto > 40.0
        lucro = (venda.valor_com_desconto - 40.0) * venda.quantidade
    else:
        assert venda.valor_com_desconto > 75.0
        lucro = (venda.valor_com_desconto - 75.0) * venda.quantidade
    return lucro

def faturamento_mensal(relatorio_vendas: list[NotaDeVenda]) -> Faturamento:
    '''
    Determina o faturamento mensal da empresa, separado entre a receita bruta e o lucro líquido do mês, levando em conta
    os *relatorio_vendas*, uma lista das notas de vendas feitas pelos vendedores da empresa.

    Exemplos:
    >>> # sem nota de venda
    >>> faturamento_mensal([])
    Faturamento(receita=0.0, lucro_liquido=0.0)
    >>> # uma nota de venda
    >>> faturamento_mensal([NotaDeVenda('Gabriel', TipoProduto.CHAPA, 500, 47.5)])
    Faturamento(receita=23750.0, lucro_liquido=3750.0)
    >>> # duas notas de venda
    >>> faturamento_mensal([NotaDeVenda('Gabriel', TipoProduto.BOBINA, 100, 55.0),\
                            NotaDeVenda('Fulano', TipoProduto.PAINEL, 60, 80.0)])
    Faturamento(receita=10300.0, lucro_liquido=800.0)
    >>> # três notas de venda
    >>> faturamento_mensal([NotaDeVenda('Marco Aurélio', TipoProduto.PAINEL, 3000, 90.0),\
                            NotaDeVenda('Cláudia', TipoProduto.BOBINA, 400, 51.0),\
                            NotaDeVenda('Marcelo', TipoProduto.BOBINA, 50, 58.9)])
    Faturamento(receita=293345.0, lucro_liquido=45845.0)
    '''
    receita = 0.0
    lucro_liquido = 0.0
    for venda in relatorio_vendas:
        receita = receita + venda.quantidade * venda.valor_com_desconto
        lucro_liquido = lucro_liquido + calcular_lucro(venda)
    return Faturamento(receita, lucro_liquido)

def unificar_lucros(relatorio_vendas: list[NotaDeVenda]) -> list[LucroIndividual]:
    '''
    Unifica todo o lucro de um determinado vendedor no *relatorio_vendas* em um lucro só, somando o lucro de cada venda feita por
    cada vendedor.
    Requer *relatorio_vendas* não vazio.

    Exemplos
    >>> unificar_lucros([NotaDeVenda('Gabriel', TipoProduto.CHAPA, 500, 47.5)])
    [LucroIndividual(vendedor='Gabriel', lucro=3750.0)]
    >>> unificar_lucros([NotaDeVenda('Gabriel', TipoProduto.BOBINA, 100, 55.0),\
                         NotaDeVenda('Fulano', TipoProduto.PAINEL, 60, 80.0)])
    [LucroIndividual(vendedor='Gabriel', lucro=500.0), LucroIndividual(vendedor='Fulano', lucro=300.0)]
    >>> unificar_lucros([NotaDeVenda('Marco Aurélio', TipoProduto.PAINEL, 100, 90.0),\
                         NotaDeVenda('Cláudia', TipoProduto.BOBINA, 400, 51.0),\
                         NotaDeVenda('Marco Aurélio', TipoProduto.BOBINA, 50, 58.9)])
    [LucroIndividual(vendedor='Marco Aurélio', lucro=1945.0), LucroIndividual(vendedor='Cláudia', lucro=400.0)]
    >>> unificar_lucros([NotaDeVenda('Jonas', TipoProduto.PAINEL, 200, 85.0),\
                         NotaDeVenda('Lucas', TipoProduto.BOBINA, 500, 52.0),\
                         NotaDeVenda('Lucas', TipoProduto.PAINEL, 1300, 80.0), NotaDeVenda('Vitor', TipoProduto.BOBINA, 5000, 51.0), \
                         NotaDeVenda('Lucas', TipoProduto.BOBINA, 50, 58.0), NotaDeVenda('Vitor', TipoProduto.BOBINA, 200, 52.0)])
    [LucroIndividual(vendedor='Jonas', lucro=2000.0), LucroIndividual(vendedor='Lucas', lucro=7900.0), LucroIndividual(vendedor='Vitor', lucro=5400.0)]
    '''
    assert relatorio_vendas != []
    lucros = []
    for i in range(len(relatorio_vendas)):
        v = 0
        nao_encontrou = True
        while v < len(lucros) and nao_encontrou:
            if relatorio_vendas[i].vendedor == lucros[v].vendedor:
                lucros[v].lucro = lucros[v].lucro + calcular_lucro(relatorio_vendas[i])
                nao_encontrou = False
            v = v + 1
        if nao_encontrou == True:
            lucros.append(LucroIndividual(relatorio_vendas[i].vendedor, calcular_lucro(relatorio_vendas[i])))
    return lucros

def melhor_vendedor(vendedores: list[LucroIndividual]) -> LucroIndividual:
    '''
    Encontra o vendedor com o maior lucro analisando uma lista dos lucros individuais mensais dos *vendedores* da empresa.
    Requer *vendedores* não vazio. 

    Exemplos
    >>> melhor_vendedor([LucroIndividual('Wagner', 5810.0)])
    LucroIndividual(vendedor='Wagner', lucro=5810.0)
    >>> melhor_vendedor([LucroIndividual('Gabriel', 500.0),\
                         LucroIndividual('Fulano', 329.0)])
    LucroIndividual(vendedor='Gabriel', lucro=500.0)
    >>> melhor_vendedor([LucroIndividual('Marco Aurélio', 1945.0),\
                         LucroIndividual('Cláudia', 738.2),\
                         LucroIndividual('Caetano', 102.0)])
    LucroIndividual(vendedor='Marco Aurélio', lucro=1945.0)
    >>> melhor_vendedor([LucroIndividual('Jonas', 8743.0),\
                         LucroIndividual('Lucas', 4839.1),\
                         LucroIndividual('Pedro', 623.0),\
                         LucroIndividual('Vitor', 9273.0),\
                         LucroIndividual('Giovani', 829.3),\
                         LucroIndividual('Gabriel', 642.1)])
    LucroIndividual(vendedor='Vitor', lucro=9273.0)
    '''
    assert vendedores != []
    melhor_vendedor = vendedores[0]
    for vendedor in vendedores:
        if vendedor.lucro > melhor_vendedor.lucro:
            melhor_vendedor = vendedor
    return melhor_vendedor

def vendedores_premiados(relatorio_vendas: list[NotaDeVenda]) -> list[str]:
    '''
    Determina os três vendedores que geraram mais lucro no mês, levando em conta o *relatorio_vendas* mensal da empresa, retornando
    uma lista com o nome dos três melhores vendedores em ordem do melhor para o pior.
    No caso de empate de lucro dos vendedores, a ordenação será por ordem de venda, onde, caso a venda no *relatorio_vendas* tenha
    sido processada antes, esse vendedor ficará na frente de quem ele empatou com.
    Requer *relatorio_vendas* não vazio.

    Exemplos
    >>> vendedores_premiados([NotaDeVenda('Marco Aurélio', TipoProduto.PAINEL, 100, 90.0)])
    ['Marco Aurélio']
    >>> vendedores_premiados([NotaDeVenda('Marco Aurélio', TipoProduto.PAINEL, 100, 90.0),\
                              NotaDeVenda('Vitor', TipoProduto.BOBINA, 400, 51.0),\
                              NotaDeVenda('Marco Aurélio', TipoProduto.BOBINA, 50, 58.9)])
    ['Marco Aurélio', 'Vitor']
    >>> vendedores_premiados([NotaDeVenda('Marco Aurélio', TipoProduto.PAINEL, 100, 90.0),\
                              NotaDeVenda('Vitor', TipoProduto.BOBINA, 400, 51.0),\
                              NotaDeVenda('Marco Aurélio', TipoProduto.BOBINA, 50, 58.9),\
                              NotaDeVenda('André', TipoProduto.BOBINA, 500, 52.0)])
    ['Marco Aurélio', 'André', 'Vitor']
    >>> vendedores_premiados([NotaDeVenda('Jonas', TipoProduto.PAINEL, 200, 85.0),\
                              NotaDeVenda('Lucas', TipoProduto.BOBINA, 500, 52.0),\
                              NotaDeVenda('Fulano', TipoProduto.PAINEL, 1300, 80.0),\
                              NotaDeVenda('Pedro', TipoProduto.BOBINA, 5000, 51.0), \
                              NotaDeVenda('João', TipoProduto.BOBINA, 50, 58.0),\
                              NotaDeVenda('Lucas', TipoProduto.BOBINA, 200, 52.0)])
    ['Fulano', 'Pedro', 'Jonas']
    '''
    assert relatorio_vendas != [] 
    melhores = []
    lista_unificada = unificar_lucros(relatorio_vendas)
    for i in range(len(lista_unificada)):
        melhor = melhor_vendedor(lista_unificada)
        melhores.append(melhor.vendedor)
        # remover melhor da lista
        j = 0
        nao_removido = True
        while j < len(lista_unificada) and nao_removido:
            if lista_unificada[j].vendedor == melhor.vendedor:
                lista_unificada = lista_unificada[:j] + lista_unificada[j+1:]
                nao_removido = False
            j = j + 1
    return melhores[:3]
