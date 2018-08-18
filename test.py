import string
import random
 
def Random_String(size=6, chars=string.ascii_lowercase):
    return "".join(random.choice(chars) for x in range(size))

for x in range(10):
    print(Random_String() +"\n")

