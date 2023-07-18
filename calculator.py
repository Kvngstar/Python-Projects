# import random

# Calculator program

# Basic functions: add, subtract, multipy, divide
# Advanced functions: square, cube, power, mod
# Approach: Using  function


# ask user how much input they want to enter

number_of_inputs = int(input("How many numbers do you want to enter: "))

inputed_digits = []
i = 0
while i < number_of_inputs:
    values = int( input(f"number {i} is: "))
    inputed_digits.append(values)
    i = i + 1

print("You can only perform  add, subtract, multipy")


x= 0
answer = 0
def add():
    for x in inputed_digits:
        
        answer = answer + x
    return answer
def sub():

    for x in inputed_digits:
        answer = answer - x
    return answer
def mult():
   
    for x in inputed_digits:
        answer = answer * x
    return answer


function_to_perform = input("Choose a function to perform: ").lower()
if function_to_perform == "add":
  x =  add()
  print(x)

elif function_to_perform == "sub":
   x  = sub()
   print(x)
elif function_to_perform == "mult":
   x  = mult()
   print(x)
else:
    print("You're very funny")
# i= 1 
# while i <= 10:
#     x = random.randint(1,100)
#     print(x, end=" ")
#     i = i + 1