import tkinter as tk
import tkinter.messagebox as message
import sqlite3
master = tk.Tk()
master.geometry('1000x1000+300+0')
master.title('Admin Dashboard')
master.configure(background = '#141444')
search_visible = False
import subprocess
from tkinter import ttk
from tkinter import END

#CRUD
# C = CREATE
# R = READ
# U = Update
# D = DELETE

def frontdesk():
    subprocess.Popen(['python', 'office.py'])


def fetch_data():
    con = sqlite3.connect('airline.db')
    cur = con.cursor()
    cur.execute('''
                select * from flights
                ''')
    rows = cur.fetchall()
    con.close
    return rows

def display_data():
    for row in fetch_data():
        tree.insert('', END, value = row)


def add():
    flight_number = entry1.get()
    origin = entry2.get()
    departure_time = entry3.get()
    arrival_time = entry4.get()
    destination = entry5.get()

    if flight_number == '' or origin == '' or departure_time == '' or arrival_time == '' or destination == '':
        message.showinfo('prompt', 'Empty Record Not Allowed , Please Fill The Form')
    
    elif flight_number and origin and departure_time and arrival_time and destination:
        con = sqlite3.connect('airline.db')
        cur = con.cursor()
        cur.execute('''
                insert into flights(flight_number, origin, departure_time, arrival_time, destination)
                    values(?,?,?,?,?)''', (flight_number, origin, departure_time, arrival_time, destination))
    
        message.showinfo('Alert', 'Record sent to Flight Table')
        con.commit()
        con.close()

        entry1.delete(0, tk.END)
        entry2.delete(0, tk.END)
        entry3.delete(0, tk.END)
        entry4.delete(0, tk.END)
        entry5.delete(0, tk.END )

def delete():
    flight_number = entry1.get()

    if flight_number == '':
        message.showerror('Error', 'Enter Flight Number')
        return
    con = sqlite3.connect('airline.db')
    cur = con.cursor()

    cur.execute('DELETE FROM flights WHERE flight_number = ?', (flight_number, ))
    con.commit()
    
    if cur.rowcount == 0:
        message.showinfo('Result', 'No record found')
    else:
        message.showinfo('Success', 'Flight delete')
    
    con.close()

def search():
    global search_visible
    flight_number = entry1.get()

    if flight_number== '':
        message.showinfo('Prompt', 'Enter Flight Number')
        return
    
    if not search_visible:
        con = sqlite3.connect('airline.db')
        cur = con.cursor()

        try:
            cur.execute('''
                SELECT flight_number, origin, departure_time, arrival_time, destination
                FROM flights
                WHERE flight_number = ? ''', (flight_number,))
            result = cur.fetchone()

            if result:
                entry1.delete(0, tk.END)
                entry2.delete(0, tk.END)
                entry3.delete(0, tk.END)
                entry4.delete(0, tk.END)
                entry5.delete(0, tk.END)

                entry1.insert(0, result[0])
                entry2.insert(0, result[1])
                entry3.insert(0, result[2])
                entry4.insert(0, result[3])
                entry5.insert(0, result[4])

                search_visible = True
            
            else:
                message.showinfo('Not Found', 'Flight Not Found')

            con.close()
        except Exception as e:
            message.showerror('Error', str(e))
    else:
        entry1.delete(0, tk.END)
        entry2.delete(0, tk.END)
        entry3.delete(0, tk.END)
        entry4.delete(0, tk.END)
        entry5.delete(0, tk.END)

        search_visible = False

def update():
    flight_number = entry1.get()
    origin = entry2.get()
    departure_time = entry3.get()
    arrival_time = entry4.get()
    destination = entry5.get()


    if flight_number and origin and departure_time and arrival_time and destination:
        con = sqlite3.connect('airline.db')
        cur = con.cursor()
        cur.execute('''
                    update flights set origin = ?, departure_time = ?, arrival_time = ?, destination = ?
                    where flight_number = ?
                    ''', (origin, departure_time, arrival_time, destination, flight_number))
        
        con.commit()
        con.close()

        if cur.rowcount>0:
            message.showinfo('Alert', 'Record Updated Successfully')


        else:
            message.showinfo('prompt', 'Record Not Found')
    else:
        message.showinfo('prompt', 'Input Flight Number')





label = tk.Label(master, text = 'Flight Dashboard', font = ('verdana', 50, 'bold'), 
            fg = '#fff', bg = '#141444' )
label.place(x = 250, y = 0)

leftframe = tk.Frame(master, width = 500, height = 1000)
leftframe.place(x = 0, y = 150)

label1 = tk.Label(leftframe, text = 'Flight Number', fg = '#000000', 
                  font = ('verdana', 12, 'bold'))
label1.place(x = 0, y = 30)

entry1 = tk.Entry(leftframe, width = 50, border = 5)
entry1.place(x = 150, y = 30)

label2 = tk.Label(leftframe, text = 'origin', fg = '#000000', 
                  font = ('verdana', 12, 'bold'))
label2.place(x = 0, y = 60)

entry2 = tk.Entry(leftframe, width = 50, border = 5)
entry2.place(x = 150, y = 50)

label3 = tk.Label(leftframe, text = 'Depature Time', fg = '#000000', font = ('verdana', 12, 'bold'))
label3.place(x = 0, y = 90)

entry3 = tk.Entry(leftframe, width = 50, border = 5)
entry3.place(x = 150, y = 90)

label4 = tk.Label(leftframe, text = 'Arrival Time', fg = '#000000', font = ('verdana', 12, 'bold'))
label4.place(x = 0, y = 120)

entry4 = tk.Entry(leftframe, width = 50, border = 5)
entry4.place(x = 150, y = 120)

label5 = tk.Label(leftframe, text = 'Destination', fg = '#000000', font = ('verdana', 12, 'bold'))
label5.place(x = 0, y = 150)

entry5 = tk.Entry(leftframe, width = 50, border = 5)
entry5.place(x = 150, y = 150)

result_label = tk.Label(master, text = '', bg = 'yellow', width = 50)
result_label.place(x = 300, y = 300)
result_label.place_forget()

btnAdd = tk.Button(leftframe, text = 'Add Flight', fg = '#000000', bg = '#fff', command = add)
btnAdd.place(x = 150, y = 180)

btnSearch = tk.Button (leftframe, text = 'Search', command = search)
btnSearch.place(x = 240, y = 180)

btnUpdate = tk.Button(leftframe, text = 'Update Flight', bg = '#fff',  fg = '#000000', command = update)
btnUpdate.place(x = 290, y = 180)

btnDelete = tk.Button(leftframe, text = 'Delete Flight', command = delete)
btnDelete.place(x = 380, y = 180)

labelfront = tk.Button(master, text = 'Go to front desk', font = ('verdana', 30, 'bold'),
                 bg = 'white', fg = '#3b3b3f', command = frontdesk)
labelfront.place(x = 600, y = 70)

rightframe = tk.Frame(master, width = 500, height = 1000, bg = '#80184C')
rightframe.place(x = 500, y = 150)

labelright = tk.Label(rightframe, text = 'flight booking')
labelright.place(x = 0, y = 0)
cols = ['ID', 'Flight Number', 'Origin', 'Departure Time', 'Arrival Time', 'Destination']
tree = ttk.Treeview(rightframe, column = cols, show = 'headings')

for col in cols:
    tree.heading(col, text = col)
    tree.column(col, width = 80)

tree.place(x = 0, y = 50)


display_data()








master.mainloop()  
