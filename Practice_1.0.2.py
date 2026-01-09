#Prueba
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