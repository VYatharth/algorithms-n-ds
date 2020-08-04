#Using Fermat Little Theorem

def ncr(n, r, p): 
    ## initialize numerator 
   # # and denominator 
    num = den = 1 
    for i in range(r): 
        num = (num * (n - i)) % p 
        den = (den * (i + 1)) % p 
    return (num * pow(den,  
            p - 2, p)) % p 
  
# #p must be a prime 
## greater than n 
n, r, p = 0, 0, 0
print(ncr(n, r, p)) 
