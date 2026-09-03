n = int(input("ingresa la cantidad de numeros: "))

a = 1
b = 1

fibonacci = []

for i in range(n):
    fibonacci.append(a)
    
    if a != 0:
        division = b / a
        print(f"Paso {i}: {b} / {a} = {division:.3f}")
    
    a, b = b, a + b

print("Serie de Fibonacci completa: ", fibonacci)