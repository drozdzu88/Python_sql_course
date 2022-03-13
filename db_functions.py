import mysql.connector
from mysql.connector import Error

def create_server_connection(host_name, user_name, user_password):
    """
    Create connection with our databes.
    """
    
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password
            )
        print("MySQL Database connection succesful")
    except Error as err:
        print(f"Error: '{err}'")
    
    return connection


def create_database(connection, query):
    """
    Crating database
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")
        
def create_db_connection(host_name, user_name, user_password, db_name):
    """
    Connecting with database 
    """
    connection = None
    try: 
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password,
            database = db_name
            )
        print(f"MySQL {db_name} Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    
    return connection

def execute_query(connection, query):
    """
    This is going to take our SQL queries, stored in Python as strings, 
    and pass them to the cursor.execute() method to execute them on the server.

    """
    
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")
        
def read_query(connection, query):
    """ 
    this time using cursor.fetchall() instead of cursor.commit(). 
    With this function, we are reading data from the database and will 
    not be making any changes.
    """
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

def execute_list_query(connection, sql, val):      
    cursor = connection.cursor()
    try:
        cursor.executemany(sql, val)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        