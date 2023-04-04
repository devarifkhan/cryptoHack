key='73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
unhex_key=[k for k in bytes.fromhex(key)]
for c in range(256):
    flag="".join(chr(c^b) for b in unhex_key)
    if 'crypto' in flag:
        print(flag)