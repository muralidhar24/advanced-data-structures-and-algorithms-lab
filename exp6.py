"AIM : implement quick sort and merge sort and calculate the execution time for various input sizes(average, worst and best cases)"

import time
import random

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    return time.time() - start_time

sizes = [100, 500, 1000, 5000, 10000]
example_array = [random.randint(1, 100) for _ in range(10)]

print("Example array before sorting:", example_array)
print("Quick Sort result:", quick_sort(example_array))
print("Merge Sort result:", merge_sort(example_array))

for size in sizes:
    random_arr = [random.randint(1, 100000) for _ in range(size)]
    sorted_arr = list(range(size))  # Best case for Quick Sort
    reverse_sorted_arr = list(range(size, 0, -1))  # Worst case for Quick Sort
    
    print(f"\nInput size: {size}")
    print("Quick Sort (Average Case):", measure_time(quick_sort, random_arr[:]))
    print("Quick Sort (Best Case):", measure_time(quick_sort, sorted_arr[:]))
    print("Quick Sort (Worst Case):", measure_time(quick_sort, reverse_sorted_arr[:]))
    print("Merge Sort (Average Case):", measure_time(merge_sort, random_arr[:]))
    print("Merge Sort (Best Case):", measure_time(merge_sort, sorted_arr[:]))
    print("Merge Sort (Worst Case):", measure_time(merge_sort, reverse_sorted_arr[:]))
