from time import time

from random import randrange

l1 = [randrange(1, 10000000) for i in range(10000)]

l2 = [randrange(1, 10000000) for i in range(100000)]

l3 = [randrange(1, 10000000) for i in range(10000000)]


t1 = time()
l1.sort()
t2 = time()
ti = [t2-t1]

t1 = time()
l2.sort()
t2 = time()
ti.append(t2-t1)

t1 = time()
l3.sort()
t2 = time()
ti.append(t2-t1)


print(ti)