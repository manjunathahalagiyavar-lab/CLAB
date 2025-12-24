3.Write a Python program to check if a password meets the following criteria: 

a. At least 8 characters long. 
b. Contains at least one uppercase letter, one lowercase letter, one digit, and one special character 
(e.g., @, #, $, %, or &). 
c. If the password meets the criteria, print a message that says "Valid Password." If it doesn’t 
meet the criteria, print a message that says "Password does not meet requirements."



password = input("Enter password: ") 

if len(password) < 8: 

 print("Password does not meet requirements.") 

else: 

 

 has_upper = any(c.isupper() for c in password) 

 has_lower = any(c.islower() for c in password) 

 has_digit = any(c.isdigit() for c in password) 

 has_special = any(c in "@#$%&" for c in password) 

 if has_upper and has_lower and has_digit and has_special: 

 print("Valid Password.") 

 else: 

 print("Password does not meet requirements.")
