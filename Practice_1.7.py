# Calculadora de IMC (Índice de Masa Corporal)

weight = float(input("¿Cuál es tu peso en kilogramos? "))
height = float(input("¿Cuál es tu altura en metros? "))

bmi = weight / (height ** 2)

if bmi < 18.49:
    category = "Bajo peso"
elif 18.5 <= bmi <= 24.99:
    category = "Peso normal"
elif 25 <= bmi <= 29.99:
    category = "Sobrepeso"
elif 30 <= bmi <= 34.99:
    category = "Obesidad grado I"
elif 35 <= bmi <= 39.99:
    category = "Obesidad grado II"
else:
    category = "Obesidad grado III"

print(f"Tu IMC es: {bmi:.2f}. Categoría: {category}.")