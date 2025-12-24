6.Write a Python program that reads a file containing a list of usernames and passwords, one 

pair per line separated by a comma (,). It checks each password to see if it has been leaked in a 

data breach. You can use the “Have I Been Pwned” API (https://haveibeenpwned.com/API/v3) 

to check if a password has been leaked. 

  

import hashlib 

import requests 

def check_password(password): 

 hash = hashlib.sha1(password.encode()).hexdigest().upper() 

 first5 = hash[:5] 

 last = hash[5:] 

 url = "https://api.pwnedpasswords.com/range/" + first5 

res = requests.get(url) 

 for line in res.text.splitlines(): 

 part = line.split(":") 

 if part[0] == last: 

 return int(part[1]) 

 return 0 

pwd = input("Enter password: ") 

count = check_password(pwd) 

if count > 0: 

 print("This password was found", count, "times in data leaks!") 

else: 

 print("This password was NOT found in any leak.")
