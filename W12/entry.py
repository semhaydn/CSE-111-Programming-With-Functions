from tkinter import * 

root = Tk()

backgroud_colour = 'Black'
text_colour = "White"

e = Entry(root,width= 50, fg=text_colour, bg=backgroud_colour,border=2 , borderwidth=4)
e.pack()
default_value = 'Enter Your Name: '
e.insert(0,default_value)

def myClick():

    hello = f'Hello {e.get()}'
    myLabel = Label(root, text=hello,bg=backgroud_colour,fg=text_colour)
    myLabel.pack()



confirm = 'Confirm'
myButton = Button(root, text=confirm, command=myClick, fg=text_colour , bg=backgroud_colour,)


myButton.pack( )

root.mainloop()