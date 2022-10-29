import sqlite3
import os
sql_con = sqlite3.connect('music_db')

cur = sql_con.cursor()
cur.execute('''CREATE TABLE class
        (id_class INTEGER PRIMARY KEY,
        name_class VARCHAR(30) not null);''')
cur.execute('''CREATE TABLE instrument
            (id_instrum INTEGER PRIMARY KEY,
            name_instrum VARCHAR(30) not null,
            id_class INTEGER,
            FOREIGN KEY id_class
                REFERENCES class(id_class));''')
cur.execute ('''CREATE TABLE musician
        (id_m integer primary key autoincrement,
        id_instrum integer,
        name_m varchar(30) not null,
        foreign key id_instrum
            references instrument(id_instrum));''')
sql_con.commit()
sql_con.close()

