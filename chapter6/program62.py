#Gediminas Lukosevicius
#October 18th, 2016 ©
#This program will ouput all of the course names and scores entered by the user
#on file, one course per line
#define main
#open grades.txt and assign to myfile
#initialize total and counter
#assign line from file to a variable line
#print 'Here are your grades'
#create while loop with counter
#close file
#calculate average
#print average accurate to two decimal places

def main():
    myfile = open('grades.txt','r')
    total_percent = 0
    counter = 0
    line = myfile.readline()
    print('Here are your grades')

    while line != '':
        course = line.rstrip('\n')
        percent = int(myfile.readline())
        total_percent += percent
        print(course,'score is',percent)
        line = myfile.readline()
        counter += 1

    myfile.close()
    average_percent = total_percent / counter

    print('Average grade score is',format(average_percent,'.2f'))
main()
