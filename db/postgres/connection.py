
import psycopg2
from psycopg2.extras import RealDictCursor
import json



# test database connection
connection = psycopg2.connect(user="postgres", password="", host="localhost", port="5432", database="test")
def check_connection():
    with connection as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute("select 1 + 1")
            result = cursor.fetchall()
            print("connection was successful")


db={
	"local":'psycopg2.connect(user="postgres", password="", host="localhost", port="5432", database="test")',
	"prouction":""
}