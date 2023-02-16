import matplotlib.pyplot as plt
import json
import time
import sys
sys.setrecursionlimit(20000)

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    mid = (start + end) // 2
    if array[end] < array[start]:
        array[start], array[end] = array[end], array[start]
    if array[mid] < array[start]:
        array[mid], array[start] = array[start], array[mid]
    if array[end] < array[mid]:
        array[end], array[mid] = array[mid], array[end]
    p = array[mid]

    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

# open testing inputs and create list of timing results
with open("ex2.json") as inf:
    inputs = json.load(inf)

length = []
times = []
for i, arr in enumerate(inputs):
    start = time.time()
    func1(arr, 0, len(arr) - 1)
    end = time.time()
    length.append(len(arr))
    times.append(end - start)

# plot timing of execution as a function of the length of the array
fig = plt.figure()
plt.scatter(length, times)
plt.title("Timing of Improved QuickSort for Arrays of Various Lengths")
plt.xlabel("Length of Array (n)")
plt.ylabel("Time to Execute QuickSort (sec)")
plt.show()