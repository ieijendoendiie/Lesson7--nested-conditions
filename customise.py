print("Choose vehicle: ")
print("1. car")
print("2. bike")
choice = int(input("Enter your choice: "))

if choice == 1:
    print("Choose a type of bike: ")
    print("1. Normal")
    print("2. advanced")
choice2 = int(input("Enter your choice: "))
if choice == 2:
    print("Choose a type of car: ")
    print("1. Normal")
    print("2. advanced")
choice3 = int(input("Enter your choice: "))
if choice2 == 1 or choice3 == 1:
    print("Its normal")
elif choice2 == 2 or choice3 == 2:
    print("Its advanced")
else:
    print("Error")

