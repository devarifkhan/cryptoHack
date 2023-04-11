# def gcd(m,n): #Euclid's Algorithm
#     if m<n:
#         m,n=n,m
#     while m%n!=0:
#         m,n=n,m%n
#     return n
# print(gcd(12,8))

a=66528
b=52920

def gcd(m,n): #Euclid's Algorithm
    if m<n:
        m,n=n,m
    while m%n!=0:
        m,n=n,m%n
    return n
print(gcd(a,b))