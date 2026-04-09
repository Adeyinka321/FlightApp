# create a page with full name, username and password
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox as msg

import sqlite3 
import subprocess
# import hashlib
from tkinter import ttk

UserRole = [
    'admin',
    'user'
]

top = Tk()
top.geometry('500x400+300+0')
top.title('Signup Page')
top.configure(background='#40ffdc')
image = Image.open('bg.jpg')
photo = ImageTk.PhotoImage(image)

def signup():
    subprocess.Popen(['python', 'signin.py'])

def sign():
    fullname = entry2.get()
    username = entry3.get()
    userrole = entryuser.get()
    password = entry4.get()
    remark = text5.get('1.0', 'end')

    if fullname == '' or username == '' or password == '' or remark == '':
        msg.showinfo('alert', 'Empty Record Not Allowed! Please Fill The Form.')

    else:
        con = sqlite3.connect('airline.db')
        cur = con.cursor()
    try:
        cur.execute('''insert into users(fullname, username, userrole, password, remark)
                    values(?,?,?,?,?)''',
                    (fullname, username, userrole, password, remark))
        con.commit()
        msg.showinfo('Alert', 'Successfully Registerred')
        con.close()
        top.destroy()
        signup()
    
    except sqlite3.IntegrityError:
        msg.showinfo('Alert', 'User already exists!')

imagelabel = Label(top, image = photo)
imagelabel.place(relheight = 1, relwidth = 1)

label1 = Label(top, text = 'Signup Page', font = ('verdana', 10, 'bold'), 
                                                  foreground = 'black', background = 'white')
label1.grid(row = 0, column = 1)

label2 = Label(top, text = 'Full Name:', font = ('verdana', 10, 'bold'),
                foreground = 'black', background = 'white')
label2.grid(row = 1, column =0)

entry2 = Entry(top, width = 50)
entry2.grid(row = 1, column = 1, padx = 10)

label3 = Label(top, text = 'Username:', font = ('verdana', 10, 'bold'),
                foreground = 'black', background = 'white')
label3.grid(row = 2, column = 0)


entry3 = Entry(top, width = 50)
entry3.grid(row = 2, column = 1)

labeluser = Label(top, text = 'User Role', font = ('verdana', 10, 'bold'), 
                  fg = 'white', bg = 'black')
labeluser.grid(row = 3, column = 0)

entryuser = ttk.Combobox(width = 50, values = UserRole)
entryuser.grid(row = 3, column = 1)

label4 = Label(top, text = 'Password:', font = ('verdana', 10, 'bold'), 
               foreground = 'black', background = 'white')
label4.grid(row = 4, column = 0)

entry4 = Entry(top, width = 50, show = '*')
entry4.grid(row = 4, column = 1)

label5 = Label(top, text = 'Remark', font = ('verdana', 10, 'bold'), 
               foreground = 'black', background = 'white')
label5.grid(row = 5, column = 0)

text5 = Text(top, width = 40, height = 10)
text5.grid(row = 5, column = 1)

btn = Button(top, text = 'Sign Up Page', font = ('verdana', 10, 'bold'),
              foreground = 'black', background = 'white', width = 20, command=sign)
btn.grid(row = 6, column = 1)





top.mainloop()