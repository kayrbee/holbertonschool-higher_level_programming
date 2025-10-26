#!/usr/bin/python3
"""
Write a script that lists all cities from the database hbtn_0e_4_usa

Your script should take 3 arguments: mysql username, mysql password and database name
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by cities.id
You can use only execute() once
Results must be displayed as they are in the example below
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
    db = MySQLdb.connect(
        host='localhost',
        user=user,
        passwd=password,
        database=database,
        port=3306,
        charset="utf8")
    cur = db.cursor()

    # Execute case-sensitive query
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        LEFT JOIN states
        ON cities.state_id=states.id
        ORDER BY cities.id ASC
        """
    cur.execute(query)
    # Fetch results and print them. Rows are returned as tuples by default
    rows = cur.fetchall()
    for row in rows:
        print(row)
    # Close the cursor and connection
    cur.close()
    db.close()
