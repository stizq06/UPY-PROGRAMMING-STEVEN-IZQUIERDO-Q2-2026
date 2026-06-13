age= int(input("What is your age: "))
has_id = bool(input("Have ID? "))

if age > 65:
    discount=0.4
elif age < 65 and age >= 26:
    discount =0
elif age < 26 and age >= 12
    has_id = bool(input("Have ID? "))
        discount=0
    if has_id==True:
    else:
        discount= 0.2
else:
    discount=0.3

ticket = 150 * (1 - discount)
print(f"Total is ${ticket:.2f} MXN")