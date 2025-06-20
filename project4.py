#age checker\
while True:
 name = input("Your name: ")
 current_year = int(input("Enter the current year: "))
 birth_year = int(input("Your birth year: "))
 if (current_year - birth_year < 18):
    print("Too young")
 elif(current_year - birth_year >= 18):
    print("You're legal")
 elif(current_year - birth_year >= 60):
    print("You're wise")
 choice = input("Do you want to continue? (yes/no): ")
 if choice.lower() in ["yes", "y"]:
    print("Continuing the program...")
 elif choice.lower() in ["no", "n"]:
    print ("Goodbye!")
    break
 else:
    print("Invalid input, please enter yes/no")
 

