#Gediminas Lukosevicius
#October 4th, 2016 ©

#This program will calculate the surface area and volume of a cube
#build main function
#Get side length of cube from user
#call function and catch all returned values
#display surface area and volume
#build cuber function with formulas and "return function"
#Call the main function


def main():
    a = float(input('Enter side length of cube '))
    SurfaceArea,Volume = cuber(a)
    print('Surface area is ',format(SurfaceArea,'.3f'))
    print('Volume is ',format(Volume,'.3f'))
   

def cuber(a):
    SurfaceArea = (6 * (a ** 2))
    Volume = (a ** 3)
    
    return SurfaceArea,Volume
main()


    






    

    
