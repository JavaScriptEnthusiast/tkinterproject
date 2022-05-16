
from tkinter import *
from tkinter import ttk


#Using Notebook and Tkinter
display = Tk()
icon = PhotoImage(file= 'color.png')
display.iconphoto(True,icon)

bigPic = PhotoImage(file='bigPic.png')
bigSplash = PhotoImage(file='bigSplash.png')
backEnd = PhotoImage(file='backEnd.png')




#These are the callback functions that the terminal will print.
def t1():
    print("Engineering a modern web application can be compared to building a spaceship.")
    print("The front end needs to be visually appealing and responsive, requiring precision.")
    print("Companies such as google allow you to launch an app very quickly with back end services.")
    print("APIs are more flexible than ever, with a high number of services interacting to form one app.")
    print(" ")
def t2():
    print("Everything starts with the holy trinity of HTML, CSS, and Javascript.")
    print("Quality HTML and CSS can be written in lightspeed with libraries.")
    print("React has consolidated a lot of the JavaScript developers and established a monopoly.")
    print("DOM manipulation with frameworks has created a new level of complexity for web development.")
    print(" ")
def t3():
    print("With the invention of Node.JS, JavaScript can be written server side now.")
    print("Server rooms full of computers specialised to hold a massive amount of data supply the client side.")
    print("Frameworks such as Flask for Python, and Express for Javascript are used by developers for development.")
    print("New services such as Firebase turn the Backend into a service, which is optimal for new startups.") 
    print(" ")

quit = Button(display, text="exit application", command=display.quit)
quit.pack()


#These are the buttons that the User will click to see the text on the terminal.
nextButton1 = Button(display, text="The Big Picture", command=t1)
nextButton1.pack()

nextButton2 = Button(display, text="React's Big Splash", command=t2)
nextButton2.pack()

nextButton3 = Button(display, text="Behind the scenes", command=t3)
nextButton3.pack()

#Setting up the tabs to house the labels.
book = ttk.Notebook(display)
firstTab = Frame(book)

secondTab = Frame(book)

thirdTab = Frame(book)


#These are the tabs to house the labels.

book.add(firstTab, text="Modern Development")
book.add(secondTab,text="Front End")
book.add(thirdTab,text="Back End")
book.pack()

#The labels are images that explain what happens when the buttons are clicked.

Label(firstTab,image=bigPic, width=300,height=300) .pack()
Label(secondTab,image=bigSplash, width=300,height=300).pack()
Label(thirdTab,image=backEnd, width=300,height=300).pack()



#Nikola Petreski
#Final Project for Intro to Software Development
#Python Version 3.10
#This project will print to the terminal a paragraph about each of the three main sections.
#5/16/2022

display.mainloop()

