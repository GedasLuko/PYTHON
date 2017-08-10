#Gediminas Lukosevicius
#October 19th, 2016 ©

#This program reads and displays the contents of philosophers.txt file

def main():
    #Open a file named philosophers.txt.
    infile = open('philosophers.txt', 'r')

    #Read the file's contents.
    file_contents = infile.read()

    #Close the file.
    infile.close()

    #Print the data that was read into
    #memory.
    print(file_contents)
main()
