import time
from line_profiler import LineProfiler

from randomArray import createRandomArray
# arr = [23, 28, 1, 83, 9, 82, 12, 90, 89, 23, 76, 11]
temp = createRandomArray(1000, 1, 10000)
arr = temp
arr_result = []


# pass 1
# 23, 28, 1, 83, 9, 82, 12, 90, 89, 23, 76, 11
# 23, 28, 1, 83, 9, 82, 12, 90, 89, 23, 76, 11
# 23, 28, 1, 83, 9, 82, 12, 90, 89, 23, 76, 11
    # 1 -> to new list
    # latest version of old list: 23, 28, 83, 9, 82, 12, 90, 89, 23, 76, 11

# First approach to sort the arr list
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Create an instance of the LineProfiler
lp1 = LineProfiler()

# Add the function to be profiled
lp1.add_function(bubble_sort)

# Run the profiler
lp1.run('bubble_sort(arr)')

# Print the results
lp1.print_stats()



# 23 12 2 9 1


# arr = [23, 28, 1, 83, 9, 82, 12, 90, 89, 23, 76, 11]
arr = temp
def unbubble_sort(arr):
    while len(arr):
        for i in arr:
            indx = arr.index(i)
            min = i
            for t in arr:
                indx_t = arr.index(t)
                if min > arr[indx_t]:
                    min = t
            arr_result.append(arr.pop(arr.index(min))) 
    arr = arr_result
    return arr


# Create an instance of the LineProfiler
lp = LineProfiler()      

# Add the function to be profiled
lp.add_function(unbubble_sort)

# Run the profiler
lp.run('unbubble_sort(arr)')

# Print the results
lp.print_stats()

# Explanation:
# 2 23 12 1 9



# Pass 1
# 2 23 12 1 9
# 2 12 23 1 9
# 2 12 1 23 9
# 2 12 1 9 23

# Pass 2
# 2 12 1 9 23
# 2 1 12 9 23
# 2 1 9 12 23

# Pass 3
# 1 2 9 12 23
# 1 2 9 12 23

# Pass 4
# 1 2 9 12 23



