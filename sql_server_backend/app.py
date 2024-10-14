from flask import Flask, jsonify, request
import pyodbc
from config import Config

app = Flask(__name__)

# SQL Server connection string for Windows Authentication
conn_str = (
    f"DRIVER={Config.DRIVER};"
    f"SERVER={Config.SERVER};"
    f"DATABASE={Config.DATABASE};"
    f"Trusted_Connection=yes;"  # This enables Windows Authentication
)

@app.route('/')
def index():
    return "Welcome to the API! Use /api/data for GET and POST requests."

@app.route('/api/data', methods=['GET'])
def get_data():
    try:
        with pyodbc.connect(conn_str) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM [dbo].[Categories]")  # Replace with your table name
            rows = cursor.fetchall()
            columns = [column[0] for column in cursor.description]
            results = [dict(zip(columns, row)) for row in rows]
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/data', methods=['POST'])
def insert_data():
    try:
        data = request.json
        # Replace with your insert query and the correct data structure
        with pyodbc.connect(conn_str) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO YourTableName (Column1, Column2) VALUES (?, ?)", 
                           (data['column1'], data['column2']))
            conn.commit()
        return jsonify({"message": "Data inserted successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
