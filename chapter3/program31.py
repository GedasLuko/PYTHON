#Gediminas Lukosevicius
#September 10th, 2016 ©

#This program will identify an integer entered by the user as EVEN or ODD

def main ():
#Promp user to enter an integer
    integer_num = int(input('Please enter an integer: '))
#Calculate if number has remainder when divided by 2; if no remainder = EVEN, else = ODD
    if integer_num % 2 == 0:
        print('The integer entered is: EVEN ')
    else:
        print('The integer entered is: ODD ')

main()
    
