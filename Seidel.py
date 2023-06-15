import numpy as np

A = np.array([
    [10, 2, 1],
    [1, 5, 1],
    [2, 3, 10]
])

b = np.array([
    [7],
    [-8],
    [6]
])

print("A solução exata é:\n", np.linalg.inv(A) @ b)


def gaussSeidel(A, b, p, x0, nMax):
    n, _ = np.shape(A)
    inv = np.linalg.inv(A * np.eye(n))
    B = np.eye(n) - inv @ A
    d = inv @ b
    xOld = np.copy(x0)
    x = np.copy(x0)
    it = 0
    er = 1
    while er >= 10 ** (-p) and it <= nMax:
        for i in range(n):
            x[i, 0] = B[i, 0:] @ x + d[i, 0]
        er = np.max(np.abs(x - xOld)) / np.max(np.abs(x))
        xOld = np.copy(x)
        it = it + 1
    return x, it


n, _ = np.shape(A)
x0 = np.zeros((n, 1))
x, it = gaussSeidel(A, b, 10, x0, 30)
print(f'O valor da solução após {it} iterações é:')
print(x)



def sistemaTriangularSuperior(U, y):
    n, nc = np.shape(U)
    x = np.zeros((n, 1))
    for i in range(n-1, -1, -1):
        x[i, 0] = (y[i, 0] - U[i, i+1:n] @ x[i+1:n, 0]) / U[i, i]
    return x

def eliminacaoG(A, b):
    n, _ = np.shape(A)
    Aa = np.concatenate((A, b), 1)
    for j in range(n-1):
        pivo = Aa[j, j]
        for i in range(j+1, n):
            fator = Aa[i, j] / pivo
            Aa[i, 0:] = Aa[i, 0:] - fator * Aa[j, 0:]
            print("Iteração", j+1)
            print(Aa)
            print()
    U = Aa[:, 0:n]
    y = Aa[:, n:]
    x = sistemaTriangularSuperior(U, y)
    return x

# Entrada da matriz A e vetor b
n = int(input("Digite o tamanho da matriz A: "))
A = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        A[i, j] = float(input(f"Digite o valor para A[{i+1}, {j+1}]: "))

b = np.zeros((n, 1))
for i in range(n):
    b[i, 0] = float(input(f"Digite o valor para b[{i+1}]: "))

x = eliminacaoG(A, b)
print("Solução:")
print(x)

