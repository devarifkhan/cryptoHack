from pwn import *
k1= 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
k23= 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
k132 = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'

k1=bytes.fromhex(k1)
k23=bytes.fromhex(k23)
k132=bytes.fromhex(k132)

print(xor(k1,k23,k132))