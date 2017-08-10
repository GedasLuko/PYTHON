#Gediminas Lukosevicius
#September 9th, 2016 ©

#This program will get the total cost of coffee when ordered by the pound

#Enter the number in pounds of coffee being ordered
pounds_coffee = int(input('How many pounds are you ordering? '))

#Calculate cost of coffee per pound
if pounds_coffee <=  9:
    coffee_cost = (pounds_coffee * 12.00)
if pounds_coffee >= 10:
    coffee_cost = (pounds_coffee * 10.00)
if pounds_coffee >= 20:
    coffee_cost = (pounds_coffee * 8.75)
if pounds_coffee >= 40:
    coffee_cost = (pounds_coffee * 7.50)
print('Cost of coffee: $', format(coffee_cost, ',.2f'), sep='')

#Calculate 7% sales tax from coffee cost
sales_tax = (coffee_cost * .07)
print('7% sales tax: $', format(sales_tax, ',.2f'), sep='')

#Calculate shipping fee
if coffee_cost <= 150.00:
    shipping_fee = (pounds_coffee * 1.00)
if coffee_cost > 150.00:
    shipping_fee = (pounds_coffee * 0.00)
print('Shipping fee: $', format(shipping_fee, ',.2f'), sep='')

#Determine total cost of order
total_cost = (coffee_cost + sales_tax + shipping_fee)
print('Total payable: $', format(total_cost, ',.2f'), sep='')
    
    
