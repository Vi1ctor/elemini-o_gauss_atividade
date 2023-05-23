# -*- coding: utf-8 -*-     #codificação do arquivo padronizada para UTF-8
import math    #importa o modulo math do python que nos possibilita usar funçções matemáticas úteis

def eliminacao_gauss(A, b):  #função que recebe como parametro uma matriz A, e um vetor relacionado ao termo independente
    n = len(A)  #determinar o tamanho do sistema linear  n= o número de equações/variáveis do sistema, no caso usado (3).

    for i in range(n):
        if A[i][i] == 0:
            raise ValueError('Divisão por zero encontrada!') #for para percorrer a diagnal principal(se achar um zero ocasionaria em uma indeterminação)
                                                             # Neste caso uma divisão por zero
        for j in range(i + 1, n):
            fator = A[j][i] / A[i][i]    #percorrem as linhas abaixo da diagonal principal e calculam o fator de eliminação


            for k in range(i, n):
                A[j][k] -= fator * A[i][k]

            b[j] -= fator * b[i]

        print("Matriz A após a etapa", i + 1)
        for row in A:
            print(row)
        print()

    x = [0] * n    #lista preenchida de zeros para guardar os resultados

    for i in range(n - 1, -1, -1):
        soma = sum(A[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (b[i] - soma) / A[i][i]

    return x


A = [[2, 1, -1],
     [-3, -1, 2],
     [-2, 1, 2]]

b = [8, -11, -3]

solucao = eliminacao_gauss(A, b)

print("Solução:")
for i, x in enumerate(solucao):
    print("x{} = {}".format(i+1, x))