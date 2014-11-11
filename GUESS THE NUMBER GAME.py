# Mateusz Sacha
# 10-11-2014
# guess the number game
import random
random_number = random.randint(1,100)
number = 0
count = 0
number_of_guesses = 0
print(random_number)
while not number == random_number:
    number_of_guesses = number_of_guesses + count
    number = int(input("Enter a number between 1 and 100:"))
    if number < 0:
        print("the number is out of range. Enter a number between 1 and 100:")
    elif number > 100:
        print("the number is out of range. Enter a number between 1 and 100:")
    elif random_number < number:
        print("too high")
    elif number < random_number:
        print("too low")
print(number_of_guesses)
    
        
    
    

    

