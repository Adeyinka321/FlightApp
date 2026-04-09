import sqlite3
con = sqlite3.connect('airline.db')
cur = con.cursor() # Create table
cur.execute('''create table if not exists users(
            id integer primary key autoincrement,
            fullname varchar(20) unique not null, 
            username varchar (20) unique not null,
            userrole varchar(20) unique not null,
            password varchar(20) unique not null,
            remark varchar(40) unique not null

            )
            ''')

# flight table for flight details
cur.execute('''
            create table if not exists flights(
            id integer primary key autoincrement,
            flight_number varchar(20) unique not null,
            origin varchar(20) unique not null,
            departure_time varchar(20) unique not null,
            arrival_time varchar(20) unique not null,
            destination varchar(50) unique not null
  )
''')
con.commit()
con.close()