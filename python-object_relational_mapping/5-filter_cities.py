#!/usr/bin/python3
"""
Write a script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa

Your script should take 4 arguments: mysql username, mysql password,
database name and state name (SQL injection free!)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by cities.id
You can use only execute() once
The results must be displayed as they are in the example below
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
    state = arguments[4]

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
        SELECT cities.name
        FROM cities
        LEFT JOIN states
        ON cities.state_id=states.id
        WHERE states.name = %s
        """
    cur.execute(query, (state,))
    # Fetch results and print them. Rows are returned as tuples by default
    rows = cur.fetchall()
    cities = [row[0] for row in rows]
    print(", ".join(cities))
    # Close the cursor and connection
    cur.close()
    db.close()
