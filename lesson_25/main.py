from psycopg_example.connection import Connection


connection = Connection()

cursor  = connection.cursor
cursor.execute("select * from products;")

print(cursor.fetch_all())
