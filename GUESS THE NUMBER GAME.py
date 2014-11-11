# Mateusz Sacha
# 10-11-2014
# guess the number game
import random
random_number = random.randint(1,100)
number = 0
number_of_guesses = 0
print(random_number)
while not number == random_number:
    number = int(input("Enter a number between 1 and 100:"))
    if number < 0:
        print("The number is out of range. Enter a number between 1 and 100:")
    elif number > 100:
        print("The number is out of range. Enter a number between 1 and 100:")
    elif random_number < number:
        print("Too high")
    elif number < random_number:
        print("Too low")
    number_of_guesses = number_of_guesses + 1
print("This is how many guesses you've had {0}.".format(number_of_guesses))
    
        
    
    

    

