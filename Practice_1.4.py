
#Práctica de formulario simple
nombre = input("Hola, ¿Cuál es tu nombre?: ")
edad = int(input("¿Y cuál es tu edad?: "))

edad_joven = edad - 10
edad_anciano = edad + 50

# Recordar: usar str() para convertir números a texto al concatenar.
print("¡Hola, " + nombre + "! Interesante saber que tienes " + str(edad) + " años. Eso significa que hace 10 años, tenías " + str(edad_joven) + " y que en 50 años, tendrás " + str(edad_anciano) + " años.")