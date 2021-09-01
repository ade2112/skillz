https://pynative.com/python-postgresql-tutorial/


Table of contents

1.  Install Psycopg2 using pip command
2.  Verifiy Psycopg2 installation
3.  Python PostgreSQL database connection
4.  Python example to connect PostgreSQL database connection
5.  Important Points
6.  Create a PostgreSQL table from Python
7.  The mapping between Python and PostgreSQL types
8.  Constants and numeric conversion
9.  Perform PostgreSql CRUD operations from Python
10. Working with PsotgreSQl date and time in Python
11. Call PostgreSql CRUD operations from Python
12. Python PostgreSQL Transaction management
13. Python PostgreSQL Connection Pooling
14. Python PostgreSQl Exercise Project





<!-- How to Connect to PostgreSQL in Python -->

1.  install psycopg2
    pip install psycopg2

    #install psycopg2 using anaconda
    conda install -c anaconda psycopg2

2.  Use the connect() method
    Use the psycopg2.connect() method with the required arguments to connect MySQL. It would return an Connection object if the connection established successfully

3.  Use the cursor() method
    Create a cursor object using the connection object returned by the connect method to execute PostgresSQL queries from Python.

4.  Use the execute() method
    The execute() methods run the SQL query and return the result

5.  Extract result using fetchall()
    Use cursor.fetchall() or fetchone() or fetchmany() to read query result

6.  Close cursor and conenction objects
    Use cursor.close() and connection.close() method to close PostgreSQL connections after your work completes

Remember to commit your changes to the database using the commit() method.


The Mapping between Python and PostgreSQL types

Pytho               PostgreSLQ
None        ->      Null
bool        ->      bool
float        ->      real or double
int        ->       smallint integer bigint
Decimal    ->       numeric
str        ->       varchar text
date       ->       date
time        ->      time timetz
datetime    ->      timestamp timestamptz
timedelta   ->      interval
list        ->      ARRAY
tuple        ->     Composite types IN syntax
dict        ->      hstore


Constants & numeric conversion
When you try to insert Python None and boolean values such as True and False into PostgreSQL, it gets converted into the proper SQL literals. The same case is with Python numerical types. It gets converted into equivalent PostgreSQL types.

For example, When you execute an insert query, Python numeric objects such as int, long, float, Decimal are converted into a PostgreSQL numerical representation. When you read from the PostgreSQL table, integer types are converted into an int, floating-point types are converted into a float, numeric/Decimal are converted into Decimal.




Working with PostgreSQL date and time in Python

This section will demonstrate how to work with PostgreSQL date and timestamp data types in Python and vice-versa. Most of the time, we work with date and time data. We insert date and time into the table and also read from it in our application whenever required.

In a usual scenario, when you execute the insert query with the datetime object, the Python psycopg2 module converts it into a PostgreSQL timestamp format to insert it in the table.

And when you execute a SELECT query from Python to read timestamp values from the PostgreSQL table, the psycopg2 module converts it into a datetime object.

We are using the “Item” table for this demo. Please copy and execute the below query on your PostgreSQL query tool to have adequate data for this operation.



Python PostgreSQL Connection Pooling Using Psycopg2
