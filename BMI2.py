# INPUT
weight_input = input('Enter weight in kg (or type "exit"): ')

# PROCESS
flag = False

while not flag:
    if weight_input.lower() == "exit":
        flag = True
    else:
        height_input = input("Enter height in m: ")
        
        weight = float(weight_input)
        height = float(height_input)
        bmi = weight / (height * height)
        
        if bmi < 18.5:
            print(f"BMI: {bmi:.2f} — Underweight")
        elif bmi <= 24.9:
            print(f"BMI: {bmi:.2f} — Normal")
        elif bmi <= 29.9:
            print(f"BMI: {bmi:.2f} — Overweight")
        else:
            print(f"BMI: {bmi:.2f} — Obese")
            
        # Ask again at the end of the loop
        weight_input = input('Enter weight in kg (or type "exit"): ')

# OUTPUT
print("Program finished.")