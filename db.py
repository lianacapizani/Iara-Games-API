
import os
from dotenv import load_dotenv
import psycopg2
from psycopg2 import sql

load_dotenv()


db_params = {
    'dbname': os.environ.get('DB_NAME'),
    'user': os.environ.get('DB_USER'),
    'password': os.environ.get('DB_PASS'),
    'host': os.environ.get('DB_HOST'),  
    'port': os.environ.get('DB_PORT')   
}

def get_db_connection():
    try:
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()
        print("Connected to the database")
        return cursor

    except Exception as error:
        print(f"Error connecting to PostgreSQL database: {error}")
