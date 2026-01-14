#FizzBuzz: Un clásico
while True:
#Utiliza un loop que solo se rompe por decisión del usuario
    user_input = (input("¡Bienvenido a FizzBuzz! Ingresa tu número o escribe Salir: "))

    try:
        num = int(user_input)
    except ValueError:
        print("¡Gracias por jugar!")
        break
#Si el usuario escribe "Salir",
#o realmente cualquier cosa que no sea un número,
#el programa termina.
    if num % 3 == 0 and num % 7 == 0:
        print("¡Eso es un FizzBuzz!")
    elif num % 3 == 0:
        print("¡Eso es un Fizz!")
    elif num % 7 == 0:
        print("¡Eso es un Buzz!")
    else:
        print(f"Ingresaste {num}. ¡Intenta de nuevo!")