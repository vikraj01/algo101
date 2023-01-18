def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


arr = [23, 28, 1, 83, 9, 82, 12, 90, 89, 23, 76, 11]
print(bubble_sort(arr))

# 5 1 4 2 8
