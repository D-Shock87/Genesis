
# Programa que: Solicita números enteros hasta que el usuario escriba "Salir".
# Al escribir esto, el programa debe mostrar la sumatoria y  el promedio de los números introducidos.

# Programa fallido

sum = 0
num_count = 0
num_ip = int(input("Introduce un número ENTERO: "))
break_word = "Salir"
mean = None

if num_count > 0:
    mean = sum / num_count

while break_word == False:
    num_ip += sum
    num_count += 1

if break_word:
    print(f"En total, se introdujeron {num_count} números, que sumados equivalen a {sum} y su promedio es {mean}.")