2.Write a Python program that defines a function to generate random passwords of a specified 

length. The function takes an optional parameter length, which is set to 8 by default. If no 

length is specified by the user, the password will have 8 characters. 





import random, string 

def make_password(length=8): 

 chars = string.ascii_letters + string.digits + "!@#$%&*" 

 return ''.join(random.choice(chars) for i in range(length)) 

n = input("Enter password length (press Enter for 8): ") 

if n == "": 

 print("Your password is:", make_password()) 

elif n.isdigit(): 

 print("Your password is:", make_password(int(n))) 

else: 

 print("Please enter only numbers for length!")
