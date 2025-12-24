8.Write a Python program for implementation of symmetric encryption using Caesar cipher 

algorithm. 







def encrypt(text, shift): 

 result = "" 

 for ch in text: 

 if ch.isalpha(): 

 base = 'A' if ch.isupper() else 'a' # check case (A-Z or a-z) 

 result += chr((ord(ch) - ord(base) + shift) % 26 + ord(base)) 

 else: 

 result += ch 

 return result 

def decrypt(text, shift): 

 return encrypt(text, -shift) 

message = "HELLO WORLD" 

shift = 3 

encrypted = encrypt(message, shift) 

print("Encrypted Text:", encrypted) 

decrypted = decrypt(encrypted, shift) 

print("Decrypted Text:", decrypted) 
