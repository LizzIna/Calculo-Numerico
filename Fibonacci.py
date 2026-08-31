n = int(input("ingresa la cantidad de numeros: "))

a = 0
b = 1

fibonacci = []

for i in range(n):
    fibonacci.append(a)
    
    if a != 0:
        division = b / a
        print(f"Paso {i}: {b} / {a} = {division}")
    
    a, b = b, a + b

print("\nSerie de Fibonacci completa:")
print(fibonacci)