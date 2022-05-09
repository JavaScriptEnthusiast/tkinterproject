from tkinter import *
from tkinter import ttk

display = Tk()

book = ttk.Notebook(display)

firstTab = Frame(book)

secondTab = Frame(book)

thirdTab = Frame(book)
book.add(firstTab, text="Modern Development")
book.add(secondTab,text="Front End")
book.add(thirdTab,text="Back End")
book.pack()

Label(firstTab,text="Modern Web apps feature Specialization, which in turn promotes reciprocity", width=100,height=100).pack()
Label(secondTab,text="Best practices are evolving rapidly with mass adoption of libraries and workflows", width=100,height=100).pack()
Label(thirdTab,text="Let's talk about creating value behind the scenes", width=100,height=100).pack()

display.mainloop()