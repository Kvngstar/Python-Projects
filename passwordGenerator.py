import string  
import random 
from math import  ceil
#password container
# random words generator
# Random number generator
# loop through the WPRDS AND number



# password = string.ascii_letters
# print(password)
# password2 = random.choice(string.ascii_letters) 
# print(password2)
# print("char", chr(random.randint(67,99)))

 
def PasswordGenerator(y):
    PasswordContainer = ""
    calculatedY = ceil(y/2)
    for x in range(calculatedY):
        
    
        if y%2 == 1 and x == calculatedY-1:
            PasswordContainer = PasswordContainer + string.ascii_letters[random.randint(1,26)]
            print("before break")
            break
        
        print("no break")
        PasswordContainer = PasswordContainer + string.ascii_letters[random.randint(1,26)]  + str(random.randint(0,9))
        
    print(PasswordContainer)
    
PasswordGenerator(100)