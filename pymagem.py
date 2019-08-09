# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS
# NÃO INCLUA NENHUM import ...
#------------------------------------------------------------------

'''

    Nome: Emerson Silva Aragão
    NUSP: 11371583

    Ao preencher esse cabeçalho com o meu nome e o meu número USP,
    declaro que todas as partes originais desse exercício programa (EP)
    foram desenvolvidas e implementadas por mim e que portanto não 
    constituem desonestidade acadêmica ou plágio.
    Declaro também que sou responsável por todas as cópias desse
    programa e que não distribui ou facilitei a sua distribuição.
    Estou ciente que os casos de plágio e desonestidade acadêmica
    serão tratados segundo os critérios divulgados na página da 
    disciplina.
    Entendo que EPs sem assinatura devem receber nota zero e, ainda
    assim, poderão ser punidos por desonestidade acadêmica.

    Abaixo descreva qualquer ajuda que você recebeu para fazer este
    EP.  Inclua qualquer ajuda recebida por pessoas (inclusive
    monitores e colegas). Com exceção de material de MAC0110, caso
    você tenha utilizado alguma informação, trecho de código,...
    indique esse fato abaixo para que o seu programa não seja
    considerado plágio ou irregular.

    Exemplo:

        A monitora me explicou que eu devia utilizar a função int() quando
        fazemos leitura de números inteiros.

        A minha função quicksort() foi baseada na descrição encontrada na 
        página https://www.ime.usp.br/~pf/algoritmos/aulas/quick.html.

    Descrição de ajuda ou indicação de fonte:

'''
#-------------------------------------------------------------------------- 


class Pymagem:
    '''
    Implementação da classe Pymagem que tem o mesmo comportamento descrito 
    no enunciado.
    '''

    # escreva aqui os métodos da classe Pymagem
    def __init__(self, nlin, ncol, valor = 0):
        self.nlin = nlin
        self.ncol = ncol
        self.valor = valor
        M = []
        for linha in range(nlin):
            linha_de_M = []
            for coluna in range(ncol):
                linha_de_M.append(valor)
            M += [linha_de_M]


        self.matriz = M

    def __str__(self):
        M = ''
        for linha in range(self.nlin):
            linha_de_M = ''
            for coluna in range(self.ncol):
                if coluna != self.ncol - 1:
                    linha_de_M += '{0}, '.format(self.valor)
                else:
                    linha_de_M += '{0}\n'.format(self.valor)

            M += linha_de_M

        return M

    def size(self):
        return (self.nlin, self.ncol)



    def get(self, lin, col):
        imagem = self.matriz
        return imagem[lin][col]



    def put(self, lin, col, value):
        imagem = self.matriz
        imagem[lin][col] = value



    def crop(self, tlx=0, tly=0, brx=None, bry=None):
        if brx == None:
            brx = self.nlin
        if bry == None:
            bry = self.ncol
        imagem = self.matriz
        nlin = brx - tlx
        ncol = bry - tly


        recorte = []
        for linha in range(nlin):
            linha_recorte = []
            for coluna in range(ncol):
                linha_recorte.append(imagem[tlx + linha][tly + coluna])
            recorte += [linha_recorte]

        return recorte







