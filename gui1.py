import tkinter as tk



window =tk.Tk()
window.title("My first GUI")
top = tk.Toplevel( )
top.title("PYTHON UI")
# btn_Widget =tk.Button(window,activebackground="red",foreground="blue",width=25,height=5,text="Click here",) 
# btn_Widget.pack()
# Another wdget
# var1 = tk.IntVar()
# checkBtn_widget = tk.Checkbutton(window,text="CLICK HERE 2")
# checkBtn_widget.grid(row=1,sticky=tk.W)
# label= tk.Label(window,text="Name")
# e1 = tk.Entry(window,background="white",bd=2,highlightcolor="green")
# e1.grid(row=0,column=2)
# label.grid(row=0,column=1)


frame1 = tk.Frame(window,width=300,height=500,background="teal")
frame1.pack(side=tk.LEFT)
frame2 = tk.Frame(window,width=300,height=500,background="hotpink")
frame2.pack(side=tk.RIGHT)
label2 = tk.Label(frame1,text="Name",foreground="teal")
label2.place(x=0,y=10) 
entry2 = tk.Entry(frame1)
entry2.place(x=39,y=10)
listbox1 = tk.Listbox(frame1,width=20,height=10,background="teal",foreground="white")
listbox1.insert(1,"Football")
listbox1.insert(2,"Baseball")
listbox1.insert(3,"Volleyball")
listbox1.insert(4,"Hockey")
listbox1.place(x=0,y=50)
menubutton = tk.Menubutton(frame1,text="Menu",background="white")
menubutton = tk.Menubutton(frame1,text="Menu",background="white")
menubutton.menu = tk.Menu(menubutton)

menubutton['menu'] = menubutton.menu
menubutton.menu.add_checkbutton(label="Football")
menubutton.menu.add_checkbutton(label="Spanish club") 
menubutton.place(x=0,y=120)


menu = tk.Menu(window)
window.config(menu = menu)
filemenu = tk.Menu(menu)
menu.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="new file")
filemenu.add_command(label="existing file")
viewmenu = tk.Menu(menu)
menu.add_cascade(label="view", menu=viewmenu)
viewmenu.add_command(label="block view")


# menu = tk.Menu(window)
# window.config(menu=menu)
# filemenu = tk.Menu(menu)
# menu.add_cascade(label='File', menu=filemenu)
# filemenu.add_command(label='New')
# filemenu.add_command(label='Open...')
# filemenu.add_separator()
# filemenu.add_command(label='Exit', command=window.quit)
# helpmenu = tk.Menu(menu)
# menu.add_cascade(label='Help', menu=helpmenu)
# helpmenu.add_command(label='About')

# MESSAGE
message = tk.Message(frame1,text="world python day, to show how important \"python programming\" is to the world of programming",bg="skyblue")
message.config(width=120)
message.place(x=0,y=150)
v=tk.IntVar()
tk.Radiobutton(frame1,text="Male",variable=v,value=1).place(x=0,y=260)
tk.Radiobutton(frame1,text="Female",variable=v,value=2).place(x=0,y=300)

#Scale
scale1 = tk.Scale(frame1,from_= 0, to = 42) 
scale1.place(x=10,y=390)
scale2 = tk.Scale(frame1, from_ = 0, to=42, orient="horizontal")
scale2.place(x=10,y=340)


# Scrollbar

# scrollbar = tk.Scrollbar(frame1)
# scrollbar.pack(side=tk.BOTTOM,fill=tk.Y)
# mylist = tk.Listbox(frame1,yscrollcommand=scrollbar.set)
# for line in range(100):
#    mylist.insert(tk.END, 'This is line number' + str(line))
# mylist.pack( side = tk.LEFT, fill = tk.BOTH )
# scrollbar.config( command = mylist.yview )

scrollbar = tk.Scrollbar(frame2)
scrollbar.pack( side = tk.LEFT, fill = tk.Y )
mylist = tk.Listbox(frame2, yscrollcommand = scrollbar.set,width=200 )
for line in range(100):
   mylist.insert(tk.END, 'This is line number' + str(line))
mylist.pack( side = tk.LEFT, fill = tk.BOTH )
scrollbar.config( command = mylist.yview )


# SpinBox

spinbox = tk.Spinbox(frame1,background="pink",from_=0,to=100)
spinbox.pack(
    
)
m1 = tk.PanedWindow()
m1.pack(fill = tk.BOTH,expand=1)
left = tk.Entry(m1,bd=5)
m1.add(left)
m2 =tk.PanedWindow(m1,orient=tk.VERTICAL)
m1.add(m2)
top = tk.Scale(m2,orient=tk.HORIZONTAL)
m2.add(top)



window.mainloop()