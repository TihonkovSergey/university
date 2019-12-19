import psycopg2
from jcUserClass import User
from psycopg2 import sql

DB_NAME = 'postgres'
DB_USER = 'postgres'
DB_PASSWORD = 'postgres'
DB_HOST = 'localhost'

def get_all_users():
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
    records = []
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM users')
        records = cursor.fetchall()
    conn.close()
    users = []
    for rec in records:
        user = User(rec)
        users.append(user)
    return users