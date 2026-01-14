#Ejercicio de validación
#Uso de definición de funciones
#Uso de funciones con argumentos/parámetros
#Uso de argumentos con entrada del usuario

x = input("Please enter username: ")
y = input("Please enter password: ")

def validation(username, password):
    if username == "admin" and password == "qwerty":
        print(f"Welcome, {username}")
    elif username == "user" and password == "qweasd":
        print(f"Welcome, {username}")
    else:
        print("Wrong data, please try again.")

validation(x, y)