# INPUT
user_input = input('Enter a grade (or type "done" to finish): ')

# PROCESS
flag = False
total_sum = 0.0
count = 0

while not flag:
    if user_input.lower() == "done":
        flag = True
    else:
        grade = float(user_input)
        total_sum = total_sum + grade
        count = count + 1
        
        # Ask again at the end of the loop
        user_input = input('Enter a grade (or type "done" to finish): ')

# OUTPUT
if count == 0:
    print("No grades entered. Please enter at least one grade.")
else:
    average = total_sum / count
    if average >= 7.0:
        print(f"Average: {average:.2f} — Passed")
    else:
        print(f"Average: {average:.2f} — Failed")