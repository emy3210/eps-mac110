# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS E ATRIBUTOS
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

##################################################################
def main():
    '''(None) -> None

    Coloque sua solução individual abaixo, seguindo o enunciado do
    exercício disponível na página da disciplina.

    Siga as instruções para entrega disponíveis em:
    https://paca.ime.usp.br/mod/page/view.php?id=42515
    '''
    # escreva o corpo da função main() a seguir
    # cuidado com a tabulação
    N=int(input("digite N:"))
    A=int(input("Digite um número para A: "))
    E=int(input("Digite um número para E: "))
    
    cont=0
    seq=0
    while cont<N:
        cont+=1
        X=float(input("digite x: "))
        Y=float(input("Digite y: "))
        if acertou_tiro(X,Y):
            print("    Acertou")
            seq+=A*(10**(N-cont))
        else:
            print("    Errou")
            seq+=E*(10**(N-cont))
    print("Código: ",seq)
    
    
        
##################################################################
def acertou_tiro(x, y):
    '''(float ou int, float ou int) -> bool

    Esta função recebe dois valores x e y, que representam as
    coordenadas (x,y) de um mapa. Se (x,y) for um ponto pertencente a área
    definida como alvo, essa função retornará True, 
    caso contrário, retornará False. 
    '''
    # escreva o corpo de sua função acertou_tiro() a seguir
    # cuidado com a tabulação
    Acertou=False
    if y>12 or y<=0:
        Acertou=False
    elif x<-4 or x>=6:
        Acertou=False
    elif -0.5<=x<=0.5 and 9.5<=y<10.5:
        Acertou=True
    elif x==1 and y==9:
        Acertou=False
    elif x==-1 and y==9:
        Acertou=False
    elif -1<x<1 and 9<=y<11:
        Acertou=False
    elif 4<=x<6 and 8<y<=10:
        Acertou=False
    elif x==4 and y==8:
        Acertou=False
    elif 2<=x<4 and 8<y<=10:
        Acertou=False
    elif y==8 and x<=4:
        Acertou=False
    elif -4<x<-2 and 8<y<=10:
        Acertou=False
    elif x==0 and y==4:
        Acertou=True
    elif y<8 and 0<=x<=4 and y-x>4:
        Acertou=False
    elif y<8 and -4<=x<0 and y+x>4:
        Acertou=False
    elif x==5 and y==7:
        Acertou=False
    elif x==4 and y==6:
        Acertou=False
    elif 4<x<=5 and 6<=y<7:
        Acertou=False
    elif x==-2 and y==4:
        Acertou=False
    elif x==-3 and y==5:
        Acertou=False
    elif x==2 and y==4:
        Acertou==False
    elif x==3 and y==5:
        Acertou==False
    elif -3<=x<-2 and 4<=y<5:
        Acertou=False
    elif 2<x<=3 and 4<=y<5:
        Acertou=False
    elif (x==1 or x==-1) and y==2:
        Acertou=False
    elif -1<=x<=1 and 2<y<=3:
        Acertou=False
    elif 0<=x<=6 and y-x<=0:
        Acertou=False
    elif -4<=x<0 and y+x<0:
        Acertou=False
    else:
        Acertou=True
    
    
    return Acertou
    

#######################################################
###                 FIM   DA   MAIN()               ###
#######################################################
#
#  Não modifique as linhas abaixo
#
# Esse if serve para rodar a main() dentro do Spyder
# e não atrapalhar o corretor automático

if __name__ == '__main__':
    main()
