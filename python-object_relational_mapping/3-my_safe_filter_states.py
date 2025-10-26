#!/usr/bin/python3
"""
Once again, write a script that takes in arguments and displays
all values in the states table of hbtn_0e_0_usa where name
matches the argument.
But this time, write one that is safe from MySQL injections!

Your script should take 4 arguments: mysql username, mysql password,
database name and state name searched (safe from MySQL injection)
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
    name = arguments[4]

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
        SELECT * FROM states
        WHERE name LIKE BINARY %s
        ORDER BY id ASC
        """
    cur.execute(query, (name,))
    # Fetch results and print them. Rows are returned as tuples by default
    rows = cur.fetchall()
    for row in rows:
        print(row)
    # Close the cursor and connection
    cur.close()
    db.close()
