#INput
hours_worked=float(input("Write your hours work here: "))#Get hours_worked from the user
hourly_rate =float(input("Write your hours rate here: "))#Get time hourly_rate from the user

#process
Ws= hours_worked*hourly_rate #this is how we get the weekly salary 

#output
print(f"This is your weekly salary: {Ws:.2f}" )