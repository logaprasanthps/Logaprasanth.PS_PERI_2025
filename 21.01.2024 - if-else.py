#Task
#Given an integer, n, perform the following conditional actions:
#If n is odd, print Weird
#If n is even and in the inclusive range of 2 to 5 , print Not Weird
#If n is even and in the inclusive range of 6 to 20 , print Weird
#If n is even and greater than 20, print Not Weird

#Input Format

#A single line containing a positive integer,n .

#Constraints
#1<=n<=100

#Output Format

#Print Weird if the number is weird. Otherwise, print Not Weird.

#Sample Input 0

#3
#Sample Output 0

#Weird
#Explanation 0

#n = 3
 #n is odd and odd numbers are weird, so print Weird.

#Sample Input 1

#24
#Sample Output 1

#Not Weird
#Explanation 1

#n = 24

 #n>20 and   n is even, so it is not weird.

#LOGIC1:

#!/bin/python3

import math
import os
import random
import re
import sys



if _name_ == '_main_':
    n = int(input().strip())

    if n%2 != 0:
        print("Weird")
    else:
        if n>=2 and n<=5:
            print("Not Weird")
        elif n>=6 and n<=20:
            print("Weird")
        else:
            print("Not Weird")


            #logic2:


 val = int(input())
output = "Weird"
if val%2 == 1:
    pass
elif 2 <= val < 5:
    output = "Not Weird"
elif 6 <= val <= 20:
    pass
else:
    output = "Not Weird"

print(output)
