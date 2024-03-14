import psycopg2
from dotenv import load_dotenv
import os
import time

load_dotenv()

def connect():
    while True:
        try:
            conn = psycopg2.connect(host=os.environ['DATABASE_HOSTNAME'], 
                                    database=os.environ['DATABASE_NAME'], 
                                    user=os.environ['DATABASE_USERNAME'],
                                    password=os.environ['DATABASE_PASSWORD'])
            print("Database connection was successful!")
            break
        except Exception as error:
            print(f"Connecting to database failed: {error}")
            time.sleep(2)
    return conn