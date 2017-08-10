#Gediminas Lukosevicius
#October 31st, 2016 ©

#This program displays the records that are in the employees.txt file.

def main():
    #Open the employees.txt file.
    emp_file = open('employees.txt', 'r')

    #Read the first line from the file, which is
    #the name field of the first record.
    name = emp_file.readline()

    #If a field was read, continue processing.
    while name != '':
        #Read the ID number field.
        id_num = emp_file.readline()

        #Read the department field.
        dept = emp_file.readline()

        #Strip the newlines from the fields.
        name = name.rstrip('\n')
        id_num = id_num.rstrip('\n')
        dept = dept.rstrip('\n')

        #Display the record.
        print('Name:', name)
        print('ID: ', id_num)
        print('Dept:', dept)
        print()
        name = emp_file.readline()

    emp_file.close()


main()
    
