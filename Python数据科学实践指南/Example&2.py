
import math

import time 

print(time.ctime()) 

for x in range(5):
	print(time.ctime())
	time.sleep(3)


import random
for i in range(5):
	print(random.random())


import random 
random.seed(5)
for i in range(5):
	print(random.random())


import random 
a = []
for x in range(len(a)):
	random.shuffle(a)
	print(a)

for x in range(len(a)):
	random.choice(a)
	print(a)
for x in range(5):
	random.sample(a, 3)	

from glob import glob
file_path = glob("./")
for i in file_path:
	print(i)