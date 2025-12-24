4.Write a Python program that reads a file containing a list of passwords, one per line. It 

checks each password to see if it meets certain requirements (e.g., at least 8 characters, contains 

both uppercase and lowercase letters, and at least one number and one special character). 

Passwords that satisfy the requirements should be printed by the program. 



file = open("passwords.txt", "r") 

lines = file.readlines() 

file.close() 

for password in lines: 

 password = password.strip() 

 if len(password) < 8: 

 continue 

has_upper = any(c.isupper() for c in password) 

has_lower = any(c.islower() for c in password) 

has_digit = any(c.isdigit() for c in password) 

has_special = any(c in "@#$%&" for c in password) 

 if has_upper and has_lower and has_digit and has_special: 

 print("Valid Password:", password) 
