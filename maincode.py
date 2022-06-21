# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from tkinter import *
from tkinter.ttk import *
from converter2 import encrypt
# creates a Tk() object
master = Tk()
 
# sets the geometry of main
# root window
master.geometry("700x350")
master.title('MORSE CODE')
def open_decode():
   exec(open("eye_blink.py").read())

# function to open a new window
# on a button click
def openNewWindow():
    def printInput():
        inp = inputtxt.get(1.0, "end-1c")
        
        lbl.config(text = encrypt(inp.upper()),font=("Arial", 25))

    # Toplevel object which will
    # be treated as a new window
    frame = Toplevel(master)
    frame.title('ENCODE')
    # sets the title of the
    # Toplevel widget
    frame.title("New Window")
 
    # sets the geometry of toplevel
    frame.geometry("700x350")
 
    # A Label widget to show in toplevel
    # TextBox Creation
    inputtxt = Text(frame,
                   height = 2,
                   width = 50)
    inputtxt.pack(pady = 50)
  
    # Button Creation
    printButton = Button(frame,
                        text = "GENERATE MORSE CODE", 
                        command = printInput)
    printButton.pack(pady = 30)
  
    # Label Creation
    lbl = Label(frame, text = "")
    lbl.pack()
    frame.mainloop()
 
 
 
# a button widget which will open a
# new window on button click

btn = Button(master,
             text ="\n\n\nENCODE\n\n\n",
             width=30,
             command = openNewWindow)
btn.pack(pady = 20)

btn = Button(master,
             text ="\n\n\nDECODE\n\n\n",
             width=30,
             command = open_decode)
btn.pack(pady = 20)


 
# mainloop, runs infinitely
mainloop()