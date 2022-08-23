from cgitb import text
from ctypes import sizeof
from email.mime import image
from re import A
from textwrap import fill
import tkinter as tk
from tkinter import *
from PIL import Image

root = Tk()
root.title('Learn Tkinter')
root.configure(width=700, height = 700)
root.configure(bg='white')
root.geometry('700x700')





#WIN3
def open_new3_win3():
    win3 = Toplevel(root)
    win3.geometry('700x700')
    win3.title('Learn Tkinter #3')
    ## Labels, Buttons and code.




## WIN2 / WINTWO / WINDOW 2
def open_new2_win2():
    wintwo = Toplevel(root)
    wintwo.geometry('700x700')
    wintwo.title('Learn Tkinter #2')
    #label wintwo 1
    labelwintwo1 = Label(wintwo, text = 'Then you need to do /root.configure(width=700,height=700)')
    labelwintwo1.grid(row=2,column=2)
    # 2nd label win2 / wintwo
    labelwintwo2 = Label(wintwo,text ='Then you need /root.configure(bg = "white")' )
    labelwintwo2.grid(row=6,column=8)
    # win2 label button next 2 / wintwo 
    buttonnext2 = Button(wintwo,text = 'Next Page!' , command= open_new3_win3)
    buttonnext2.grid(column = 1, row = 3)
    















## WIN1 / WINONE / LABEL = LABELWIN1
def open_new_win1():

    win1 = Toplevel(root)

    win1.geometry('700x700')

    win1.title("Learn Tkinter #1")
    
    ##labelwin1
    labelwin1 = Label(win1,text = 'Lets Start with importing tkinter, tkinter is built in, so /from tkinter import */ (slashes are not used)')
    labelwin1.grid(row = 0, column = 1)
    #label win 1 2

    labelwinone2 = Label(win1,text='Now, you need to do /root = Tk()/ then /root.title(then title of name in qoutation mark)')
    labelwinone2.grid(row = 1,column = 1)
    #next button 1
    buttonnext1 = Button(win1,text = 'Next', command = open_new2_win2)
    buttonnext1.grid(row = 2,column=1)
    
    
    
    
    



##properties to label,grid 

start_label =  Label(root, text = 'Welcome', font = ('Arial',12), bg = 'white')
start_label.grid(row = 0, column=1)

##label2
label2 = Label(root,text = 'Made by MrMatthew ', font =('Arial', 12), bg = 'white', )
label2.grid(row = 4, column=0)

##introlabel
intro_label = Label(root,text = 'Learn Tkinter', font = ('Arial', 12),bg = 'white')
intro_label.grid(row = 4, column=6)
##button
button1 = Button(root, text = 'Start!', command= open_new_win1)
button1.grid(row = 4, column=8)





#configuration

root.mainloop()  