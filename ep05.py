#
# Siga as instruções que estão no enunciado do EP05
# para criar o arquivo ep05.py 
#
     
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
#####################################################################
# MÓDULOS A SEREM UTILIZADOS NO PROGRAMA
import random

#####################################################################
# CONSTANTES
# Constantes definem variáveis cujos valores NÃO DEVEM ser 
# alterados durante a execução do programa. Assim você deve
# escolher bem esses valores ANTES de executar o programa.
#
# O uso de constantes é um boa prática de programação
# pois constantes ajudam a melhorar a legibilidade
# de seus programas. Por convenção, para identificar
# as constantes em um programa, vamos usar nomes com todas 
# as letras maiúsculas.
#
# As constantes abaixo são fornecidas como exemplo. Você
# pode utilizar, ou não, qualquer uma delas e ainda criar 
# outras constantes se desejar.
#
DEBUG = True       # se True, pede para digitar a semente e mostra a senha
MENOR_VALOR = 0    # menor número sorteado
MAIOR_VALOR = 10000 # limite superior para o maior número sorteado (mais 1)
MAX_TENTATIVAS = 10 # número máximos de chutes permitidos
NUM_DIGITOS  = 4   # número de dígitos da senha

#####################################################################
def main():
    '''(None) -> None 

    Coloque sua solução individual abaixo, seguindo o enunciado 
    desse exercício na página da disciplina.

    Siga as instruções para entrega disponíveis em:
    https://paca.ime.usp.br/mod/page/view.php?id=42515
    
    '''

    print("Bem vindo ao MASTER BIME!!")
    # as linhas abaixo vão ajudar durante o desenvolvimento e depuração 
    # para deixar de executá-las, basta modificar a constante DEBUG para 
    # False. Mas lembre-se de deixá-la True antes de enviar esse EP.
    if DEBUG:
        semente = int(input("Digite o valor da semente: "))
        random.seed(semente)
        senha = random.randrange(MENOR_VALOR, MAIOR_VALOR)
        print("Número sorteado: ", senha)
    else:
        senha = random.randrange(MENOR_VALOR, MAIOR_VALOR)
        
    # escreva seu programa a seguir
    n=MAX_TENTATIVAS
    cont=1
    chute=int(input("Digite seu chute: "))
    print("Dígitos em posições corretas do chute",cont,"/",n,":",em_posicoes_certas(senha,chute,NUM_DIGITOS))
    print("Dígitos certos do chute",cont,"/",n,": ",digitos_certos(senha,chute))
    while cont<n and chute!=senha:
        chute=int(input("Digite seu chute: "))
        cont+=1
        print("Dígitos em posições corretas do chute",cont,"/",n,": ",em_posicoes_certas(senha,chute,NUM_DIGITOS))
        print("Dígitos certos do chute",cont,"/",n,":",digitos_certos(senha,chute))
    if chute!=senha:
        print("Ha ha, você perdeu!")
    else:
        print("Parabéns, você acertou!")

    print("Fim do jogo.")

def em_posicoes_certas(senha,chute,NUM_DIGITOS):
    '''recebe 3 números inteiros e devolve um número inteiro de 0 a 4'''
    cont=1
    c=0
    while cont<=NUM_DIGITOS:
        x= senha%10
        y= chute%10
        if x==y:
            c+=1
        else:
            c+=0
        senha=senha//10
        chute=chute//10
        cont+=1
    return c

def digitos_certos(senha,chute):
    '''recebe 2 números inteiros e devolte um número inteiro de 0 a 4'''
    a=(senha//(10**0))%10
    b=(senha//(10**1))%10
    c=(senha//(10**2))%10
    d=(senha//(10**3))%10
    j=(chute//(10**0))%10
    k=(chute//(10**1))%10
    l=(chute//(10**2))%10
    m=(chute//(10**3))%10
    pontos=0
    if j==a:
        pontos+=1
    else:
        if j==b:
            pontos+=1
        else:
            if j==c:
                pontos+=1
            else:
                if j==d:
                    pontos+=1
                else:
                    pontos+=0
    if k==a and j!=k:
        pontos+=1
    else:
        if k==b and b==a:
            pontos+=1
        elif k==b and k!=j:
            pontos+=1
        else: 
            if k==c and j!=k:
                pontos+=1
            elif k==c and (c==a or c==b):
                pontos+=1
            else:
                if k==d and j!=k:
                    pontos+=1
                elif k==d and (d==a or d==b or d==c):
                    pontos+=1
                else: 
                    pontos+=0
    
    if l==a and j!=l and k!=l:
        pontos+=1
    else:
        if l==b and j!=l and k!=l:
            pontos+=1
        elif l==b and b==a and (j!=l or k!=l):
            pontos+=1
        else:
            if l==c and j!=l and k!=l:
                pontos+=1
            elif l==c and c==a and c==b:
                pontos+1
            elif l==c and c==a:
                if k!=l or l!=j:
                    pontos+=1
                else:
                    pontos+=0
            elif l==c and c==b:
                if k!=l or j!=l:
                    pontos+=1
                else:
                    pontos+=0  
            else:
                if l==d and j!=l and k!=l:
                    pontos+=1
                elif l==d and (d==a or d==b or d==c) and (j!=l or k!=l):
                    pontos+=1
                elif l==d and ((d==a and d==b)or(d==a and d==c)or(d==b and d==c)):
                    pontos+=1
                else:
                    pontos+=0
    if m==a and j!=m and k!=m and l!=m:
        pontos+=1
    else:
        if m==b and j!=m and k!=m and l!=m:
            pontos+=1
        elif m==b and b==a and ((j!=m and k!=m)or(j!=m and l!=m)or(k!=m and l!=m)):
            pontos+=1
        else:
            if m==c and j!=m and k!=m and l!=m:
                pontos+=1
            elif m==c and (c==a or c==b) and ((j!=m and k!=m)or(j!=m and l!=m)or(k!=m and l!=m)):
                pontos+=1
            elif m==c and c==a and c==b and (j!=m or k!=m or l!=m): 
                pontos+=1
            else: 
                if m==d and j!=m and k!=m and l!=m:
                    pontos+=1
                elif m==d and (d==a or d==b or d==c) and ((j!=m and k!=m)or(j!=m and l!=m)or(k!=m and l!=m)):
                    pontos+=1
                elif m==d and ((d==a and d==b)or(d==a and d==c)or(d==b and d==c)) and (j!=m or k!=m or l!=m):
                    pontos+=1
                elif m==d and d==a and d==b and d==c:
                    pontos+=1
                else:
                    pontos+=0
    return pontos

# =========================================================
# NÃO MODIFIQUE AS LINHAS ABAIXO
# ELAS SÃO NECESSÁRIAS PARA O CORRETOR AUTOMÁTICO
# =========================================================

if __name__ == "__main__":
    main()
