number = int(input("Enter a number between 10 and 20 inclusive:"))
while number < 10 or number > 20:
    print("Your number is not in range of 10 to 20 inclusive")
    number = int(input("Enter a number between 10 and 20 inclusive:"))
