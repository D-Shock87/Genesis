#Divisor de cuenta

bill = float(input("Por favor, ingrese el total de la cuenta: "))
tip = float(input("Por favor, ingrese el porcentaje de propina deseado: "))

total = bill + (bill * (tip / 100))
total_tip = bill * (tip / 100)

people = int(input("Por favor, ingrese el número de comensales: "))

total_pay = total / people

#El número en "total_tip" y "total_pay" está formateado con ": .2f" para solo mostrar dos decimales.
print(f"El total de propina es de: ${total_tip: .2f}. Cada persona debe pagar: ${total_pay: .2f}")