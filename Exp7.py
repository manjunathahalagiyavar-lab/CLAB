7.Write a Python program that simulates a brute-force attack on a password by trying out all 
possible character combinations. 








import itertools 

def brute_force(secret, charset="abc123", max_len=3): 

 for length in range(1, max_len + 1): 

 for combo in itertools.product(charset, repeat=length): 

 guess = "".join(combo) 

 if guess == secret: 

 print("Found password:", guess) 

 return 

 print("Password not found") 

if __name__ == "__main__": 

 secret = "b2" 

 brute_force(secret) 
