import psycopg2
import time
import random
import string
# this code is generated to fill database

COUNT_EMPLOYEE = 100000

# make random string
def Random_String(size=6, chars=string.ascii_lowercase):
    return "".join(random.choice(chars) for x in range(size))

try:
    # connection 
    connection_string = "dbname='assignment2' user='sangjin' host='localhost' password='1234'"
    connection1 = psycopg2.connect(connection_string)
    connection1.autocommit=True
    pc = connection1.cursor()

    # Employee ( ssum(int), name(char), manager(char), dept(int), salary(int), numfriends(int))
    for x in range(COUNT_EMPLOYEE):
        query = "INSERT INTO employee values ( %s, %s, %s, %s, %s, %s)"
        if x / 10000 < 1:
            #attri = [ x , Random_String(random.randint(7, 10)), Random_String(random.randint(7, 10)), 1, random.random()*1000, random.randint(1, 10)]
            pc.execute(query, (x , Random_String(random.randint(7, 10)), Random_String(random.randint(7, 10)), 1, random.random()*1000, random.randint(1, 10)))
        else :
            #attri = [ x , Random_String(random.randint(7, 10)), Random_String(random.randint(7, 10)), random.randint(2, 10), random.random()*1000, random.randint(1, 10)]
            pc.execute(query, (x , Random_String(random.randint(7, 10)), Random_String(random.randint(7, 10)), random.randint(2, 10), random.random()*1000, random.randint(1, 10)))
        #pc.execute(query, attri)
    
    pc.close()
except Exception as e:
    print("can't connect")
    print(e)

