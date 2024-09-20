#Prompt user for input and convert string to int for conditional operators
number = int(input("Please Enter in a whole number"))

#if number is less then 50 print Too Low
if number <50:
    print("Too Low")
#if number is 50 print correct
elif number == 50:
    print("corect")
#if number is more then 50 print Too High
elif number > 50:
    print("Too High")