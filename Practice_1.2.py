# Prueba de booleans, signo de comparación (==) y estructuras de control (if-else)

usuario = "D-Shock"
clave_correcta = "5429"

#Primer uso de "input"
clave_ingresada = input("Ingrese su clave: ")

acceso = (clave_ingresada == clave_correcta)

# Era "if acceso == True:", pero se corrigió a "if acceso:" para simplificar
if acceso:
    print("Acceso concedido. Bienvenido,", usuario)
else:
    print("Acceso denegado. Clave incorrecta. Smithers, libere a los perros.")