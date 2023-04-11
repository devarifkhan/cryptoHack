def extendedGCD(a,b):
    if a==0:
        return b,0,1
    else:
        gcd,x,y=extendedGCD(b%a,a)
        return gcd,y-(b//a)*x,x
print(extendedGCD(26513,32321))