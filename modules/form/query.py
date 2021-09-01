from db.postgres.connection import connection
from psycopg2.extras import RealDictCursor

# cursor
from db.postgres.pool import CursorFromConnectionFromPool
# models
from modules.form.model import Business


import json

# Executing a SQL query to insert data into  table
def insert_query(business: Business):
	id="momo"
	insert_query = f""" insert into business (id,full_name, business_email,role, service,team_size) values ({id},{business.businessName},{business.fullName},{business.businessEmail},{business.role}, {business.service}, {business.teamSize}) """
	with CursorFromConnectionFromPool() as cursor:
		cursor.execute(insert_query)
		data = cursor.fetchall()
		for i in data:
			print (i)		
		# return data
		
	

# # Fetch result
# def fetch_query():
#     cursor.execute("SELECT * from mobile")
#     record = cursor.fetchall()
#     print("Result ", record)

# # Executing a SQL query to update table
# def update_query():
#     update_query = """Update mobile set price = 1500 where id = 1"""
#     cursor.execute(update_query)
#     connection.commit()
#     count = cursor.rowcount
#     print(count, "Record updated successfully ")

# def delete_query():
#     # Executing a SQL query to delete table
#     delete_query = """Delete from mobile where id = 1"""
#     cursor.execute(delete_query)
#     connection.commit()
#     count = cursor.rowcount
#     print(count, "Record deleted successfully ")
