#Prueba de pregunta tipo cuestionario

nombre = "joven padawan"
# La respuesta fue erróneamente introducida como un número entero (variable tipo int) para una función input (Leer nota de abajo)
respuesta_correcta = 237

# La función "input" SIEMPRE interpreta la entrada del usuario como una cadena de texto (variable tipo str)
# La función "input" fue convertida a entrada tipo int para una comparación correcta con la variable "respuesta_correcta"
respuesta_ingresada = int(input("¿Cuál es el resultado de 125+112?: "))

respuesta = (respuesta_ingresada == respuesta_correcta)

if respuesta:
    print("Excelente respuesta,", nombre)
else:
    print("Intenta otra vez,", nombre)