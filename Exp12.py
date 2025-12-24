12.Write a Python program to implement symmetric encryption using Python library. 






from cryptography.fernet import Fernet 

key = Fernet.generate_key() 

cipher = Fernet(key) 

message = b"Hello Students" 

encrypted = cipher.encrypt(message) 

print("Encrypted:", encrypted) 

decrypted = cipher.decrypt(encrypted) 

print("Decrypted:", decrypted.decode()) 

