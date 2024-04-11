import sqlite3

def insert_data(name: str, value: int):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("INSERT INTO example_table (name, value) VALUES (?, ?)", (name, value))
    conn.commit()
    conn.close()
    return {"message": "Data inserted successfully"}

def read_data():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('SELECT * FROM example_table')
    result = c.fetchall()
    conn.close()
    return result
