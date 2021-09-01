import psycopg2
from psycopg2.extras import RealDictCursor

import json

try:
    connection = psycopg2.connect(user="postgres",
                                  password="",
                                  host="localhost",
                                  port="5432",
                                  database="test")

    cursor = connection.cursor()
    # # Executing a SQL query to insert data into  table
    # insert_query = """ INSERT INTO mobile (ID, MODEL, PRICE) VALUES (1, 'Iphone12', 1100)"""
    # cursor.execute(insert_query)
    # connection.commit()
    # print("1 Record inserted successfully")
    # # Fetch result
    # cursor.execute("SELECT * from mobile")
    # record = cursor.fetchall()
    # print("Result ", record)

    # # Executing a SQL query to update table
    # update_query = """Update mobile set price = 1500 where id = 1"""
    # cursor.execute(update_query)
    # connection.commit()
    # count = cursor.rowcount
    # print(count, "Record updated successfully ")
    # # Fetch result
    # cursor.execute("SELECT * from mobile")
    # print("Result ", cursor.fetchall())

    # # Executing a SQL query to delete table
    # delete_query = """Delete from mobile where id = 1"""
    # cursor.execute(delete_query)
    # connection.commit()
    # count = cursor.rowcount
    # print(count, "Record deleted successfully ")
    # # Fetch result
    # cursor.execute("SELECT * from mobile")
    # print("Result ", cursor.fetchall())


     # Executing a SQL query to delete table
    select_query = """select * from courses"""
    cursor.execute(select_query)
    connection.commit()
    result = cursor.fetchall()
    # print("Result ", result)
    dict = dict()
    for r in result:
        (id, name, lead_lecturer, duration, price) = r
        dict[id] = {
            "name": name, 
            "lead_lecturer": lead_lecturer,
            "duration": duration,
            "price": price
        }
    # print (json.dumps(dict))

    with connection as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute("select * from courses")
            result = cursor.fetchall()
            print(json.dumps(result))

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")