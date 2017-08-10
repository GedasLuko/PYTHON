#Gediminas Lukosevicius
#September 22nd, 2016 ©

#This program will determine the average of integers entered by a user
#initialize an accumulator
#intialize a counter
#create a while loop with a sentinel defined as 0
#create a break
#accumulate the total of integers entered by user
#increment counter for integers entered by user
#calculate average of integers entered by user
#display the average of integers entered by user to two decimal places

def main():

    total = 0.00
    counter = 0.00

    while True:

        num = int(input('Enter integer '))
        if num == 0:
            break
        total += num
        counter += 1
        avg = total / counter
           
    print('The average is', format(avg, '.2f'))

main()

    



            
            

