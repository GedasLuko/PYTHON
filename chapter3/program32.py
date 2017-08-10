#Gediminas Lukosevicius
#September 10th, 2016 ©

#This program will display two questions about our solar system
#Prompt the user to enter the answers
#Display the answers as either correct or incorrect

#Display the first question
def main():
    first_question = input('What is the farthest planet in our solar system? Enter name here: ')
    
#Detect if answer to first question is correct or incorrect
    if first_question == 'pluto' or first_question == 'Pluto':
        print('You are correct!')
    else:
        print('Sorry that is incorrect, please try again.')
        
#Display the second question
    second_question = int(input('How many planets are in our solar system? Enter number here: '))

#Detect if answer to second question is correct or incorrect
    if second_question == 9:
        print('You are correct! Good job.')
    else:
        print('Sorry that is incorrect, please try again.')

main()
