from pyodbc import (
    connect,
)



connection_string = (
    "DRIVER={PostgreSQL};"
    "User=postgres;"
    "Password=postgres;"
    "Database=test;"
    "Server=127.0.0.1;"
    "Port=5432;"
)

connection = connect(connection_string)
