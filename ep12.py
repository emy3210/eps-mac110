# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS OU ATRIBUTOS
# NÃO APAGUE OS DOCSTRINGS 
#------------------------------------------------------------------
     
'''
    Nome: Emerson Silva Aragão
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
# Constantes
# use essas constantes caso desejar
DNA = 'ATCG'
GAP = '_'


#------------------------------------------------------------------
def main():
    '''
        Modifique essa função, escrevendo os seus testes.
    '''

    ## Escreva aqui os testes para a função gera_gaps
    x=gera_gaps( 'AT_G')
    print(x)
    
    ## Escreva aqui os testes para a função pontuação
    #  
    s=conte_permut('G_G_')
    print(s)
    print("Fim dos meus testes.")


#------------------------------------------------------------------
#
def gera_gaps( dna ):
    ''' ( str ) -> list
    RECEBE uma string `dna` representando uma fita de DNA com os
    símbolos 'A', 'T', 'C', 'G' e '_' (um gap).
    RETORNA uma lista com todas as variações de dna com um gap a 
    mais e sem repetição.

    exemplos: 
    In  [1]: gera_gaps( 'T' )
    Out [1]: ['_T', 'T_']
    
    In  [2]: gera_gaps( 'CA' )
    Out [2]: ['_CA', 'C_A', 'CA_']
    
    In  [3]: gera_gaps( 'AT_G')
    Out [3]: ['_AT_G', 'A_T_G', 'AT__G', 'AT_G_'] 
    '''
    # modifique o código abaixo para conter a sua solução.
    lista=[]
    y=conte_permut(dna)
    n=0
    i=0
    while n<y:
        inicio=dna[0:i]
        meio=GAP
        fim=dna[i:]
        novo_dna=inicio+meio+fim
        if not novo_dna in lista:
            lista+=[novo_dna]
            n+=1
            i+=1
        else:
            i+=1
    return lista

#------------------------------------------------------------------
#
def pontuacao(m, d, g, s, t):
    ''' (int, int, int str, str) -> int
    RECEBE 3 inteiros não negativos `m`, `d`, e `g` e duas strings `s` e `t` 
    de mesmo tamanho com zero ou mais gaps representando fitas de DNA.
 
    RETORNA a pontuação do alinhamento entre `s` e `t` calculada da seguinte 
    forma:
 
       * duas letras iguais alinhadas contam m pontos, 
       * duas letras diferentes alinhadas contam −d pontos (subtrai d pontos) e 
       * uma letra alinhada com um gap ou dois gaps alinhados contam −g pontos.

    Exemplos:
    In  [1]: pontuacao(5, 5, 3, 'T_CGTAC', 'ATCG___')
    Out [1]: -7 
    
    In  [2]: pontuacao(1, 5, 3, 'T_CGTAC', 'ATCG___')
    Out [2]: -15
    
    In  [3]: pontuacao(5, 5, 3, 'T_CGTA', 'ATCG__')
    Out [3]: -4
    '''
    # modifique o código abaixo para conter a sua solução.
    x=len(s)
    soma=0
    for i in range(x):
        fita_s=s[i]
        fita_t=t[i]
        if fita_s in DNA and fita_t in DNA:
            if fita_s==fita_t:
                soma+=m
            else:
                soma-=d
        else:
            soma-=g
            
    return soma
    
#----------------------------------------------------------------------------
def conte_permut(dna):
    '''(str) -> int
    RECEBE uma fita de dna e calcula o número de permutações possíveis 
    ao adicionar um gap a esta fita'''
    
    x=len(dna)
    g=0
    for i in range(x):
        if GAP == dna[i]:
            g+=1
    calc=x+1-g
    return calc
        
#######################################################
###                 FIM                             ###
#######################################################
# 
# Esse if serve para rodar a main() dentro do Spyder.

if __name__ == '__main__':
    main()
