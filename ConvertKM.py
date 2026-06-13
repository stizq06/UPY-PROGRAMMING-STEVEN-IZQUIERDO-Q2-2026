# INPUT
weight_input = input('Enter weight in kg (or "exit" to stop): ')

# PROCESS
flag = False
total_cost = 0.0

while not flag:
    if weight_input.lower() == "exit":
        flag = True
    else:
        distance_input = input("Enter distance in km: ")
        
        weight = float(weight_input)
        distance = float(distance_input)
        
        if distance <= 100:
            if weight <= 5:
                cost = 50.00
            else:
                cost = 80.00
        else:
            if weight <= 5:
                cost = 120.00
            else:
                cost = 200.00
                
        total_cost = total_cost + cost
        print(f"Shipping cost: ${cost:.2f} MXN")
        
        # Ask again at the end of the loop
        weight_input = input('Enter weight in kg (or "exit" to stop): ')

# OUTPUT
print(f"Total: ${total_cost:.2f} MXN")