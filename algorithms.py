def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def binary_search(arr, x):
    N = len(arr)
    ResultOk = False
    First = 0
    Last = N - 1
    Pos = -1

    while First <= Last:
        Middle = (First + Last) // 2
        if arr[Middle] == x:
            First=Middle
            Last=First
            Pos = Middle
            ResultOk = True
            break
        elif arr[Middle] < x:
            First = Middle + 1
        else:
            Last = Middle - 1

    if ResultOk:
        print("Элемент найден")
        return Pos
    else:
        print("Элемент не найден")
        return -1