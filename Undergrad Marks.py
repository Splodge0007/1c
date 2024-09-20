#Ask user for their mark
mark = int(input("What mark did you get?"))

#use of if/elif/else block to score the mark based on input and return to the user
if mark <30:
    print("You got an E")
elif mark in range (30, 39):
    print("You got a D")
elif mark in range(40, 49):
    print("You got a C")
elif mark in range(50, 59):
    print("You got a B2")
elif mark in range(60, 69):
    print("You got a B1")
elif mark in range(70, 79):
    print("You got a A3")
elif mark in range(80, 89):
    print("You got a A2")
elif mark in range(90, 100):
    print("You got a A1")
else:
    print("Score not recognised")