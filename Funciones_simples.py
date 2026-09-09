a = int(input("Ingresa el valor de a: "))
b = int(input("Ingresa el valor de b: "))

if a != 0:
    x = -b / a
    print(f"La solución de {a}x + {b} = 0 es: x = {x}")
else:
    print("El valor de la a no puede ser 0.")