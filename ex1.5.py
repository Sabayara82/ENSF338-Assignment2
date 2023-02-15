import time
import matplotlib.pyplot as plt

def func1(n, memo={}):
    if n == 0 or n == 1:
        return n
    if n in memo:
        return memo[n]
    else:
        memo[n] = func1(n-1, memo) + func1(n-2, memo)
        return memo[n]
    
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

times1 = []
for n in range(36):
    start = time.time()
    result = func1(n)
    end = time.time()
    times1.append(end - start)

plt.plot(range(36), times, label = "Original Code")
plt.plot(range(36), times1, label = "New Code")
plt.xlabel("Input size (n)")
plt.ylabel("Time (seconds)")
plt.title("Time complexity of func()")
plt.legend()
plt.show()


