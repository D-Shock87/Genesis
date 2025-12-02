# Mini examen de matemáticas

print("Bienvenido. ¿Cuál es tu nombre?")
nombre = input()

print("Hola, " + nombre + ". Por favor, responde las siguientes preguntas:")

print("¿Cuánto es 7 x 5?")
x = 7
y = 5
respuesta_correcta_1 = x * y
# ¿Por qué se usa int antes del "input"?
# Porque input() devuelve una cadena de texto (string) y necesitamos convertirla a un número (int) para que la comparación funcione.
respuesta_usuario_1 = int(input())

if respuesta_usuario_1 == respuesta_correcta_1:
    print("¡Correcto!")
else:
    print("Incorrecto. La respuesta correcta es " + str(respuesta_correcta_1) + ". Siguiente pregunta.")
    # ¿Por qué usar str() aquí?
    # Porque al concatenar (unir) números con texto, es mejor convertir las variables para evitar errores de tipo.

print("¿Cuánto es 3 x 9?")
x = 3
y = 9
respuesta_correcta_2 = x * y
respuesta_usuario_2 = int(input())

if respuesta_usuario_2 == respuesta_correcta_2:
    print("¡Correcto! Muchas gracias por responder. Hasta pronto.")
else:
    print("Incorrecto. La respuesta correcta es " + str(respuesta_correcta_2) + ". Muchas gracias por responder. Hasta pronto.")