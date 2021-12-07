def gcd(a,b):
 if(a==0):
    return b
 if (b==0):
        return a
 if(a==b):
    return a
 if(a>b):
    return gcd(a-b,b)
    return gcd(b-a,a)
a=60
b=12
c=gcd(a,b)
print(c)
                    
