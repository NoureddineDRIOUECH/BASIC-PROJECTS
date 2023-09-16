import random
import string
chars = " " + string.ascii_letters + string.digits + string.punctuation
chars = list(chars)
key = chars.copy()
random.shuffle(key)
encryptedmessage = ""
textuser = input("Enter your text to encrypt : ")
for i in textuser:
    index = chars.index(i)
    encryptedmessage += key[index]
print(f"The encyption of your message is : {encryptedmessage}")
encryptedmessage = ""
textuser = input("Enter your text to decrypt : ")
for i in textuser:
    index = key.index(i)
    encryptedmessage += chars[index]
print(f"The encyption of your message is : {encryptedmessage}")
