pipimport csv
import psycopg2
import time
# normal insert
try:
    connection_string = "dbname='assignment1' user='sangjin' host='localhost' password='1234'"

    connection1 = psycopg2.connect(connection_string)
    connection1.autocommit=True
    pc = connection1.cursor()

    f = open("auth.tsv", encoding="utf-8", errors='replace')
    start = time.time()
    for line in csv.reader(f, delimiter='\t'):
        query = "INSERT INTO auth values ( '"+ line[0]+'\',\''+line[1] + "')"
        if(pc.execute(query) == 0):
            raise Exception("fuck")
    end = time.time()
    
    print(end-start)
    pc.close()
    f.close()
except Exception as e:
    print("can't connect")
    print(e)



