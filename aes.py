'''
cipher text :
    '89NEvN56VtNjo1w5x3whmFUOZOqTaRyoMnIrPjCGKUv5n7kgGFHDmStzEgDFAU7QnZOK9MLeO/FW4etzIOhpKfOsw5xSD4Em72X1O2FRfaM='

utf-8 : 
'''
import base64
import sys
from Crypto.Cipher import AES

###function
#get key
keyChar = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
symbols = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# firstTwo = 'In'
def initKey(a,b,c,d):
    key = "2" + a + "?" + b + "mYD;@" + c + ";x" + d + "v\"i"
    return key
##decode AES
def decodeAES(key,cipherText):
    cipher = AES.new(key.encode("utf-8"),AES.MODE_ECB)
    plaintext = cipher.decrypt(cipherText)
    return plaintext

###cipher base64 to utf-8
cipher_base64 = '89NEvN56VtNjo1w5x3whmFUOZOqTaRyoMnIrPjCGKUv5n7kgGFHDmStzEgDFAU7QnZOK9MLeO/FW4etzIOhpKfOsw5xSD4Em72X1O2FRfaM='
cipher_byte = base64.b64decode(cipher_base64)
print(cipher_byte)
print("start")

###decode
for l in keyChar:
        for k in keyChar:
            for i in keyChar:
                for j in keyChar:
                    try:
                        check = True
                        key = initKey(i,j,k,l)
                        tmp_plain = decodeAES(key,cipher_byte)
                        result = tmp_plain.decode('utf-8')
                        print(f'key: {key}')
                        print(f"result : {result}")
                    except UnicodeDecodeError as e:
                        continue
                        
##print 
print("code finish")