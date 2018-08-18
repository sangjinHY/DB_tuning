import psycopg2
import time
import random
import string
# this code is test for sql

# test SQL

# -Arithmetic expressions
#   WHERE salary/12 >= 100;
#   -> WHERE salary >= 100*12;

# -Substring expressions
#   WHERE SUBSTR(name, 1, 1) = ‘g’;
#   -> WHERE name = 'g*' 
COUNT_EMPLOYEE = 100000


try:
    # connection 
    connection_string = "dbname='assignment2' user='sangjin' host='localhost' password='1234'"
    connection1 = psycopg2.connect(connection_string)
    connection1.autocommit=True
    pc = connection1.cursor()

    # Employee ( ssum(int), name(char), manager(char), dept(int), salary(int), numfriends(int))
    ## test 1
    #           case 1
    query = "select * from employee where salary/12 > 100"
    start_time = time.time()
    pc.execute(query)
    end_time = time.time()

    print(end_time - start_time)

    #           case 2
    query = "select * from employee where salary > 100*12"
    start_time = time.time()
    pc.execute(query)
    end_time = time.time()

    print(end_time - start_time)

    #           end


    ## test 2
    #           case 1
    query = "select * from employee WHERE SUBSTR(name, 1, 1) = 'g'"
    start_time = time.time()
    pc.execute(query)
    end_time = time.time()

    print(end_time - start_time)
    
    #           case 2
    query = "select * from employee WHERE name = 'g*'"
    start_time = time.time()
    pc.execute(query)
    end_time = time.time()

    print(end_time - start_time)

    #           end
    pc.close()
except Exception as e:
    print("can't connect")
    print(e)

