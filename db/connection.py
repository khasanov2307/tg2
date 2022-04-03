from sqlite3 import connect

conn = connect('price.db', check_same_thread=False)
cursor = conn.cursor()
