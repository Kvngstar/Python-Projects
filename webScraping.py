import os
import pickle
import json

#for Write operations
# f = open('data.txt','wb')
# f.write('Hello World \n')
# print(f.truncate(5))
# f.write('Welcome to mens world ')
# f.close()   

# for read operations
# defaultRead = open("data.txt","r")
# print(defaul tRead.readline())
# print(defaultRead.read())

# for append operations

# appendText = open("data.txt","a")
# appendText.writelines("Ebenezer")
# appendText.writelines("My help has come")

# Read = open("data.txt","r")
# print(Read.seek(3))
# print(Read.readline())
# print(Read.seek(3))
# print(Read.flush())
# print(Read.readlines())

# for checking directories 
# os.chdir("C:/Users/DELL/Desktop")
# print(os.listdir("C:/Users/DELL/Desktop"))
# print(os.getcwd())


# for serialization of Data we have marshal pickle json
# saving in pickle files


# for reading specified pickle object representation from a byte code
# favourite_cars = {"Mercedez benz":"Gl2","Toyota":"GLE","Ferarri":"me2"}
# favourite_carsList = [1,'Toyota',"Ferarri"]
# favourite_carsTuple = (1,[1,'a'],'Ferarri')
# pickled_object = pickle.dumps(favourite_cars)
# print(pickled_object)
# unPickle_Object = pickle.loads(pickled_object)
# print(unPickle_Object)
# for writing to a file, a specified pickle object representation in  byte code
# pickled_objectToFile = pickle.dump(favourite_cars,f)
# load_PickleObj = pickle.load(f)
# print(load_PickleObj)
# dumpedJson = json.dumps(favourite_carsTuple)
# print(dumpedJson )
# loadedJson = json.load(f)
# print(loadedJson)

#List COmprehension 

# so instead of using for in expression
M = [[1,2,3],[4,5,6],[7,8,9]]

col2 =  [row[1] for row in M]
print(col2)
# for in expression

empty_Array = []
for row in M:
   empty_Array.append(row[1])
print(empty_Array)
# lambda expression 
print(reduce(lambda row:row[1],M))
