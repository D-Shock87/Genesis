#Contador de números primos
#Primer uso del nested loop
#Uso de f-string

count_prime = 0
for i in range(2, 3001):
    prime = True
    for j in range(2, i):
        if i % j == 0 and j != 1 and j != i:
            prime = False
            break
    if prime == True:
        count_prime += 1
        print(f"{i} es un número primo")

print(f"En 3,000 números, existen {count_prime} que son primos.")