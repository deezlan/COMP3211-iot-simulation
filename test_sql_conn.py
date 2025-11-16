import pyodbc

conn_str = (
    "Driver={ODBC Driver 18 for SQL Server};"
    "Server=tcp:sqldbserver-deezlan.database.windows.net,1433;"
    "Database=comp3211-db;"
    "Uid=qnlm4525;"
    "Pwd=Flappyjack1321!;"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
    "Connection Timeout=30;"
)

try:
    conn = pyodbc.connect(conn_str)
    print("Connected successfully!")
    cursor = conn.cursor()
    cursor.execute("SELECT GETDATE();")
    for row in cursor:
        print("Current date/time from DB:", row[0])
except Exception as e:
    print("ERROR:", e)
