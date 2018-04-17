import threading
import time
import sys

ITER = 50000000

def count(n):
    while n > 0:
        n -= 1


a = time.time()
# count(ITER)
# count(ITER)
print('Chained time: ', time.time() - a)


t1 = threading.Thread(target=count,args=(ITER,), daemon=True)
t2 = threading.Thread(target=count,args=(ITER,), daemon=True)
a = time.time()
t1.start()
t2.start()
print('Thread time: ', time.time() - a)

sys.exit()
