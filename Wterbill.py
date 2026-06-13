# INPUT
user_input = input('Enter m3 consumed (or "exit" to stop): ')

# PROCESS
flag = False
total_accumulated = 0.0

while not flag:
    if user_input.lower() == "exit":
        flag = True
    else:
        m3 = float(user_input)
        
        if m3 <= 10:
            charge = m3 * 8.00
        elif m3 <= 20:
            charge = m3 * 12.00
        else:
            charge = m3 * 18.00
            
        total_accumulated = total_accumulated + charge
        print(f"Month charge: ${charge:.2f} MXN")
        
        # Ask again at the end of the loop
        user_input = input('Enter m3 consumed (or "exit" to stop): ')

# OUTPUT
print(f"Total: ${total_accumulated:.2f} MXN")