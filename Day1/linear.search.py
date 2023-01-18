from randomArray import createRandomArray,mili

arr = [32, 2, 29, 34, 19, 8, 12, 20, 10, 20, 44, 1, 14]
# O(n)


# 1 2 8 10 12 14 19 20
# 0 1 2 3  4  5  6   7
# key =  



bigArray = createRandomArray(18, 1, 1000)

# searching 


def linear_search(key, A):
    x = -1
    for i in range(0, len(arr)):
        if key == A[i]:
            x = i
    return x


# O(log n)
def binary_search(A, low, high, key):
    while (low <= high):
        mid = (low + high) // 2
        if A[mid] == key:
            return mid
        elif A[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    return -1

print(bigArray)

start = mili()
print(linear_search(int(input()),bigArray))
print("Linear search : ",mili() - start)


sorted_start= mili()
sorted_arr = sorted(bigArray)
print("Time for sorting: ",mili() - sorted_start)

start = mili()
print(binary_search(sorted_arr,0,len(bigArray),int(input())))
print("Binary Search : ", mili() - start)