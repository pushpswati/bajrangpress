#!/usr/bin/python
import psycopg2
from config import config

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
		
        # create a cursor
        cur = conn.cursor()
        
	# execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
       
	    # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()
    
    #How it works.

#First, read database connection parameters from the database.ini file.
#Next, create a new database connection by calling the connect() function.
#Then, create a new cursor and execute an SQL statement to get the PostgreSQL database version.
#After that, read the result set by calling the  fetchone() method of the cursor object.
#Finally, close the communication with the database server by calling the close() method of the cursor and connection objects.
#The connect() function raises the DatabaseError exception if an error occurred. To see how it works, we can change the #connection parameters in the database.ini file.