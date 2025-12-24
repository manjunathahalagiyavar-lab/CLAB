11.Write a Python program for encoding and decoding using Base64. 









import base64 

text = "Hello Students" 

encoded = base64.b64encode(text.encode()) 

print("Encoded:", encoded.decode()) 

decoded = base64.b64decode(encoded).decode() 

print("Decoded:", decoded) 

Input text

Hello Students 
