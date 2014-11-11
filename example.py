number = int(input("Please enter a number: "))
high = max(number)
low = min(number)
while number == -1:
    number = int(input("Enter a number: "))
print ("The highest number entered was {0}".format(high))
print ("The lowest number entered was {0}".format(low))



