import MySQLdb

def get_connection():    
    connection = MySQLdb.connect(
    host="localhost",
    user="root",     
    password="",
    database="hrdashboard")
    return connection

def execute_query(query, value):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(query, value)
    return cursor

def insert_data(query, value):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.executemany(query, value)
    connection.commit()
