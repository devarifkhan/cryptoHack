from Crypto.PublicKey import RSA
f=open('General/DATA FORMATS/privacy_enhanced_mail.pem','rb')
p=RSA.importKey(f.read())
print(p.d)