#Input
weight=float(input("Write your weight in kg: ")) #Get weight from the user
height= float(input("Write your higth in m: ")) #Get heigth from the user

#Process
#BMI = weight/height^2 # Tambien es valido
BMI = weight/height **2

#Output
print(f"Hello, your BMI is: {BMI:.2f}") #Mostrar el indice de masa coporal



