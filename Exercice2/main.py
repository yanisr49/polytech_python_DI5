from tkinter import *


class Calculator(Frame):

    def __init__(self, master):
        super().__init__(master)
        self.pack(fill=BOTH)

        self.display = Label(self, text="0", anchor=E)
        self.display["background"] = "#AAAAAA"
        self.display["justify"] = "right"
        self.display.grid(row=0, column=0, columnspan=5, sticky="nesw")

        self.create_buttons()

        self.historic = ["0"]

    def create_menu(self):


    def create_buttons(self):

        # Create all buttons
        # first row
        button_7 = Button(self, text="7", command=lambda: self.add_historic("7"))
        button_7.grid(row=1, column=0, sticky="nesw")
        self.master.bind("<KP_7>", lambda event: self.add_historic("7"))
        button_8 = Button(self, text="8", command=lambda: self.add_historic("8"))
        button_8.grid(row=1, column=1, sticky="nesw")
        self.master.bind("<KP_8>", lambda event: self.add_historic("8"))
        button_9 = Button(self, text="9", command=lambda: self.add_historic("9"))
        button_9.grid(row=1, column=2, sticky="nesw")
        self.master.bind("<KP_9>", lambda event: self.add_historic("9"))
        button_plus = Button(self, text="+", command=lambda: self.add_historic("+"))
        button_plus.grid(row=1, column=3, sticky="nesw")
        self.master.bind("<KP_Add>", lambda event: self.add_historic("+"))
        button_clear = Button(self, text="C", command=self.backspace)
        button_clear.grid(row=1, column=4, sticky="nesw")
        self.master.bind("<BackSpace>", self.backspace)

        # second row
        button_4 = Button(self, text="4", command=lambda: self.add_historic("4"))
        button_4.grid(row=2, column=0, sticky="nesw")
        self.master.bind("<KP_4>", lambda event: self.add_historic("4"))
        button_5 = Button(self, text="5", command=lambda: self.add_historic("5"))
        button_5.grid(row=2, column=1, sticky="nesw")
        self.master.bind("<KP_5>", lambda event: self.add_historic("5"))
        button_6 = Button(self, text="6", command=lambda: self.add_historic("6"))
        button_6.grid(row=2, column=2, sticky="nesw")
        self.master.bind("<KP_6>", lambda event: self.add_historic("6"))
        button_minus = Button(self, text="-", command=lambda: self.add_historic("-"))
        button_minus.grid(row=2, column=3, sticky="nesw")
        self.master.bind("<KP_Subtract>", lambda event: self.add_historic("-"))
        button_allclear = Button(self, text="AC", command=self.reset)
        button_allclear.grid(row=2, column=4, sticky="nesw")
        self.master.bind("<Delete>", self.reset)

        # third row
        button_1 = Button(self, text="1", command=lambda: self.add_historic("1"))
        button_1.grid(row=3, column=0, sticky="nesw")
        self.master.bind("<KP_1>", lambda event: self.add_historic("1"))
        button_2 = Button(self, text="2", command=lambda: self.add_historic("2"))
        button_2.grid(row=3, column=1, sticky="nesw")
        self.master.bind("<KP_2>", lambda event: self.add_historic("2"))
        button_3 = Button(self, text="3", command=lambda: self.add_historic("3"))
        button_3.grid(row=3, column=2, sticky="nesw")
        self.master.bind("<KP_3>", lambda event: self.add_historic("3"))
        button_time = Button(self, text="*", command=lambda: self.add_historic("*"))
        button_time.grid(row=3, column=3, sticky="nesw")
        self.master.bind("<KP_Multiply>", lambda event: self.add_historic("*"))
        button_lpar = Button(self, text="(", command=lambda: self.add_historic("("))
        button_lpar.grid(row=3, column=4, sticky="nesw")
        self.master.bind("(", lambda event: self.add_historic("("))

        # forth row
        button_0 = Button(self, text="0", command=lambda: self.add_historic("0"))
        button_0.grid(row=4, column=0, sticky="nesw")
        self.master.bind("<KP_0>", lambda event: self.add_historic("0"))
        button_dot = Button(self, text=".", command=lambda: self.add_historic("."))
        button_dot.grid(row=4, column=1, sticky="nesw")
        self.master.bind("<KP_Decimal>", lambda event: self.add_historic("."))
        button_eq = Button(self, text="=", command=self.display_total)
        button_eq.grid(row=4, column=2, sticky="nesw")
        self.master.bind("<KP_Enter>", self.display_total)
        self.master.bind("<Return>", self.display_total)
        button_divide = Button(self, text="/", command=lambda: self.add_historic("/"))
        button_divide.grid(row=4, column=3, sticky="nesw")
        self.master.bind("<KP_Divide>", lambda event: self.add_historic("/"))
        button_rpar = Button(self, text=")", command=lambda: self.add_historic(")"))
        button_rpar.grid(row=4, column=4, sticky="nesw")
        self.master.bind(")", lambda event: self.add_historic(")"))

    def add_historic(self, value):
        if self.historic[0] == "SYNTAX ERROR":
            self.reset()

        if self.display["text"] == "0" and value in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "(", ")"]:
            self.display["text"] = value
            self.historic = [value]
        else:
            if self.display["text"][-1] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ")"] and value == "(":
                self.add_historic("*")
            if value in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "("] and self.display["text"][-1] == ")":
                self.add_historic("*")
            self.display["text"] += value
            self.historic.append(value)

    def display_total(self, event=None):
        try:
            self.display["text"] = str(round(eval(self.display["text"]), 2))
        except TypeError:
            self.display["text"] = "SYNTAX ERROR"
        except SyntaxError:
            self.display["text"] = "SYNTAX ERROR"
        self.historic = [self.display["text"]]

    def reset(self, event=None):
        self.display["text"] = "0"
        self.historic = ["0"]

    def backspace(self, event=None):
        if len(self.display["text"]) == 1:
            self.reset()
        else:
            self.display["text"] = self.display["text"][:-1]
            if len(self.historic[-1]) == 1:
                self.historic = self.historic[:-1]
            else:
                self.historic[-1] = self.historic[-1][:-1]


window = Tk()
window.title("Calculatrice")
calc = Calculator(window)
calc.mainloop()
