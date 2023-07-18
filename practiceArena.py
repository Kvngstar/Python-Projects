print("Amarachukwu","Okoronkwo","is","my","name",sep="%",end="\n")
print("kingsley")

# to trigger exception raise Exception("message")
# assert 2+2==5,"2+2 is not equal to 5"
# del data[k: ]
a,*b = 'span',"man","milk"


print(b[0])
#docstring
def func():
    """This is a docstring"""
    pass
print(func.__doc__)
#Namespace


class Integer:
    def __init__(self,first,second):
        self.first = first
        self.second = second
        
    def Callback(self):
        print(f'My name is {self.first} {self.second}')
        
        
c1 = Integer("kingsley","okoronkwo")
c1.attr = "emma"
print(c1.attr)