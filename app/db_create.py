import psycopg2

conn = psycopg2.connect(
    database='postgres',
    user='marcos.soares',
    password='B@gaio2247',
    host='localhost',
    port='5432',
)
conn.autocommit = True
cursor = conn.cursor()
cursor.execute('CREATE DATABASE customer_data_db')
