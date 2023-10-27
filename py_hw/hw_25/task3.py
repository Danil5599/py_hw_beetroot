def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def partition(arr, low, high):
    i = low-1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quicksort(arr, low, high, limit):
    if len(arr) == 1:
        return arr
    if low < high:
        if high-low <= limit:
            insertion_sort(arr)
        else:
            pi = partition(arr, low, high)
            quicksort(arr, low, pi-1, limit)
            quicksort(arr, pi+1, high, limit)

import random

arr = [random.randint(1, 100) for i in range(20)]
print("Original Array:", arr)
quicksort(arr, 0, len(arr)-1, 10)
print("Sorted array:", arr)