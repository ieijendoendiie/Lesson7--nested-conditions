ask = input("Do u have a medical thing? (Y/N): ").upper()

if ask == "Y":
    print("Allowed")
else:
    atten = int(input("Enter your attendence: "))
    if atten >=75:
        print("Allowed")
    else:
        print("Not allowed")