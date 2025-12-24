9.Write a Python program for implementation of hacking Caesar cipher algorithm. 









def crack_caesar(text): 

 for key in range(26): 

 result = "" 

 for ch in text: 

 if ch.isalpha(): 

 if ch.isupper(): 

 result += chr((ord(ch) - 65 - key) % 26 + 65) 

 else:  

 result += chr((ord(ch) - 97 - key) % 26 + 97) 

 else: 

 result += ch 

 print("Shift", key, ":", result) 

cipher_text = "Khoor, Zruog!" 

crack_caesar(cipher_text) 
