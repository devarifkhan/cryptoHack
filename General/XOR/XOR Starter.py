from pwn import *
string="label"
result=''
for i in string:
    result+=chr(ord(i)^13)
print('crypto{{{}}}'.format(result))