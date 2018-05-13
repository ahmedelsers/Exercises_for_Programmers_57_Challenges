#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox as mb

class SimpleMath(tk.Tk):
    def __init__(self):
        super().__init__()

        self.num1_label = tk.Label(self, text="First Number:")
        self.num1_label.grid(row=0, column=0)


        self.num1_var = tk.StringVar()
        self.num1 = tk.Entry(self, textvariable=self.num1_var)
        self.num1.grid(row=0, column=1)

        self.num2_label = tk.Label(self, text="Second Number:")
        self.num2_label.grid(row=1, column=0)

        self.num2_var = tk.StringVar()
        self.num2 = tk.Entry(self, textvariable=self.num2_var)
        self.num2.grid(row=1, column=1)

        self.CalcOut_label_var = tk.StringVar()
        self.CalcOut_label = tk.Label(self, textvariable=self.CalcOut_label_var)
        self.CalcOut_label.grid(row=2, rowspan=4, sticky='WE')

        self.calculations = {'sum': lambda num1, num2: num1+num2,
                             'diff': lambda num1, num2: num1-num2,
                             'product': lambda num1, num2: num1*num2,
                             'div': lambda num1, num2: num1//num2}

        self.num1_var.trace_add('write', self.calc_printout)
        self.num2_var.trace_add('write', self.calc_printout)

    def calc_printout(self, event=None, *args):
        if (self.num1.get() and self.num2.get() != ''):
            try:
                self.int_num1 = int(self.num1.get())
                self.int_num2 = int(self.num2.get())
                self.var = "Sum: {}\n Difference: {}\n Product: {}\n Quotient: {}".format(self.calculations['sum'](self.int_num1, self.int_num2),
                                                                                          self.calculations['diff'](self.int_num1, self.int_num2),
                                                                                          self.calculations['product'](self.int_num1, self.int_num2),
                                                                                          self.calculations['div'](self.int_num1, self.int_num2))
                self.CalcOut_label_var.set(self.var)
            except ValueError:
                mb.showwarning("Error", "Please enter numbers only!")
            except ZeroDivisionError:
                mb.showwarning("Error", "Please do not use 0 in the Second Number")



if __name__ == "__main__":
    app = SimpleMath()
    app.title("Simple Math")
    app.resizable(False, False)
    app.mainloop()
