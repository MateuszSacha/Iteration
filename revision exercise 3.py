total = 0
nofnumbers = int(input("How many number do you want to calculate the average from?:"))
for count in range (0,nofnumbers):
    total = total + int(input("Enter a number:"))
average = total / nofnumbers
print("The average is {0}".format(average))

    
