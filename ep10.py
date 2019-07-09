# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS E ATRIBUTOS
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
#####################################################################
# MÓDULOS UTILIZADOS NO PROGRAMA
import math        # math.exp(), math.sqrt() e math.pi   
import random      # random.seed(), random.choices()
import numpy as np # np.arange()
import matplotlib.pyplot as plt # plt.subplots(), plt.bar(),  plt.xlabel(),
                                # plt.ylabel(), plt.title(), plt.show()

#####################################################################
#  CONSTANTES
# 
SEED   = 123456 # para gerador aleatório; garante reproducibilidade dos experimentos
CARA   = 'H'    # possível valor em uma amostra aleatória produzida por random.choices()
COROA  = 'T'    # possível valor em uma amostra aleatória produzida por random.choices()
SIM    = 's'

#####################################################################
def main():
    '''(None) -> None

    A função main() serve como unidade de teste para as funções.
    Pode ser alterada à vontade.
    Não será avaliada, a menos que produza erros ao executarmos o programa.
    '''
    random.seed(SEED) # para efeito de reproducibilidade

    teste = True
    while teste:
        # leia parâmetros
        n = int(input("Digite o número n de lançamentos da moeda: "))
        p = float(input("Digite a probabilidade de obtermos cara: "))
        t = int(input("Digite o número t de amostras: "))
        s = input("Deseja que ver a distribuição normal? ('s' para sim e o resto para não): ")
        if s == SIM:
            mostre_normal = True
        else:
            mostre_normal = False
            
        # obtenha o número de caras em t amostra aleatórias de n lançamentos uma moeda
        caras = caras_em_amostras(n, t, p)

        # obtenha a frequência de cada valor k nas t amostras
        freq_obs = frequencias_observadas(caras, n)

        # construa a distribuição binomial Bnp[] para os parâmetros n e p.
        Bnp = distribuicao_binomial(n, p)

        # construa a lista freq_esp[] das frequências esperadas de caras em t amostras,
        # segundo a distribuição binomial
        freq_esp = frequencias_esperadas(Bnp, t)
        
        # apresente as frequências observadas e esperadas
        print("Frequências observadas (esperadas)")
        for i in range(n+1):
            print("%8d: %7d (%g)"%(i, freq_obs[i], freq_esp[i]))

        # desenhe os gráficos    
        plot(freq_obs, freq_esp, n, t, p, mostre_normal)

        resp = input("Deseja continuar? ('s' para sim e o resto para não): ")
        if resp != 's' and resp != 'S':
            teste = False

#####################################################################
def caras_em_amostra_aleatoria(n, p=0.5, mostra_amostras=False):
    '''(int, float) -> int

    RECEBE um inteiro n e a probabilidade p de observarmos cara em 1
    lançamento de uma moeda.

    A função gera uma amostra aleatória com os resutados de n lançamentos  
    de uma moeda em que a probabilidade de obter cara é p e RETORNA 
    o número observado de caras na amostra aleatoria gerada.
 
    Se mostra_amostras é True a função deve imprimir a amostra aleatoria
    gerada.

    Uma amostra será representada através de uma lista com as strings
    'H' e 'T'. A string 'H' deve ser interpretada como cara e a 
    string 'T' como coroa.

    Para gerar a amostra aleatória a função deve usar a função 
    random.choices() do módulo random. A linha

        amostra_aleatoria = random.choices("HT", weights=(p, 1-p), k=n) 

    atribui à variável amostra_aleatoria uma lista de comprimento n em 
    que cada posição contém 
        - a string 'H' com probabilidade p ou 
        - a string 'T' com probabilidade 1-p.

    '''
    amostra_aleatoria = random.choices("HT", weights=(p, 1-p), k=n)
    # modifique o código abaixo para conter a sua solução.
    if mostra_amostras:
        print(amostra_aleatoria)
        
    cara=0
    for i in range(n):
        if 'H'== amostra_aleatoria[i]:
            cara+=1
        
    return cara


#####################################################################        
def caras_em_amostras(n, t, p=0.5, mostra_amostras=False):
    '''(int, int, float) -> list

    RECEBE inteiros positivos n e t e uma probabilidade p de observarmos
    cara em 1 lançamento de uma moeda. 

    RETORNA uma lista de comprimento t em que cada posição contém o 
    número observado de caras em uma amostra aleatória com os resultados
    de n lançamentos de uma moeda em que a probabilidade de obter cara é p.

    Se mostra_amostras é True a função deve imprimir cada uma das t amostras
    aleatorias geradas.
    '''
    # modifique o código abaixo para conter a sua solução.
    amostra=0
    caras=[]
    while amostra<t:
        caras+=[caras_em_amostra_aleatoria(n,p,mostra_amostras)]
        amostra+=1
        
    return caras
    
    

#####################################################################
def frequencias_observadas(no_caras, n):
    '''(list, int) -> list

    RECEBE uma lista no_caras com os números observados de caras 
    em t amostras aleatorias com os resultados de n lançamentos 
    de uma moeda.

    RETORNA uma lista de comprimento n+1 em que cada posição k contém a
    frequência de k na lista.
    '''
    # modifique o código abaixo para conter a sua solução.
    k=no_caras
    lista_f=[0]*(n+1)
    m=len(no_caras)
    for ind in range(m):
        j=k[ind]
        lista_f[j]+=1
        
    return lista_f


#####################################################################
def distribuicao_binomial(n, p=0.5):
    '''(int, float) -> list

    RECEBE um número n de lançamentos de uma moeda e uma probabilidade
    p de observarmos cara em 1 lançamento.

    RETORNA a distribuição binomial para os parâmetros n e p.
    '''
    # modifique o código abaixo para conter a sua solução.
    k=0
    distribuicao=[]
    while k<=n:
        coroa=n-k
        p_cara=1
        for i in range(0,k,1):
            p_cara=p*p_cara
            
        p_coroa=1
        for i in range(0,coroa,1):
            p_coroa=(1-p)*p_coroa
            
        p_final=combinacao(n,k)*p_coroa*p_cara
        distribuicao+=[p_final]
        
        k+=1
    return distribuicao



#####################################################################
def frequencias_esperadas(Bnp, t):
    '''(list, int) -> list

    RECEBE uma distribuição binomial Bnp e um inteiro t.

    RETORNA uma lista de comprimento n+1 em que cada posição k contém a
    frequência esperada de obtermos k caras em t amostras de n lançamentos
    de uma moeda SEGUNDO a distribuição binomial.
    '''
    # modifique o código abaixo para conter a sua solução.
    lista_esp=Bnp[:]
    n=len(lista_esp)
    for k in range(n):
        lista_esp[k]*=t
   
    return lista_esp
    
#######################################################################
def fatorial(n):
    num=n
    fat=1
    cont=1
    while cont<=num:
        fat*=(cont)
        cont+=1
    return fat
######################################################################    
def combinacao(x,y):
    n= fatorial(x)
    k= fatorial(y)
    nk=fatorial(x-y)
    return n/(k*nk)
#####################################################################
#
#  Desse ponto em diante não há nada a ser feito
#
#####################################################################

#####################################################################
def phi(x, mu=0, sigma2=1):
    '''(float, float, float) -> float

    RECEBE reais x, mu e sigma2.

    RETORNA o valor da função "densidade de probabilidade" 
    da distribuição normal de média mu e variância sigma2 no 
    ponto x.
    '''
    return math.exp(-(x-mu)*(x-mu)/(2*sigma2)) / math.sqrt(2*math.pi*sigma2)

#-------------------------------------------------------------
def plot(y_obs, y_esp, n, t, p, mostre_normal=False):
    '''(list, list, int, int, float, bool) -> None

    Exibe o gráfico de barras (azuis) representando a frequência observada.

    Exibe um gráfico pontilhado (vermelha) representando a frequência
    esperada segundo a distribuição binomial.

    Se mostre_normal é True exibe um gráfico de pontos (verdes)
    próximos representando a frequência esperada segundo a função
    densidade (phi()) da distribuição normal.
    '''
    # crie um gráfico
    fig, ax = plt.subplots()
    x = np.arange(n+1)
    
    # desenhe barras para representar com a frequência observada
    plt.bar(x, y_obs)

    # desenhe o gráfico com as frequência esperadas obtidas através da distribuição binomial
    ax.plot(x, y_esp, color='red', marker='^', linestyle='dashed', linewidth=1, markersize=6)

    # devemos desenhar a distribuição normal?
    if mostre_normal:
        
        # média da distribuição binomail
        mu = n*p
        
        # variância de distribuição binomial
        sigma2 = n*p*(1-p)
        
        # domínimo para o cálculo dos valores da função densidade da distribuição (continua) normal
        z = np.arange(0, n+1, 0.1)
        
        # valores da distribuição normal
        N = [0]*len(z) # np.zeros(len(z))
        for i in range(len(z)):
            N[i] = phi(z[i], mu, sigma2) * t
            
        # desenhe os pontos
        ax.plot(z, N, color='green', marker='*', linestyle='solid', linewidth=.5, markersize=2)

    # rotulos
    plt.xlabel('no. de caras')
    plt.ylabel('frequências')
    plt.title('Histograma para n=%d, t=%d e p=%g'%(n,t,p))
    plt.grid(True)

    # desenhe
    plt.show()

#=====================================================================
# Não modifique as linhas abaixo
# Esse if serve para rodar a main() dentro do Spyder
# e não atrapalhar o corretor automático

if __name__ == '__main__':
    main()
