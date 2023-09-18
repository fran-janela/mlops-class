import os
import psycopg2
import os
from dotenv import load_dotenv

# Reading .env and creating environment variables
load_dotenv()

# Reading environment variable
host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_DATABASE")
port = os.getenv("DB_PORT")

## Import PreProcessed Data
conn = psycopg2.connect(database = database, 
                        user = user, 
                        host= host,
                        password = password,
                        port = port)

print("Database connected successfully")
cur = conn.cursor()

with open(os.path.join(os.path.dirname(__file__), "../data/", "view.sql")) as f:
    cur.execute(f.read())
    conn.commit()
print("View Created")

# Close communication with the database
cur.close()
conn.close()