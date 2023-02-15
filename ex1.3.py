
import matplotlib.pyplot as plt

import time 
def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)
    
times = []
for n in range(36):
    start = time.time()
    result = func(n)
    end = time.time()
    times.append(end - start)

plt.plot(range(36), times)
plt.xlabel("Input size (n)")
plt.ylabel("Time (seconds)")
plt.title("Time complexity of func()")
plt.show()