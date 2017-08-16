#Gediminas Lukosevicius
#September 1st, 2016 ©
#This program will convert an improper fraction to a mixed number
#Get Numerator
#Get Denominator
#Convert improper fraction to mixed number
#Dislpay the equivalent mixed number with no space either side of the / symbol

numerator = int(input('Please enter the numerator: '))
denominator = int(input('Please enter the denominator: '))
whole_number = int(numerator // denominator)
remainder_fraction = int(numerator % denominator)
print('The mixed number is: ', format(whole_number), ' and ', format(remainder_fraction), '/', format(denominator),sep='')


