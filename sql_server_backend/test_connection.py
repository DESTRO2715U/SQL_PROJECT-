import pyodbc

# Adjust these variables based on your configuration
conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=PANDA\\CLARRR;"  # Replace with your server name
    "DATABASE=InventoryDB;"  # Replace with your database name
    "Trusted_Connection=yes;"  # This enables Windows Authentication
)

try:
    with pyodbc.connect(conn_str) as conn:
        print("Connection successful!")
except Exception as e:
    print(f"Error: {e}")
