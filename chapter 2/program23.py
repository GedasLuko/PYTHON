#Gediminas Lukosevicius
#August 31st, 2016
#This program will calculate the commission a real estate salesperson will earn on the sale of a property
#Get selling price of property
#Get percent commission rate 
#Calculate the commission earned
#Display the commission earned with dollar sign, comma for thousands, two decimal places


selling_price = float(input('Please enter the selling price of the property: '))
commission_rate = float(input('Please enter the percent commission rate: '))
commission_earned = (commission_rate / 100) * selling_price
print('The amount of commission earned is: $', format(commission_earned,',.2f'), sep='')


