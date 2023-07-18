import tkinter as tk
from tkinter import messagebox
window = tk.Tk()
window.title("second GU interface")
window.geometry("500x500")

# Scale

def getScale(select):
    # select=scl.get()
    print("number is: ",select)
    
    
scl=tk.IntVar()
myscale = tk.Scale(window, from_=0,to=100,variable=scl,command=getScale)
myscale.pack()


#scrollbar
scrollbar = tk.Scrollbar()
scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
txt = tk.Text(window,yscrollcommand= scrollbar.set)
txt.place(x=60)
scrollbar.config(command=txt.yview )


#Checker 

# def checker():
#     if fruit.get():
#         print("fruit was selected")
#     else:
#         print()
#     if price.get():
#         print("price is also checked")
#     else:
#         print()

# window.mainloop()

def ShowRadioButton():
    myRadioOption = radio.get()
    if myRadioOption==1:
        messagebox.showinfo("info","You are a Male")
    elif myRadioOption==2:
        messagebox.showinfo("info","You are a Female")
    else:
        messagebox.showerror("invalid gender")
        
radio = tk.IntVar()

rad1 = tk.Radiobutton(window,variable=radio,value=1,text="male")
rad2 = tk.Radiobutton(window,variable=radio,value=2,text="female")

btn2 = tk.Button(window,text="Check gender",command=ShowRadioButton)

# to place

rad1.place(x=10,y=400)
rad2.place(x=10,y=420)
btn2.place(x=10,y=440)
window.mainloop()