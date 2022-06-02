# coding: utf-8


# Libraries to add a random number generator to implement hash generator
import time
import hashlib
import random

# Arbitrary string we are hashing.
a_string = 'poly'

# Below for-loop creates 15 data values for randomly generated hashed numbers/chars
for i in range(15):
    n = random.random()
    hashed_string = hashlib.sha256(a_string.encode('utf-8')).hexdigest()+f"{n}"
    hashed_string = hashlib.sha256(hashed_string.encode('utf-8')).hexdigest()
    
    print(hashed_string[-5:-1])
    time.sleep(6)