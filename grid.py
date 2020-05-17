from tkinter import *

root = Tk()

#creating label widget
#myLabel1 = Label(root, text="hello world!")
##myLabel2 = Label(root, text="my name is jake dawn!")
#myLabel3 = Label(root, text="dumas is the name!")
#shoving it on the screen
#myLabel.pack()
#myLabel1.grid(row=0, column=0)
#myLabel2.grid(row=1, column=0)
#myLabel3.grid(row=1, column=1)




e = Entry(root, width=50,borderwidth= 5)
e.pack()
e.insert(0,"enter your name")




def myClick():
    hello = " hello " + e.get()
    myLabel1 = Label(root, text=hello)
    myLabel1.pack()



myButton = Button(root, text="enter your name", command = myClick)
myButton.pack()

root.mainloop()
