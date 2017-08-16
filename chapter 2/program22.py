#Gediminas Lukosevicius
#August 31st, 2016 ©
#This program will convert weight in pounds to kilograms accurately to three decimal places
#Get the weight in pounds from user
#convert pounds to kilograms
#display kilograms to three decimal places for user
def main():
    weightPounds = int(input('Please enter weight in pounds: '))
    weightKilograms = weightPounds*0.45359237
    print('The weight in kilograms: ',format(weightKilograms, '.3f'),'kg')

main()
