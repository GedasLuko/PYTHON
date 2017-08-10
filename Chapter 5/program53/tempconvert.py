#Gediminas Lukosevicius
#October 8th, 2016 ©

#This program will convert temperature from celsius to fahrenheit
#and fahrenheit to celsius
#write formula for celsius to fahrenheit
#display converted celsius temperature in fahrenheit
#create function with formula for fahrenheit to celsius conversion
#return fahrenheit to celsius conversion temperature

def c_to_f(tmp):
    fahr = 9.0 / 5.0 * tmp + 32
    print('In Fahrenheit that is',format(fahr,'.2f'))

def f_to_c(tmp):
    return (tmp - 32) * 5 / 9
