#Prueba
count_prime = 0

for i in range(2,3001):
    prime_num = True
    for j in range(2, i): 
        if i % j == 0:
            prime_num = False
    if prime_num == True:
        count_prime += 1
        print(i)

print(count_prime)