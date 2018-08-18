import io
import csv
import psycopg2
import time
# bulk insert
def array_to_str(data):
    f=io.StringIO()
    f.write('\n'.join('\t'.join(str(s) for s in r) for r in data))
    f.seek(0)
    return f
try:
    connection_string = "dbname='assignment1' user='sangjin' host='localhost' password='1234'"

    connection1 = psycopg2.connect(connection_string)
    connection1.autocommit=True
    pc = connection1.cursor()

    f = open("auth.tsv", encoding="utf-8", errors='replace')
    start = time.time()
    
    insert_query = "insert into auth(name,pubid) values (%s, %s)"    
    data = []
    k=0
    for line in csv.reader(f, delimiter='\t'):
        data.insert(k,[str(line[0]),str(line[1])])
        k= k+1
        if(k == 500):
            pc.copy_from(array_to_str(data), 'auth')
            data = []
            k=0
    end = time.time()
    
    print(end-start)
    pc.close()
    f.close()
except Exception as e:
    print("can't connect")
    print(e)



