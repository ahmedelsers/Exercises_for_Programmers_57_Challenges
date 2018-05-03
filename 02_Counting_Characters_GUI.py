#!/usr/bin/env python3

import tkinter as tk


class CountChar(tk.Tk):
    def __init__(self):
        super().__init__()

        self.label = tk.Label(self, text="Text:")
        self.label.grid(row=0, column=0)

        self.string = tk.Entry(self)
        self.string.grid(row=0, column=1)

        self.count = tk.Button(self, text="Count")
        self.count.bind("<Button-1>", self.print_count)
        self.count.grid(row=0, column=2)

        self.CountOutput = tk.StringVar()
        self.count = tk.Label(self, textvariable=self.CountOutput)
        self.count.grid(row=1, column=1)


    def print_count(self, event=None):
        if self.string.get():
            self.CountOutput.set("{} has {} characters".format(self.string.get(),
                                                               len(self.string.get())))
        else:
            self.CountOutput.set("You must enter something to count!")



if __name__ == "__main__":
    app = CountChar()
    app.title("Character Counter")
    app.resizable(False, False)
    app.mainloop()
