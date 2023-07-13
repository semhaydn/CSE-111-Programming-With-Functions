from tkinter import * 

root = Tk()

def myClick():
    myLabel = Label(root, text='Look! I clicked a button!')
    myLabel.pack()


myButton = Button(root, text='Click me', command=myClick, fg='violet' , bg='Black',)


myButton.pack( )

root.mainloop()
