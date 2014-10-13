#Mateusz Sacha
#13-10-2014
#iteration homework task 3d
word = input("Enter a word:")
number = int(input("Enter a number:"))
number_of_times_to_print = int(input("Enter the number of times you want your text to be printed:"))
for count in range(number_of_times_to_print):
    print("{0} {1}".format(word,number))
    
