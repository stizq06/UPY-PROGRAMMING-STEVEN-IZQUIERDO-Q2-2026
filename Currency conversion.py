#Input
amount_MXN=float(input("Write the amoun in MXN Pounds:"))
e_r_USD=float(input("Write the current change in USD: "))
e_r_EUR=float(input("Write the current change in EUR: "))

#Process
USD = amount_MXN/e_r_USD  #this converts mxn to dollars
EUR =  amount_MXN/e_r_EUR   #this converts mxn to euros
#Output
print(f"The currency conversion from {amount_MXN:.2f} in USD is {USD:.2f} and in EUR {EUR:.2f}")
