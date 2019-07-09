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

# 
# =================================================================------------------------------------------------------------------
# 
def main():
    '''
        Modifique essa função, escrevendo os seus testes.
    '''
    ## Coloque aqui os seus testes.

    mat = [ [1,2,3],[4,5,6] ]
    print( to_string(mat, 'Bonitona') )
    mat1=crie(2,3,2)
    print()
    copia=clone(mat1)
    copia[1][2]+=9
    print(to_string(mat1,'criada'))
    print()
    print(to_string(copia,'copia'))
    print()
    dif=subtraia(mat,mat1)
    print(to_string(dif,'subtraia'))
    limiarize(mat,5,1,0)
    print(to_string(mat,'pós limiarize'))


#------------------------------------------------------------------
#
def crie ( nlins, ncols, vini = 0 ):
    ''' (int, int, int) -> list

    RECEBE três inteiros, `nlins`, `ncols` e `vini`. 
    RETORNA uma matriz de dimensão `nlins` x `ncols` em que o valor do elemento
    em cada posição [lin][col] deve ser valor `vini`.
    '''
    # Substitua o código abaixo com a sua solução
    M=[]
    for i in range(nlins):
        M+=[[vini]*ncols]
    
    return M

#------------------------------------------------------------------
#
def clone ( mat ):
    ''' (list) -> list

    RECEBE uma matriz bidimensional mat e RETORNA um clone de mat.
    '''
    # Substitua o código abaixo com a sua solução
    
    CM=[]
    for i in mat:
        CM.append(i[:])
        
        
        
    return CM

#------------------------------------------------------------------
#
def subtraia ( mat1, mat2 ):
    ''' (list) -> list

    RECEBE duas matrizes bidimensionais `mat1` e `mat2` de números inteiros 
    e de mesma dimensão.
    RETORNA uma a matriz dif de mesma dimensão das matrizes. O valor 
    de cada posição [lin][col] deve ser dado por
 
        dif[lin][col] = mat1[lin][col] - mat2[lin][col].
    '''
    # Substitua o código abaixo com a sua solução
    nlins=len(mat1)
    ncols=len(mat1[0])
    dif=crie(nlins,ncols,0)
    for i in range(nlins):
        for j in range(ncols):
            dif[i][j]+=mat1[i][j]-mat2[i][j]
            
    return dif
    
#------------------------------------------------------------------
#
def to_string ( mat , nome = 'matriz' ):
    ''' (list, str) -> str

    RECEBE uma matriz bidimensional `mat` de números inteiros e uma string `nome`.  
    RETORNA uma string utilizada por print() para exibir a matriz, como por exemplo 
    em 

        print(to_string(bla, 'minha matriz bla'))

    que exibe o conteúdo da matriz bla.

    No que segue, por linha da string retornada entenda uma substring seguida 
    do caractere "\n" de mudança de linha.

    A string retornada deve ter o seguinte formato:

      - a primeira linha da string contém a string `nome`;
      - as demais linhas da string contém uma a uma as linhas da matriz
        `mat`.

    Os valores da matriz devem representados na string retornada por substring 
    de mesmo tamanho. O efeito será que ao exibirmos uma matriz bla através de
    print(to_string(bla)) os valores de cada coluna estarão alinhados.

    Reserve ao menos 4 posições para exibir cada número inteiro.
    '''
    # Substitua o código abaixo com a sua solução
    S="%s \n"%(nome)
    nlins=len(mat)
    ncols=len(mat[0])
    for i in range(nlins):
        for j in range(ncols):
            S+="%4d"%(mat[i][j])
        S+="\n"
        
            
    
    return S

#------------------------------------------------------------------
#
def limiarize ( mat, limite, alto=255, baixo=0 ):
    ''' (list, int, int, int) -> None
    RECEBE uma matriz bidimensional `mat` de números inteiros e três inteiros
    `limite`, `alto` e baixo.

    A função deve MODIFICAR `mat` da sequinte forma.
 
    Cada posição [lin][col] de `mat` em que mat[lin][col] > `limite`,
    deve receber o valor `alto`. As demais posições devem receber o valor 
    `baixo`.
    '''
    # Substitua o código abaixo com a sua solução
    nlins=len(mat)
    ncols=len(mat[0])
    for i in range(nlins):
        for j in range(ncols):
            if mat[i][j]>limite:
                mat[i][j]=alto
            else:
                mat[i][j]=baixo
    

#######################################################
###                 FIM                             ###
#######################################################
# 
# Esse if serve para rodar a main() dentro do Spyder.

if __name__ == '__main__':
    main()
