import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Create a table
c.execute('''CREATE TABLE IF NOT EXISTS example_table
             (id INTEGER PRIMARY KEY, name TEXT, value INTEGER)''')

# Insert data into the table
c.execute("INSERT INTO example_table (name, value) VALUES (?, ?)", ('test', 123))
conn.commit()

# Retrieve data from the table
c.execute('SELECT * FROM example_table')
print(c.fetchall())

# Close the connection
conn.close()
