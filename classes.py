classesTaken = input("Please enter the nanumber of all the ITEC classes you are taking this semester seperated by a space: ")
print("\n")
print("You are taking the following ITEC courses")
for classes in classesTaken.split():
    print(f"ITEC{classes}")