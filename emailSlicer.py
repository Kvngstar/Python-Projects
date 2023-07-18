holdEmail = input("Type an email")

index = holdEmail.find('@')
holdname = holdEmail[:index]
holdext =  holdEmail[index+1:]
suffix = holdext.find('.')
print(holdname)
print(holdext)
print(holdext[:suffix], "is the comapany")
print(holdext[suffix+1:],"is the domain")