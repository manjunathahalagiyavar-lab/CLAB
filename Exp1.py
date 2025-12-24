1.Write a Python program that defines a function and takes a password string as input and 

returns its SHA-256 hashed representation as a hexadecimal string. 

import hashlib 

def get_hash(pwd): 

 return hashlib.sha256(pwd.encode()).hexdigest() 

password = input("Enter password: ") 

print("SHA-256 Hash:", get_hash(password)) 

Output 

Enter password: hello123 

SHA-256 Hash: 872e4bdc3d3f6c9959c4f16fe813d52ab65f2f4d3f6d9bfb87ce0edce3f9a6c7
