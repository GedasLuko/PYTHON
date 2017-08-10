#Gediminas Lukosevicius
#October 8th, 2016 ©

#import random function
#build numbers function first
#create accumulator
#create a count in range of five numbers
#specify five numbers greater than ten but less than thirty
#create a total for five numbers assignment
#display five random numbers and total as specified
#build main function and call numbers function
#call main function

import random

def main():
    numbers()

def numbers():

    total = 0.0
    
    for count in range(5):
        number = random.randint(11,29)
        total = total + number
        print(number, end = ' ')
    print()
    print('The total is', format(total, '.0f'))

main()
       
    
    


    

