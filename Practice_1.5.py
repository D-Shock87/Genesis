#Práctica de calculadora básica

# Aun introduciendo números enteros, la función float() interpreta los números como decimales.
N1 = float(input("¡Bienvenido a la calculadora épica! Ingresa tu primer número: "))
N2 = float(input("Muy bien, ahora ingresa tu segundo número: "))
OP = input("¿Y qué operación de gustaría realizar? (Suma (+), Resta (-), Multiplicación (*), División (/)): ")

if OP == "+":
    RESULT = N1 + N2
    print("El resultado de la suma es: " + str(RESULT))
elif OP == "-":
    RESULT = N1 - N2
    print("El resultado de la resta es: " + str(RESULT))
elif OP == "*":
    RESULT = N1 * N2
    print("El resultado de la multiplicación es: " + str(RESULT))
elif OP == "/":
    if N2 != 0:
        RESULT = N1 / N2
        print("El resultado de la división es: " + str(RESULT))
    else:
        print("Error: No se puede dividir entre cero.")