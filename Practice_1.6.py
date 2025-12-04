#Clasificador de números

#Uso de la función input para variables float.
#Uso del operador módulo (%) para determinar si un número es par o impar con base en su resultado.
result = float(input("Please enter any number: ")) % 2

#Uso de la estructura condicional if-else para indicar el número como par o impar.
if result == 1:
    print("Odd")
else:
    print("Even")