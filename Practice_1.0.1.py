#Tomador de decisiones

entertainment = None
at_home = input("¿Estás en casa?: ")

if at_home == "Sí" or at_home == "si" or at_home == "sí" or at_home == "Si":
    entertainment = "PS5"

else:
    internet = input("¿Tienes acceso a internet?: ")
    if internet == "Sí" or internet == "Si" or internet == "si" or internet == "sí":
        entertainment = "teléfono"
    else:
        entertainment = "Nintendo Switch"

print(f"Probablemente hoy te entretendrás con tu {entertainment}.")