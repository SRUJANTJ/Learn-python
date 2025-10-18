# Database Query Results
# When fetching records from a database, using an iterator allows you to process records one at a time, reducing memory usage.
import sqlite3

# Connect to the database (it will create if not exists)
conn = sqlite3.connect('example.db')
cur = conn.cursor()

# Create table
cur.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
)
''')

# Insert sample data
cur.execute("INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com')")
cur.execute("INSERT INTO users (name, email) VALUES ('Bob', 'bob@example.com')")

# Save changes and close
conn.commit()
conn.close()
