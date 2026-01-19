#Suma-promedia-dor

lst1 = []
num = None

while True:
    n1 = input("Escribe un número o 'Salir': ")
    if n1.lower() == "salir":
        break
    try:
        num = int(n1)
    except ValueError:
        print("Entrada inválida. Intenta de nuevo")
        continue
    #En esta parte, el "continue" salta directamente a la siguiente
    #iteración del bucle, sin anexar nada a la lista abierta.

    lst1.append(num)
    #Esta pieza de código indica que, si el "try" fue exitoso,
    #el número debe anexarse a la lista abierta ("lst1").

#La siguiente estructura 'if / else' previene el hecho de que el programa no tenga entradas válidas.
if not lst1:
    print("No se han ingresado entradas válidas.")
else:
    y = sum(lst1)
    z = y / len(lst1)
    print(f"La suma total de tus números es {y} y su promedio es {z}. Lo lograste.")