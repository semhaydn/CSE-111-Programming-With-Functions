from tkinter import *
import traceback

class Calculator:
    def __init__(self, master):
        self.master = master
        self.equation = ""
        self.text_input = StringVar()
        self.operator = ""
        Entry(master, font=('arial', 20, 'bold'), textvariable=self.text_input, bd=30, insertwidth=4, 
              width=14, justify='right').grid(columnspan=4)
        
        buttons = ["7", "8", "9", "/", "C",
                   "4", "5", "6", "*", "B",
                   "1", "2", "3", "-", "±",
                   "0", ".", "=", "+", ""]
        
        row_val = 1
        col_val = 0
        for button in buttons:
            Button(master, text=button, padx=22, pady=22, bd=8, fg="black",
                   font=('arial', 20, 'bold'), command=lambda button=button: self.button_click(button)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 4:
                col_val = 0
                row_val += 1

    def button_click(self, button):
        try:
            if button == "=":
                total = str(eval(self.operator))
                self.text_input.set(total)
                self.equation = ""
            elif button == "C":
                self.text_input.set("")
                self.equation = ""
                self.operator = ""
            elif button == "B":
                self.operator = self.operator[:-1]
                self.text_input.set(self.operator)
            elif button == "±":
                if self.operator:
                    if self.operator[0] == "-":
                        self.operator = self.operator[1:]
                    else:
                        self.operator = "-" + self.operator
                self.text_input.set(self.operator)
            else:
                self.operator = self.operator + str(button)
                self.text_input.set(self.operator)
        except Exception as e:
            self.text_input.set("error")
            self.operator = ""
            print("Error:", str(e))
            print(traceback.format_exc())

root = Tk()
Calculator(root)
root.mainloop()



