#Gediminas Lukosevicius
#October 8th, 2016 ©

#This program will convert given temperature to either celsius or fahrenheit
#import tempconvert function
#build main function
#create input for user to enter degrees
#create a scale to specify entered number to either celsius or fahrenheit
#create assignment to convert the entered temperature
#display the converted temperature
#call main

import tempconvert

def main():
    temp = float(input('Enter a temperature '))
    scale = input('Was that input Celsius or Fahrenheit?\nEnter C or F ')
    if scale == "C":
        tempconvert.c_to_f(temp)
    else:
        cels = tempconvert.f_to_c(temp)
        print('In Celsius, that is',format(cels,'.2f'))
    

main()
    
