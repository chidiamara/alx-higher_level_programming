#!/usr/bin/python3
"""
takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument
"""
if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name LIKE BINARY '{}%'
                ORDER BY states.id ASC""".format(argv[4]))
    states = cur.fetchall()
    for state in states:
        print(state)
    pass
    cur.close()
    db.close()
