import os
import time
from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    # Attempt to connect to the database with a retry mechanism (up to 15 attempts, 2 seconds apart)
    # This prevents the app from crashing if the MySQL container is still initializing.
    for attempt in range(15):
        try:
            connection = mysql.connector.connect(
                host=os.environ.get("MYSQL_HOST"),
                user=os.environ.get("MYSQL_USER"),
                password=os.environ.get("MYSQL_PASSWORD"),
                database=os.environ.get("MYSQL_DATABASE")
            )
            return connection
        except mysql.connector.Error as err:
            print(f"Database connection attempt {attempt + 1} failed: {err}")
            time.sleep(2)
    raise Exception("Could not connect to the database after several attempts.")

@app.route('/')
def home():
    db = get_db_connection()
    cursor = db.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS visitors (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255)
        )
    """)
    
    cursor.execute("INSERT INTO visitors (name) VALUES ('Parmesh Visitor')")
    db.commit()
    
    cursor.execute("SELECT COUNT(*) FROM visitors")
    count = cursor.fetchone()
    
    cursor.close()
    db.close()
    
    return render_template("index.html", count=count[0])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
