import os
from dotenv import load_dotenv
import psycopg2
from sqlalchemy import create_engine
import pandas as pd

load_dotenv()

user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
database = os.getenv('DB_NAME')

def load_data(query):
    try:
        print('Connecting to database..')
        conn = psycopg2.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password
        )
    except Exception as error:
        print("Error: %s" % error)
        return None
        
    print("Connection successful!")
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df