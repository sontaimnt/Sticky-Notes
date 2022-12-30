#Sticky.py
from tkinter import *
from tkinter.filedialog import askopenfile , asksaveasfile
from random import randint
#Program
root=Tk()
root.title('Sticky Notes')
root.geometry('300x300')
#Main Box
text=Text(bg='#f9f06d' , width=300 , height=300 , font=('Fira Sans Book' , 12))
text.pack()
#Variables
italictext=False
boldtext=False
#Colors Class
class Colors():
    def random_f():
        color=randint(1 , 6)
        if color==int(1):
            Colors.yellow_f()
        elif color==int(2):
            Colors.red_f()
        elif color==int(3):
            Colors.orange_f()
        elif color==int(4):
            Colors.green_f()
        elif color==int(5):
            Colors.blue_f()
        elif color==int(6):
            Colors.purple_f()

    def red_f():
        text.configure(bg="#F86052" , fg="#F2F1EF")

    def orange_f():
        text.configure(bg="#FDBE71")
    
    def yellow_f():
        text.configure(bg="#f9f06d")

    def green_f():
        text.configure(bg="#8FF0A3")

    def blue_f():
        text.configure(bg="#99C2F0")

    def purple_f():
        text.configure(bg='#DC8ADE')
    
#Bold Text
def bold():
    global boldtext

    if boldtext==False:
        boldtext=True
        text.configure(font=('Fira Sans Book' , 12 , 'bold'))
    else:
        boldtext=False
        text.configure(font=('Fira Sans Book' , 12))

def italic():
    global italictext

    if italictext==False and boldtext==True:
        italictext=True
        text.configure(font=('Fira Sans Book' , 12 , 'bold' , 'italic'))
    elif italic==False and boldtext==False:
        italictext=True
        text.configure(font=('Fira Sans Book' , 12 , 'italic'))
    elif italictext==True and boldtext==True:
        italictext==False
        text.configure(font=("Fira Sans Book", 12 , 'bold'))
    else:
        italictext==False
        text.configure(font=("Fira Sans Book", 12))

class FileOperations():
    def open_f():
        file = askopenfile()
        text.delete(1.0 , END)
        text.insert(END , file.read())
    def save_f():
        file = asksaveasfile()
        file.write(text.get(0.0 , END))
#Menu
menubar=Menu(root , bg='#F2F1EF' , fg='#3C3846')
#File Menu
fileMenu=Menu(root ,  bg='#F2F1EF' , fg='#3C3846' , tearoff=0)
#Colors Menu
colorMenu=Menu(root ,  bg='#F2F1EF' , fg='#3C3846' , tearoff=0)
colorMenu.add_command(label="Red" , command=Colors.red_f)
colorMenu.add_command(label="Orange" , command=Colors.orange_f)
colorMenu.add_command(label="Yellow" , command=Colors.yellow_f)
colorMenu.add_command(label="Green" , command=Colors.green_f)
colorMenu.add_command(label="Blue" , command=Colors.blue_f)
colorMenu.add_command(label="Purple" , command=Colors.purple_f)
colorMenu.add_command(label="Random Colors" , command=Colors.random_f)
#Format Menu
formatmenu=Menu(root ,  bg='#F2F1EF' , fg='#3C3846' , tearoff=0)
formatmenu.add_command(label='Bold' , command=bold)
formatmenu.add_command(label='Italic' , command=italic)
#File Menu
fileMenu.add_command(label="Open File" , command=FileOperations.open_f)
fileMenu.add_command(label="Save File" , command=FileOperations.save_f)
#Menu Config
menubar.add_cascade(label='File' , menu=fileMenu)
menubar.add_cascade(label='Format' , menu=formatmenu)
menubar.add_cascade(label="Colors" , menu=colorMenu)
root.configure(menu=menubar)
#Execution
root.mainloop()
