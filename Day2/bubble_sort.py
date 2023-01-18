import time
def mili():
        return int(round(time.time() * 1000))

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr




arr = [23, 28, 1, 83, 9, 82, 12, 90, 89, 23, 76, 11]

start_time = mili()
print(bubble_sort(arr))
print(mili() - start_time)


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



