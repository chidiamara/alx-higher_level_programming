#!/usr/bin/python3
"""
takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa
"""
if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("""SELECT cities.name
                FROM cities
                LEFT JOIN states
                ON cities.state_id = states.id
                WHERE states.name = %s
                ORDER BY cities.id ASC""", (argv[4],))
    cities = cur.fetchall()
    i = 0
    for city in cities:
        if i != 0:
            print(", ", end="")
        i += 1
        print(city[0], end="")
    print()
    cur.close()
    db.close()
