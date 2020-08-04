import math
import os
import random
import re
import sys


def findPrimitiveRoot(p):
    s=p-1
    primeFactors = findPrimeFactors(s)

    isPrimitiveRoot = True
    smallestRoot = None
    for g in range(1,s):
        isPrimitiveRoot=True
        for factor in primeFactors:
            exp = int(s/factor)
            mod = powerModulus(g,exp,p)
            if mod == 1:
                isPrimitiveRoot = False
                break

        if isPrimitiveRoot:
            smallestRoot = g
            break
            
    rootCount=phi(s, primeFactors)
    
    print(str(smallestRoot) + " " + str(int(rootCount)))


def findPrimeFactors(n): 
    primeFactors = set()
    # Print the number of two's that divide n 
    while n % 2 == 0: 
        primeFactors.add(2) 
        n = n / 2
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2): 
          
        # while i divides n , print i ad divide n 
        while n % i== 0: 
            primeFactors.add(i), 
            n = n / i 
              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        primeFactors.add(n)
    return primeFactors

  
# A simple method to evaluate 
# Euler Totient Function
def phi(n, primeFactors): 
    result = n
    for f in primeFactors: 
        result = result  - result/f

    return result 

def powerModulus(x, y, p) : 
    res = 1     # Initialize result 
  
    # Update x if it is more 
    # than or equal to p 
    x = x % p  
      
    if (x == 0) : 
        return 0
  
    while (y > 0) : 
          
        # If y is odd, multiply 
        # x with result 
        if ((y & 1) == 1) : 
            res = (res * x) % p 
  
        # y must be even now 
        y = y >> 1      # y = y/2 
        x = (x * x) % p 
          
    return res

findPrimitiveRoot(644560789)
    # Write Your Code Here
