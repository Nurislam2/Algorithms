def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr



def binary_search(arr, x):
    first = 0
    last = len(arr) - 1
    mid = 0

    while first <= last:
        mid = (last + first) // 2

        if arr[mid] < x:
            first = mid + 1
        elif arr[mid] > x:
            last = mid - 1
        else:
            return mid
    return -1
