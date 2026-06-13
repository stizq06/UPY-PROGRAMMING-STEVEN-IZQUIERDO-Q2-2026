#Input
Price= float(input("Write the product'price: ")) #get Price from the user
discount_rate=float(input("Write the discount here: ")) #get the discount from the user
#Process

discounted_rate = Price - (discount_rate*Price) #Get the discounted price 
total = discounted_rate * 1.16 # Get the total

#output
print(f"The final Price to pay is:  {total:.2f} ") #Display the final price