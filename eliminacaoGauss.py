import numpy as np

def sistemaTriangularSuperior(U, y):
    n, nc = np.shape(U)
    x = np.zeros((n, 1))
    for i in range(n-1, -1, -1):
        x[i, 0] = (y[i, 0] - U[i, i:n] @ x[i:n, 0]) / U[i, i]
    return x

def eliminacaoG(A, b):
    n, _ = np.shape(A)
    Aa = np.concatenate((A, b), 1)
    for j in range(n-1):
        pivo = Aa[j, j]
        for i in range(j+1, n):
            fator = Aa[i, j] / pivo
            Aa[i, 0:] = Aa[i, 0:] - fator * Aa[j, 0:]
    U = Aa[0:, 0:n]
    y = Aa[0:, n:]
    x = sistemaTriangularSuperior(U, y)
    return x

n = int(input("Digite o tamanho da matriz: "))
A = np.zeros((n, n))
b = np.zeros((n, 1))

print("Digite os elementos da matriz A:")
for i in range(n):
    for j in range(n):
        A[i, j] = float(input(f"A[{i+1}, {j+1}]: "))

print("Digite os elementos do vetor b:")
for i in range(n):
    b[i, 0] = float(input(f"b[{i+1}]: "))

x = eliminacaoG(A, b)
print("A solução x é:")
print(x)
