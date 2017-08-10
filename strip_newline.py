#Gediminas Lukosevicius
#October 24th, 2016 ©

#This program reads the contents of the philosophers.txt file one line at a time

def main():
    infile = open('philosophers.txt', 'r')

    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

    line1 = line1.rstrip('\n')
    line2 = line2.rstrip('\n')
    line3 = line3.rstrip('\n')

    infile.close()

    print(line1)
    print(line2)
    print(line3)

main()

