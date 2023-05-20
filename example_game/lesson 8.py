import random
import time

snow = '*'
snap = '+'
while True:
    print(snow *random.randint(5, 15), snap * random.randint(10, 15), snow * random.randint(2, 6)  )
    time.sleep(5)
