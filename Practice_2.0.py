#FizzBuzz: Un clásico
while True:
    user_input = (input("¡Bienvenido a FizzBuzz! Ingresa tu número o escribe Salir: "))

    try:
        num = int(user_input)
    except ValueError:
        print("¡Gracias por jugar!")
        break
    if num % 3 == 0 and num % 7 == 0:
        print("¡Eso es un FizzBuzz!")
    elif num % 3 == 0:
        print("¡Eso es un Fizz!")
    elif num % 7 == 0:
        print("¡Eso es un Buzz!")
    else:
        print(f"Ingresaste {num}, ¡Intenta de nuevo!")