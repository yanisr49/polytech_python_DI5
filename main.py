from tkinter import *


class Calculator(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack(fill=BOTH)
        self.create_widgets()

        self.historic = ["0"]

    def create_widgets(self):

        self.display = Label(self, text="0", anchor=E)
        self.display["background"] = "#AAAAAA"
        self.display["justify"] = "right"
        self.display.grid(row=0, column=0, columnspan=5, sticky="nesw")

        # Create all buttons
        self.button_7 = Button(self, text="7", command= lambda: self.add_historic("7"))
        self.button_7.grid(row=1, column=0)
        self.button_8 = Button(self, text="8", command= lambda: self.add_historic("8"))
        self.button_8.grid(row=1, column=1)
        self.button_9 = Button(self, text="9", command= lambda: self.add_historic("9"))
        self.button_9.grid(row=1, column=2)
        self.button_plus = Button(self, text="+", command= lambda: self.add_historic("+"))
        self.button_plus.grid(row=1, column=3, sticky="nesw")
        self.button_C = Button(self, text="C", command=self.backward)
        self.button_C.grid(row=1, column=4, sticky="nesw")
        self.button_4 = Button(self, text="4", command= lambda: self.add_historic("4"))
        self.button_4.grid(row=2, column=0)
        self.button_5 = Button(self, text="5", command= lambda: self.add_historic("5"))
        self.button_5.grid(row=2, column=1)
        self.button_6 = Button(self, text="6", command= lambda: self.add_historic("6"))
        self.button_6.grid(row=2, column=2)
        self.button_minus = Button(self, text="-", command= lambda: self.add_historic("-"))
        self.button_minus.grid(row=2, column=3, sticky="nesw")
        self.button_AC = Button(self, text="AC", command=self.reset)
        self.button_AC.grid(row=2, column=4)
        self.button_1 = Button(self, text="1", command= lambda: self.add_historic("1"))
        self.button_1.grid(row=3, column=0)
        self.button_2 = Button(self, text="2", command= lambda: self.add_historic("2"))
        self.button_2.grid(row=3, column=1)
        self.button_3 = Button(self, text="3", command= lambda: self.add_historic("3"))
        self.button_3.grid(row=3, column=2)
        self.button_time = Button(self, text="*", command= lambda: self.add_historic("*"))
        self.button_time.grid(row=3, column=3, sticky="nesw")
        self.button_0 = Button(self, text="0", command= lambda: self.add_historic("0"))
        self.button_0.grid(row=4, column=0)
        self.button_dot = Button(self, text=".", command= lambda: self.add_historic("."))
        self.button_dot.grid(row=4, column=1, sticky="nesw")
        self.button_eq = Button(self, text="=", command=self.display_total)
        self.button_eq.grid(row=4, column=2)
        self.button_divide = Button(self, text="/", command= lambda: self.add_historic("/"))
        self.button_divide.grid(row=4, column=3, sticky="nesw")

    def add_historic(self, value):
        if self.historic[0] == "SYNTAX ERROR":
            self.reset()

        if self.display["text"] == "0" and value in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            self.display["text"] = value
            self.historic = [value]
        else:
            self.display["text"] += value
            self.historic.append(value)

    def display_total(self):
        try:
            self.display["text"] = str(round(eval(self.display["text"]), 2))
        except SyntaxError:
            self.display["text"] = "SYNTAX ERROR"
        self.historic = [self.display["text"]]

    def reset(self):
        self.display["text"] = "0"
        self.historic = ["0"]

    def backward(self):
        if len(self.historic) == 1:
            self.reset()
        else:
            self.historic = self.historic[:-1]
            self.display["text"] = ""
            for value in self.historic:
                self.display["text"] += value

window = Tk()
calc = Calculator(window)
calc.mainloop()
