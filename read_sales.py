#Gediminas Lukosevicius
#October 24th, 2016 ©

#This program reads all of the values in sales.txt file.

def main():
    sales_file = open('sales.txt', 'r')

    line = sales_file.readline()

    while line != '':
        amount = float(line)

        print(format(amount, ',.2f'))

        line = sales_file.readline()
    sales_file.close()

main()
