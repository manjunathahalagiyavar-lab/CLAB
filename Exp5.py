5.Write a Python program that creates a password strength meter. The program should prompt 

the user to enter a password and check its strength based on criteria such as length, complexity, 

and randomness. Afterwards, the program should provide suggestions for improving the 

password strength. 



pwd = input("Enter password: ") 

score = 0 

if len(pwd) >= 8: 

 score += 1 

if any(c.isupper() for c in pwd): 

 score += 1 

if any(c.islower() for c in pwd): 

 score += 1 

if any(c.isdigit() for c in pwd): 

 score += 1 

if any(c in "@#$%&*?!" for c in pwd): 

 score += 1 

if len(pwd) > 0 and (len(set(pwd)) / len(pwd)) > 0.5: 

 score += 1 

if score <= 2: 

 print("Password strength: WEAK") 

elif score <= 4: 

 print("Password strength: MEDIUM") 

else: 

 print("Password strength: STRONG") 

print("Suggestions:") 

if len(pwd) < 12: 

 print("- Use 12 or more characters") 

if not any(c.isupper() for c in pwd): 

 print("- Add at least one UPPERCASE letter") 

if not any(c.islower() for c in pwd): 

 print("- Add at least one lowercase letter") 

if not any(c.isdigit() for c in pwd): 

 print("- Add at least one digit (0-9)") 

if not any(c in "@#$%&*?!" for c in pwd): 

 print("- Add at least one special character (@ # $ % & * ? !)") 

if len(pwd) > 0 and (len(set(pwd)) / len(pwd)) <= 0.5: 

 print("- Avoid repeating same characters (make it more random)")
