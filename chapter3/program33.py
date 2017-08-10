#Gediminas Lukosevicius
#September 11th, 2016 ©

#This program will calculate and display the total cost of shirts ordered

def main():

#Prompt user to enter quantity of shirts ordered
    shirts_order = int(input('Please enter the number of shirts ordering: '))

#Determine cost of shirts
    shirt_cost = 14.95
    if shirts_order <= 2:
        discount_charge = (shirt_cost * shirts_order)
    elif shirts_order <= 6:
        discount_charge = (shirt_cost * shirts_order) * .80
    elif shirts_order <= 11:
        discount_charge = (shirt_cost * shirts_order) * .70
    else:
        discount_charge = (shirt_cost * shirts_order) * .60

#Determine shipping charges
    shipping_charge = (shirts_order * 1.25)

#Compute total cost of order
    total_cost = (discount_charge + shipping_charge)

#Display outputs in currency format
    print('Cost of t-shirts: $', format(discount_charge, '.2f'), sep='')
    print('Shipping and handling: $', format(shipping_charge, '.2f'), sep='')
    print('Total cost of order: $', format(total_cost, '.2f'), sep='')

main()


    
     
    
    
