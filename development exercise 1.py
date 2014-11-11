# Mateusz Sacha
# 05-11-2014
# Iteration Development exercise 1
number = 0
largest = 0
while not number == -1:
    number = int(input("Enter a number:"))
    if number > largest:
        largest = number
    if number == -1:
        print("The largest number you've entered is {0}".format(largest))
    
    

