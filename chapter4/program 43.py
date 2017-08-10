#Gediminas Lukosevicius
#September 21, 2016 ©

#This program will generate a triangle using a nested loop
#create input for user to enter an integer
#create the ranges for rows
#create a range for columns
#display 'o' as specified by the user

for i in range(6,0,-1):
    print(' ' * (6-i), end = '')
    for j in range(1,i+1):
        print('*', end = '')
    print()



