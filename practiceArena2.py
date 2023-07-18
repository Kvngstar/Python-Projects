# import tkinter as tk

# window = tk.Tk()
# window.geometry("500x500")
# label = tk.Label(window,bg="red")
# image = open("dat.txt","r")
# print(image)
# image = tk.PhotoImage(file='image.jpg')
    
# label['image'] = image
# label.pack()

# def DisbleButton(*args):
#     print(measuringSystem.get(),*args,"args")
#     print(username.get())
# measuringSystem =tk.StringVar(value="imperial")
# button = tk.Checkbutton(window,width=40, variable=measuringSystem,text="this is a button",command=DisbleButton,onvalue="General",offvalue='imperial')
# button.pack()
# username = tk.StringVar()
# entry = tk.Entry(window, textvariable=username,show="*")
# entry.insert(0, 'your name')
# entry.delete(0,'end')   
# entry.pack()
# username.trace_add("write", DisbleButton)
# countryvar = tk.StringVar()

# window.mainloop()   
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Form")
content = Frame(root)
frame = Frame(content,background="orange", borderwidth=5, relief="ridge", width=300, height=100)
namelbl = ttk.Label(content, text="Name",background="red")
name = ttk.Entry(content,background="blue")
name1 = ttk.Entry(content)

onevar = BooleanVar(value=True)
twovar = BooleanVar(value=False)
threevar = BooleanVar(value=True)

one = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=True)
two = ttk.Checkbutton(content, text="Two", variable=twovar, onvalue=True)
three = ttk.Checkbutton(content, text="Three", variable=threevar, onvalue=True)
four = ttk.Checkbutton(content, text="four", variable=threevar, onvalue=True)
ok = ttk.Button(content, text="Okay")
cancel = ttk.Button(content, text="Cancel")



content.grid(column=0,row=0,sticky=(N,S,E,W))

frame.grid(column=0,row=0,rowspan=2,columnspan=3,   sticky=(N,S,E,W))
namelbl.grid(column=3,row=0, columnspan=2,sticky=(E,W,N,S))

name.grid(column=3,row=1, columnspan=2,sticky=(N,E,W,S))





one.grid(column=0,row=2)
two.grid(column=1,row=2)
three.grid(column=2,row=2)
ok.grid(column=3,row=2)
cancel.grid(column=4,row=2)


root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

content.grid_columnconfigure(0,weight=3)
content.grid_columnconfigure(1,weight=1)
content.grid_columnconfigure(2,weight=1)
content.grid_columnconfigure(3, weight=1)
content.grid_columnconfigure(4, weight=1)
# content.grid_rowconfigure(3, weight=1)


# content.grid(column=0, row=0)
# frame.grid(column=0, row=0, columnspan=3, rowspan=2)
# namelbl.grid(column=3, row=0, columnspan=2)
# name.grid(column=3, row=1, columnspan=2)
# one.grid(column=0, row=3)
# two.grid(column=1, row=3)
# three.grid(column=2, row=3)
# ok.grid(column=3, row=3)
# cancel.grid(column=4, row=3)

root.mainloop()