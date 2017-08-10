#Gediminas Lukosevicius
#November 20th, 2016 ©

#import random function
#create main function, start w/ empty list named nums
#loop to add 10 random integers in range (1-25)
#display numbers separated by single space
#sort the list
#display the sorted list
#create start list and print
#create finish list and print
#execute odd_even function
#build odd_even function
#start count at 0 for even and odd numbers
#engineer for loop to differentiate evens and odds to be totaled counter
#print number of even and odd counted in the sentence
#display the 6th element in the list
#close main

import random

def main():
    nums = []
    for n in range(10):
        nums.append(random.randint(1,25))
    for num in nums:
        print(num,end=' ')
    print()
    nums.sort()
    for num in nums:
        print(num,end=' ')
    print()
    start = nums[0:4]
    print(start)
    finish = nums[5:10]
    print(finish)
    execute = odd_even(nums)
    

def odd_even(nums):
    oddCount = 0
    evenCount = 0
    for n in nums:
        if n % 2 == 0:
            evenCount += 1
        else:
            oddCount += 1
    print('List had',evenCount,'evens','and',oddCount,'odds')
    print('The 6th element in the sorted nums is',nums[5])
    
    
main()
