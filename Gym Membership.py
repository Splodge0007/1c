#Welcome message, prompt for multiple input and set membership cost variable
#Some validation and equality operators on the student question
#Convert input to int on the age question

print("Welcome to the UWS Gym Membership Sign Up")
student = input("Are you a UWS Student? (y/n)").lower().strip() =='y'
age = int(input("Please enter your age"))
membership_cost = 0

#if the applicant is a student, they can enter for free
if student == True:
    membership_cost = 0
    print("You can attend for free!")
#if the applicant is not a student, and under 18, they must pay £24
elif age <18:
    membership_cost = 24
# if the applicant is not a student, and over 18, they must pay £44
elif age >18:
    membership_cost = 44
#final else block for any issues / out of bounds results
else:
    print("Something went wrong!")
print("The cost of your membership is £",membership_cost)