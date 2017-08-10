#Gediminas Lukosevicius
#October 3rd, 2016 ©

#The circle module has functions that perform calculations related to circles
import math

#the area functions accepts a circle's radius as an argument and returns the
#are of the circle
def area(radius):
    return math.pi * radius ** 2

#the circumference function accepts a circle's radius and returns the
#circle's circumference.
def circumference(radius):
    return 2 * math.pi * radius
