'''Write a program using a while loop to print all the odd numbers within a given range.'''

lower_limit = int(input("Enter the lower limit : "))
upper_limit = int(input("Enter the upper limit : "))

while(lower_limit < upper_limit + 1):
    if(lower_limit % 2 != 0):
        print(lower_limit)
    lower_limit += 1
