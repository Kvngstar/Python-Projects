import datetime
import os  
import tkinter as tk
from tkinter import messagebox
# class MyWorld:
#     def __init__(self,name,name2):
#         self.fname =name
#         self.lname =name2
        
        
# hei = MyWorld("kingsley","okoronkwo")
# print(hei.fname)

#APTECH FOR ELSE STATEMENT

# x=0
# while( x<5):
#     print(x)
#     x=x+1
# counter= 100
# while counter < 1:
#     print(counter)
#     counter = counter+ 1
# count= 9
# while count > -1:
#     print(count)
#     count = count - 1

# else: 
#     print("End of Loop")
    
#PASS STATEMENT
# for i in range(0,150,10):
#         pass
 # BREAK STATEMENT
# for i in range(0,20): 
#     if(i==5):
#          print(i) 
# CONTINUE STATEMENT 

# for i in range(0,20):
#     if(i==5 or i==10 or i==15):
#         continue
#     print(i)

# def Statement
# def BrewCoffee():
#     print("Making a coffee ...")
#     input("haba")
    
# BrewCoffee()






# ASSIGNMENT 1

# username = input("enter your Username: ")
# salary = float(input("your salary: "))
# yearOfService = int(input("How long have you worked?"))
# interest = 10
# bonus  = salary * (interest/10)
# currentSalary = salary+bonus

# if yearOfService>5:
#     print(f""" welcome {username}! Your bonus is: {bonus} and current salary is: {currentSalary}   """)
# else: 
#     print(f"""Dey Play, Your current salary is still: {salary}""")



    # array = [10,15,20,25,30]

    # for x in array:
         
# lists = [input("Enter an value"), input("enter second number")]
        #  print(max(lists))
# if lists[0] < lists[1]:
#             print(f"{lists[0]} is less than {lists[1]}")
# elif lists[0] == lists[1]:
#     print("numbers are the same")
    
# else:
#       print(f"{lists[0]} is greater than {lists[1]}")
       
       
# variable Declearation

# faith = "i believe in Faith"
# print(faith)
# oki,steven = "first","second"
# print(F"oki IS: {oki} and steven is: {steven}")

# chidimma,evans = ["hello","world"]  #LIST ASSIGNMENT / POSiTION ASSIGNMENT
# print(chidimma,evans)

#     # GENERALISED / SEQUENTIAL

# one,two,three = "60"
# print(one,two,three) # eXTENDED SEQUENC UNPACKING
# a,*b,c =["hello","mr","aptech","Ajah Branch"]
# print(b)
# cat=rat=horse="aniaml"      #Multiple sequence unpacking
# print(cat,rat)

# ayoAge = 19
# ayoAge = ayoAge + 1
# ayoAge=+1
# print(ayoAge)

# RELATIONAL OPERATOR and LOGICAL OPERATORS
# a= 10
# b= 20
# result = a>b #greater
# result = a == b #equal to
# result = a != b #not equal to
# result = a >= b #greater or equal
# result = a <= b #less or equal
# print(result)

# example for logical operator
# answer = a<b or a==b        
# print("answer: ", answer)coun
# counter = 12
# while counter >= 0:
#         print(counter)
#         counter = counter -1


# cars = ["honda","benz","bugatti","vovo"]

# for i in cars:
#     if i not in cars[1:]:
#        continue 
#     print(i)
    
# ASSIGNment 
    # TIMES TABLE

# inputNum = int(input("Input Number: "))   
# for i in range(0,13):
#     print( f"{inputNum} * {i} = {inputNum*i}")
  
# varible = int(input("Enter a number: "))  
  
#   DIAMOND SHAPE
# for i in range(0,varible):
#     for j in range(0,varible-i):
#         print(end="W")
#         print("a","c",end="X")
        
        
#     for j in range(0,i+1): 
#         print("*",end=" ")
#     print()
# reducer = varible-1    
# for i in range(0,varible):
#       for j in range(0,i+1):
#         print(end=" ")
#       for j in range(0,varible-i):
#         print("*",end=" ")
#       print()
# HOUSE WORK
# x = datetime.datetime.now()
# print(x.strftime("%A")  )

# class Animals: 

# text = open("test.txt","w")
# text.write("hello world, we are now two")
# text.close()

# text = open("test.txt","a")
# text.write("I am a new line")
# text.close()


# with open("text.txt","w") as testt:

#  testt.write("hello world, we are now two")

# light = open("test.txt","r")
# print(light.read())
# with open("test.txt","w") as text:
#     print(text.read())
# mycwd= os.getcwd()
# print(mycwd)
# mycwd34 = os.chdir('c:/Users/DELL/Desktop/python projects/')
# print(mycwd34)    check why my data is not fetching
# grtlastDir = os.listdir(mycwd34)
# for donald in grtlastDir:
#     print(donald)
# animals ="""tiger, 
# lion,
# hen,
# egle,fish,dog,cat"""
# with open('animap.txt',"w") as writeData:
#     writeData.write(animals)
    
# with open('animap.txt',"r") as readData:
#     print(next(readData))
#     print(readData.readline( )+" this is readline   1")
#     print(next(readData))
#     print(next(readData))
    

# SEEK METHOD

# with open('animap.txt',"r") as seeker:
#     seeker.seek(2)
#     seeker.tell() #Wastches positions
    
#     print("start point "+ seeker.read())
    
# with open('animap.txt','r') as adds:
#     with open('animap.text','a') as add:
#         add.write(" some thing new!")
#         add.writelines("\n some \n thing \n  new!")
    
    
import pickle
# python object works with dump method
# data = ['2','4','6','8','10']
# myset = {'henry','jacob','james'}
# string='hello my people'
# tuple= ((1,2,3,4,5))

# python files works with the dump (without the 's') method
# print(pickle.loads(data))
# dump method: convert python objects to string object

# result = pickle.dumps(myset)
# print("pickle dumps:",result)
# print("double dump:", pickle.dumps(result))
# loads converts string back to a python object
# newdata = pickle.loads(result)
# print("pickle loads:",newdata)    
# list comprehension
# expression, item, iterables, condition state.(this is an option)
# lists = ['help','cry','sad','run']
# for i in lists:
#     if "r" in i:
#         print(i)
        
# output = [b for b in lists if type(b)== string]
# print(output)

# matrix = [[1,2,3],
#           [4,5,6],
#           [7,8,9]
#           ]
# getmatrix = [row[2] for row in matrix]
# print(getmatrix) 

root= tk.Tk()                                                                
root.title('my gui')
canvass = tk.Canvas(root,width=  800,height=500,background="teal")
# canvass.pack()

# label widget

alltext = tk.Label(root,text='I am kingsley okoronkwo',padx=20,pady=10)
# alltext.pack()
def displayData():
    print("hello")
    data = "Able God"
    alltext= tk.Label(root,text=data.upper(),pady=20,padx=300)
    alltext.pack()
button = tk.Button(root,text="click here",bg="red",fg="pink",command=displayData)
# button.pack()

msg = tk.Message(root,text="I am message",bg="orange")
# msg.pack()
frame1 = tk.Frame(root,width=50,height=25,bg="purple")
frame2 = tk.Frame(root,width=50,height=25,bg="gold")
frame1.grid(row=0,column=0)
frame2.grid(row=0,column=1)
    
    
    
    
root.mainloop() 