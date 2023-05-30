import numpy as np

def eliminacao_gauss(A, b):
    n = len(A)
    for k in range(n-1):
        for i in range(k+1, n):
            fator = A[i, k] / A[k, k]
            for j in range(k, n):
                A[i, j] = A[i, j] - fator * A[k, j]
            b[i] = b[i] - fator * b[k]
    return A, b

def gauss_seidel(A, b, N, epsilon):
    n = len(A)
    x = np.zeros(n)
    for _ in range(N):
        x_prev = np.copy(x)
        for i in range(n):
            sum1 = np.dot(A[i, :i], x[:i])
            sum2 = np.dot(A[i, i+1:], x_prev[i+1:])
            x[i] = (b[i] - sum1 - sum2) / A[i, i]
        if np.linalg.norm(x - x_prev) < epsilon:
            break
    return x

# Exemplo de uso
n = int(input("Digite o tamanho da matriz (n): "))
A = np.zeros((n, n))
print("Digite os elementos da matriz A:")
for i in range(n):
    for j in range(n):
        A[i, j] = float(input(f"A[{i+1}, {j+1}]: "))

b = np.zeros(n)
print("Digite os elementos do vetor b:")
for i in range(n):
    b[i] = float(input(f"b[{i+1}]: "))

metodo = input("Escolha o método (Gauss-Seidel ou eliminação de gauss): ")

if metodo.lower() == "gauss-seidel":
    N = int(input("Digite o número máximo de iterações (N): "))
    epsilon = float(input("Digite o valor de Épsilon: "))

    x = gauss_seidel(A, b, N, epsilon)
    print("Solução aproximada:")
    print(x)
elif metodo.lower() == "eliminacao de gauss" or metodo.lower() == "eliminação de gauss":
    A_final, b_final = eliminacao_gauss(A, b)

    print("Após a eliminação de Gauss:")
    print("Matriz A:")
    print(A_final)
    print("Vetor b:")
    print(b_final)
else:
    print("Método não reconhecido. Por favor, escolha Gauss-Seidel ou Eliminação de Gauss.")

