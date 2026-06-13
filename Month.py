# INPUT
user_input = input('Enter month number (1-12) or type "exit": ')

# PROCESS
flag = False

while not flag:
    if user_input.lower() == "exit":
        flag = True
    else:
        month = int(user_input)
        
        if month == 12 or month == 1 or month == 2:
            print("Winter")
        elif month >= 3 and month <= 5:
            print("Spring")
        elif month >= 6 and month <= 8:
            print("Summer")
        elif month >= 9 and month <= 11:
            print("Fall")
        else:
            print("Invalid month. Please enter a number between 1 and 12.")
        
        # Ask again at the end of the loop
        user_input = input('Enter month number (1-12) or type "exit": ')

# OUTPUT
print("Program finished.")