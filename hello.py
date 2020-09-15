from datetime import datetime #Import statement for datetime

name = input("What is your name? ") #Input request of the users name
print("Hello", name) #Greeting of the user
# A message with with the number of letters in the name entered by the user
print("Your name has", len(name), "letters.")
#Method that returns the current month
now = datetime.today().month
#When input is not a number for the month entered then an error prints
while True:
        try:
                birthMonth = int(input("What month are you born in? ")) #Input request of the month the user was born in
                break
        except ValueError:
                print("Please enter a number")
#if current month is the input for birthday month then a happy birthday message prints
if now == birthMonth:
        print("Happy birthday month!")