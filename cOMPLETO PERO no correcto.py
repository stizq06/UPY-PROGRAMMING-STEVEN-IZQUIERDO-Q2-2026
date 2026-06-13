# Input
password = input("Write your password: ")

# Process
flag = True  # This will help to exit the while loop
while flag:
    
    if len(password) < 8:
        print("Your password must be at least 8 characters long.")
        password = input("Write your password: ")
    elif not any(char.isupper() for char in password):
        print("Add at least one uppercase letter.")
        password = input("Write your password: ")
    #3
    elif not any(char.islower() for char in password):
        print("Add at least one lowercase letter.")
        password = input("Write your password: ")
    #4
    elif not any(char.isdigit() for char in password):
        print("Add at least one number.")
        password = input("Write your password: ")
    #5
    elif not any(char in "!@#$%^&" for char in password):
        print("Add at least one special character (!@#$%^&).")
        password = input("Write your password: ")
    #6
    else:
        #Sumas de digitos
        suma = 0
        for c in password:
            if c.isdigit():
                suma += int(c)
        if suma != 25:
            print("The digits in your password must add up to 25.")
            password = input("Write your password: ")
        #7
        else:
            longitud = len(password)
            # Función para saber si es primo
            def es_primo(n):
                if n < 2:
                    return False
                for i in range(2, int(n**0.5) + 1):
                    if n % i == 0:
                        return False
                return True
            if not es_primo(longitud):
                print("Your password length must be a prime number.")
                password = input("Write your password: ")
            #8
            else:
                import datetime
                mes_actual = datetime.datetime.now().strftime("%B").lower()
                if mes_actual not in password.lower():
                    print(f"Your password must include the current month in lowercase (e.g., {mes_actual}).")
                    password = input("Write your password: ")
                else:
                    flag = False

# Output
print("Your password is secure!")