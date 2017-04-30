import time
import numpy as np
temp=[-1]*100
lookup=np.array(temp)

def fib(n):
  if n==0: return 0
  elif n==1: return 1
  else:
    return fib(n-1)+fib(n-2)
    
def fib1(n):
      if lookup[n]==-1:
            if n<=1: 
              lookup[n]=n
            else:
              lookup[n]=fib(n-1)+fib(n-2) 
      return lookup[n]


start_time = time.time()

print(fib(40))

print("--- %s seconds f ---" % (time.time() - start_time))


start_time = time.time()

print(fib1(40))

print("--- %s seconds f1---" % (time.time() - start_time))