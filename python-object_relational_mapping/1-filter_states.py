#!/usr/bin/python3
"""
Write a script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa:

Your script should take 3 arguments: mysql username, mysql
password and database name (no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported
"""
if __name__ == '__main__':
    """ Your code should not be executed when imported """
    import MySQLdb
    import sys
    # Get argv inputs
    arguments = sys.argv
    user = arguments[1]
    password = arguments[2]
    database = arguments[3]

    # Connect to db
    db = MySQLdb.connect(host='localhost', user=user,
                         passwd=password, database=database, port=3306)
    cur = db.cursor()

    # Execute query
    cur.execute("SELECT * FROM states WHERE name LIKE 'L%' BY id ASC")
    # Fetch results and print them. Rows are returned as tuples by default
    rows = cur.fetchall()
    for row in rows:
        print(row)
    # Close the cursor and connection
    cur.close()
    db.close()
