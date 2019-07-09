# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS OU ATRIBUTOS
# NÃO APAGUE OS DOCSTRINGS 
#------------------------------------------------------------------
     
'''
    Nome:Emerson Silva Aragão
    NUSP:11371583

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

import ep15
# crie(), clone(), subtraia(), to_string() e limiarize()

# # =================================================================------------------------------------------------------------------
def main():
    '''
        Modifique essa função, escrevendo os seus testes.
    '''
    # coloque aqui os seus testes
    M=[[1,2,3],[9,2,5]]
    aux=ep15.clone(M)
    print(ep15.to_string(M,'M'))
    erosao(M)
    print(ep15.to_string(M,'m'))
    
    print(ep15.to_string(segmentacao_SME(aux)))
#------------------------------------------------------------------
#
def segmentacao_SME( img, viz = 3 ):
    ''' (list, int) -> list

    RECEBE uma imagem img. 
    APLICA o filtro de erosão com vizinhança viz.
    RETORNA a imagem resultado da subtração entre img e sua 
    erosão. Veja exemplos no enunciado.
    '''
    copia=ep15.clone(img)
    erosao(copia,viz)
    M=ep15.subtraia(img,copia)
    return M


#------------------------------------------------------------------
#
def erosao ( img, viz = 3 ):
    ''' (list, int) -> None

    RECEBE uma imagem img (lista de listas) em níveis de cinza e
    um inteiro viz.

    MODIFICA img de tal forma que, ao final, cada pixel 
    [lin][col] seja o valor mínimo da vizinhança de tamanho viz
    centrada no pixel [lin][col] da imagem original.
 
    Observe que essa região é menor quando o pixel [lin][col] 
    está próxima de uma borda.

    Você pode supor que viz será sempre um número ímpar, que define
    um quadrado centrado em um ponto [lin][col].
    '''
    copia=ep15.clone(img)
    nlin=len(img)
    ncol=len(img[0])
    for l in range(nlin):
        for c in range(ncol):
            k=viz//2
            for sl in range(l-k,l+1+k):
                for sc in range(c-k, c+1+k):
                    if 0<=sl<nlin and 0<=sc<ncol:
                        if img[l][c]>copia[sl][sc]:
                            img[l][c]=copia[sl][sc]

#######################################################
###                 FIM                             ###
#######################################################
# 
# Esse if serve para rodar a main() dentro do Spyder.

if __name__ == '__main__':
    main()
