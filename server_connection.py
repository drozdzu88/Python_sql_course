import mysql.connector
from mysql.connector import Error

def create_server_connection(host_name, user_name, user_password):
    """
    Create connection with our databes.

    Parameters
    ----------
    host_name : string
        DESCRIPTION.
    user_name : string
        DESCRIPTION.
    user_password : string
        DESCRIPTION.
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