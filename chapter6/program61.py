#Gediminas Lukosevicius
#October 18th, 2016 ©
#This program will enable the user to enter any number of course names
#and percent grades and write them to a file named grades.txt
#define main
#open grades.txt in write mode and assign to myfile
#prompt user to enter course and assign to course variable
#create while loop for user to enter percent
#close loop
#print 'File was created and closed'

def main():
    myfile = open('grades.txt', 'w')
    course = input('Enter course or Enter to quit ')

    while course != '':
        percent = int(input('Enter percent achieved '))
        myfile.write(course + '\n')
        myfile.write(str(percent) + '\n')
        course = input('Enter course or Enter to quit ')

    myfile.close()
    print('File was created and closed')

main()
                      
        
    
    
