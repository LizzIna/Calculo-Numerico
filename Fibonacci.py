n = int(input("Ingresa la cantidad de numeros: "))

a = 0
b = 1

fibonacci = []

for i in range(n):
    fibonacci.append(a)
    a, b = b, a + b

print("Serie de Fibonacci completa: ", fibonacci)