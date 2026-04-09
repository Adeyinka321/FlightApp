import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import subprocess
from tkinter import messagebox as msg
import sqlite3

UserRole = [
    'admin',
    'user'
]

def frontOffice():
    subprocess.Popen(['python', 'office.py'])
def main():
    subprocess.Popen(['python', 'admin.py'])


def login():
    Username = entry2.get()
    Userrole = entryuser.get()
    Password = entry3.get()

    if Username == '' or Password == '':
        msg.showinfo('Alert', 'Enter your username and password')
    elif Username == 'ur' or Password == '':
        msg.showinfo('Prompt', 'Unauthorize username and password')
        return
    con = sqlite3.connect(
        'airline.db'
    )
    cur= con.cursor()
    cur.execute('''
    select * from users where username = ? and password = ? ''',(Username, Password))
    result = cur.fetchone()

    if result:
        msg.showinfo('Alert', 'Login Successfully')

        master.destroy()
        if Userrole.lower() == 'admin':
            main()
        elif Userrole.lower() == 'user':
            frontOffice()
    else:
        msg.showwarning('unauthorized Access')
        con.close()

master = tk.Tk()
master.geometry('400x400+300+0')
master.title('Signin Page')
master.configure(background = '#40ffdc')

image = Image.open('bg.jpg').convert('RGBA')
image = image.resize((400,350))

image.putalpha(80)
photo = ImageTk.PhotoImage(image)

bg_label = tk.Label(master, image = photo, bg = '#FAF6E3')
bg_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)
bg_label.image = photo

label1 = tk.Label(master, text = 'login', font = ('verdana', 25, 'bold'), 
              fg = '#AC9008', bg = '#FAF6E3')
label1.grid(row = 0, column = 0, columnspan = 2, pady = 20)

label2 = tk.Label(master, text = 'Username', font = ('verdana', 13, 'bold'),
                   fg = '#AC9008', bg = '#FAF6E3')
label2.grid(row = 1, column = 0)

entry2 = tk.Entry(master, width = 35, relief = 'flat')
entry2.grid(row = 1, column = 1, pady = 20)

labeluser = tk.Label(master, text = 'User Role', font = ('verdana', 13, 'bold'),
                 fg = '#AC9008', bg = '#FAF6E3')
labeluser.grid(row = 2, column = 0, padx = 20)

entryuser = ttk.Combobox(width = 35, value = UserRole)
entryuser.grid(row = 2, column = 1, pady = 20)

label3 = tk.Label(master, text = 'Password', font = ('verdana', 13, 'bold'), 
                  fg = '#AC9008', bg = '#FAF6E3')
label3.grid(row = 3, column = 0, padx = 10)

entry3 = tk.Entry(master, width = 35, relief = 'flat')
entry3.grid(row = 3, column = 1, pady = 20)

login_btn = tk.Button(master, text = 'Login', font = ('verdana', 13, 'bold'), 
                      fg = '#FAF6E3', bg = '#AC9008', width = 10) #command = login
login_btn.grid(row = 4, column = 0, columnspan = 2, pady = 30)








master.mainloop()