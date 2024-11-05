import psycopg2
import os

def connect():
    conn = psycopg2.connect(os.getenv('DATABASE_URL'))
    return conn


