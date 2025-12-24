10.Write a Python program to implement asymmetric encryption using RSA Python library. 









import rsa 

public_key, private_key = rsa.newkeys(512) 

message = b"Hello Students" 

encrypted = rsa.encrypt(message, public_key) 

print("Encrypted message:", encrypted) 

decrypted = rsa.decrypt(encrypted, private_key) 

print("Decrypted message:", decrypted.decode()) 

