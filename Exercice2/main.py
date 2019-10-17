from tkinter import *
from math import *


class Calculator(Frame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()

        # create display
        self.scrollbar = Scrollbar(self, orient='horizontal')
        self.displaytext = StringVar(value="0")
        self.display = Entry(self, textvariable=self.displaytext, xscrollcommand=self.scrollbar.set, state="readonly")
        self.display.grid(row=0, column=0, columnspan=5, sticky="nesw")
        self.scrollbar.grid(row=1, columnspan=5, sticky="news")
        self.scrollbar.config(command=self.display.xview)

        # decor display
        self.display["foreground"] = "#000000"
        self.display["borderwidth"] = 0
        self.display["justify"] = "right"
        self.display.config(font=("Helvetica", 25))

        self.scientific_buttons = None
        self.historic = ["0"]

        self.create_menu()
        self.create_buttons()

    def create_menu(self):
        self.menubar = Menu(self.master)
        self.master.config(menu=self.menubar)

        self.menubar.add_command(label="Mode S", command=self.scientist_mode)

    def scientist_mode(self):
        # fifth column
        buttons = [self.create_button("cos", lambda event=None: self.add_historic("cos("), 2, 5, None),
                   self.create_button("sin", lambda event=None: self.add_historic("sin("), 3, 5, None),
                   self.create_button("tan", lambda event=None: self.add_historic("tan("), 4, 5, None),
                   self.create_button("pow", lambda event=None: self.add_historic("**"), 5, 5, None)]

        self.scientific_buttons = buttons

        self.display.grid(columnspan=6)
        self.scrollbar.grid(columnspan=6)
        self.menubar.delete("Mode S")
        self.menubar.add_command(label="Mode B", command=self.basic_mode)

    def basic_mode(self):
        for button in self.scientific_buttons:
            button.grid_remove()

        self.display.grid(columnspan=5)
        self.scrollbar.grid(columnspan=5)
        self.menubar.delete("Mode B")
        self.menubar.add_command(label="Mode S", command=self.scientist_mode)

    def create_buttons(self):
        # Create all buttons
        # first row
        self.create_button("7", lambda event=None: self.add_historic("7"), 2, 0, "<KP_7>")
        self.create_button("8", lambda event=None: self.add_historic("8"), 2, 1, "<KP_8>")
        self.create_button("9", lambda event=None: self.add_historic("9"), 2, 2, "<KP_9>")
        self.create_button("+", lambda event=None: self.add_historic("+"), 2, 3, "<KP_Add>")
        self.create_button("C", self.backspace, 2, 4, "<BackSpace>")

        # second row
        self.create_button("4", lambda event=None: self.add_historic("4"), 3, 0, "<KP_4>")
        self.create_button("5", lambda event=None: self.add_historic("5"), 3, 1, "<KP_5>")
        self.create_button("6", lambda event=None: self.add_historic("6"), 3, 2, "<KP_6>")
        self.create_button("-", lambda event=None: self.add_historic("-"), 3, 3, "<KP_Subtract>")
        self.create_button("AC", self.reset, 3, 4, "<Delete>")

        # third row
        self.create_button("1", lambda event=None: self.add_historic("1"), 4, 0, "<KP_1>")
        self.create_button("2", lambda event=None: self.add_historic("2"), 4, 1, "<KP_2>")
        self.create_button("3", lambda event=None: self.add_historic("3"), 4, 2, "<KP_3>")
        self.create_button("*", lambda event=None: self.add_historic("*"), 4, 3, "<KP_Multiply>")
        self.create_button("(", lambda event=None: self.add_historic("("), 4, 4, "(")

        # fourth row
        self.create_button("0", lambda event=None: self.add_historic("0"), 5, 0, "<KP_0>")
        self.create_button(".", lambda event=None: self.add_historic("."), 5, 1, "<KP_Decimal>")
        self.create_button("=", self.display_total, 5, 2, "<KP_Enter>")
        self.create_button("/", lambda event=None: self.add_historic("/"), 5, 3, "<KP_Divide>")
        self.create_button(")", lambda event=None: self.add_historic(")"), 5, 4, ")")

    def create_button(self, text, command, row, column, bind):
        # create button
        button = Button(self, text=text, command=command)
        button.grid(row=row, column=column)
        self.master.bind(bind, command)

        # decor button
        button["background"] = "#FFFFFF"
        button["borderwidth"] = 0
        button["width"] = 6
        button["height"] = 3
        button.config(font=("Helvetica", 15))

        return button

    def add_historic(self, value, event=None):
        if self.historic[-1] == "0" and value in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "(", "tan(", "sin(", "cos("]:
            self.historic.append(value)
        else:
            if self.historic[-1][-1] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ")"] and value in ["(", "tan(", "sin(", "cos("]:
                value = "*"+value
            if self.historic[-1][-1] == ")" and value in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "(", "tan(", "sin(", "cos("]:
                value = "*"+value
            if self.historic[-1] == "SYNTAX ERROR":
                self.historic.append(value)
            else:
                self.historic.append(self.historic[-1]+value)
        self.displaytext.set(self.historic[-1])

    def display_total(self, event=None):
        try:
            self.historic.append(str(round(eval(self.historic[-1]), 2)))
            self.displaytext.set(self.historic[-1])
        except TypeError:
            self.historic.append("SYNTAX ERROR")
            self.displaytext.set(self.historic[-1])
        except SyntaxError:
            self.historic.append("SYNTAX ERROR")
            self.displaytext.set(self.historic[-1])
        except ZeroDivisionError:
            self.historic.append("SYNTAX ERROR")
            self.displaytext.set(self.historic[-1])

    def reset(self, event=None):
        self.historic = ["0"]
        self.displaytext.set(self.historic[-1])

    def backspace(self, event=None):
        if len(self.historic) > 1:
            self.historic.pop()
        self.displaytext.set(self.historic[-1])


window = Tk()
window.title("Calculatrice")
window.resizable(width=False, height=False)

calc = Calculator(window)
calc.mainloop()
