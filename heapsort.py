"""
Heapsort Algorithm in Python

Explanation:
1. Heapify Function: Ensures the heap property is maintained. It compares a node with its children and swaps them if needed to maintain the max-heap property.
2. Heapsort Function:
   - Build a Max-Heap: This is done by calling `heapify` on all non-leaf nodes.
   - Extract Maximum Element: The root of the heap (the maximum element) is swapped with the last element, and `heapify` is called to maintain the heap property for the reduced heap.
3. Sorting: The process is repeated until the heap size is reduced to one.

Time Complexity: O(n log n), making it an efficient sorting algorithm.
"""

def heapify(arr, n, i):
    # Find the largest among root and children
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left = 2*i + 1
    right = 2 * i + 2  # right = 2*i + 2

    # If left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child exists and is greater than the current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the largest is not the root
    if largest != i:
        # Swap the root with the largest
        arr[i], arr[largest] = arr[largest], arr[i]

        # Heapify the root to maintain the max-heap property
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)

    # Build a max heap
    # Start from the last non-leaf node and heapify each node
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one from the heap
    for i in range(n - 1, 0, -1):
        # Move the current root (maximum) to the end
        arr[i], arr[0] = arr[0], arr[i]

        # Call heapify on the reduced heap
        heapify(arr, i, 0)

# Example usage with a larger dataset:
arr = [20, 18, 12, 8, 5, -2, 30, 25, 15, 6, 10, 1, 50, 45, 35]
heapsort(arr)
print("Sorted array is:", arr)

print("--------------------------------------------------------------------------------------")
print("Additional comparison with another larger dataset amoong Heapsort, Quicksort and Mergesort")
print("--------------------------------------------------------------------------------------")
print("")


#--------------------------------------------------------------------------------------------------------

"""
Additional Sorting Algorithms and Empirical Comparison:

1. Quicksort Implementation:
   - Added a simple Quicksort algorithm using the divide-and-conquer approach.
   - Uses a pivot to partition the array into elements less than and greater than the pivot.
   - Recurively sorts the partitions and combines them.

2. Mergesort Implementation:
   - Added a simple Mergesort algorithm, another divide-and-conquer sorting algorithm.
   - Recursively splits the array into halves, sorts them, and merges them back together.

3. Empirical Comparison of Sorting Algorithms:
   - Generates large datasets of varying sizes (1000, 5000, 10000) and different distributions (random, sorted, reverse-sorted).
   - Measures the running times of Heapsort, Quicksort, and Mergesort on these datasets.
   - Collects and displays the results for comparison and analysis.
"""

import random
import time

# Quicksort implementation
def quicksort(arr):
    # Base case: an array with 0 or 1 elements is already sorted
    if len(arr) <= 1:
        return arr
    else:
        # Select pivot (middle element in this case)
        pivot = arr[len(arr) // 2]

        # Partition the array into three parts: less than pivot, equal to pivot, and greater than pivot
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        # Recursively sort left and right parts and combine with the middle part
        return quicksort(left) + middle + quicksort(right)

# Mergesort implementation
def mergesort(arr):
    # Base case: an array with 0 or 1 elements is already sorted
    if len(arr) <= 1:
        return arr

    # Find the midpoint to split the array
    mid = len(arr) // 2

    # Recursively sort the left and right halves
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])

    # Merge the sorted halves
    return merge(left, right)

def merge(left, right):
    result = []  # Merged result array
    i = j = 0  # Pointers for left and right arrays

    # Merge the left and right arrays by comparing elements
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append remaining elements (if any)
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Function to measure the runtime of sorting algorithms
def measure_sorting_time(sort_function, arr):
    start_time = time.time()  # Record start time
    sort_function(arr)  # Run the sorting function
    return time.time() - start_time  # Return the elapsed time

# Generate datasets of different sizes and distributions
sizes = [1000, 5000, 10000]  # Different input sizes for testing
distributions = {
    "random": lambda size: [random.randint(0, 100000) for _ in range(size)],  # Random data
    "sorted": lambda size: sorted([random.randint(0, 100000) for _ in range(size)]),  # Sorted data
    "reverse_sorted": lambda size: sorted([random.randint(0, 100000) for _ in range(size)], reverse=True)  # Reverse sorted data
}

# Perform empirical comparison
results = []

for size in sizes:
    for distribution_name, distribution_func in distributions.items():
        # Generate the dataset based on the distribution function
        arr = distribution_func(size)
        
        # Measure the time for Heapsort
        arr_copy = arr.copy()  # Copy to avoid modifying the original array
        heap_time = measure_sorting_time(lambda x: heapsort(x), arr_copy)
        
        # Measure the time for Quicksort
        arr_copy = arr.copy()  # Copy to avoid modifying the original array
        quick_time = measure_sorting_time(lambda x: quicksort(x), arr_copy)
        
        # Measure the time for Mergesort
        arr_copy = arr.copy()  # Copy to avoid modifying the original array
        merge_time = measure_sorting_time(lambda x: mergesort(x), arr_copy)
        
        # Store the results in a list for later analysis
        results.append({
            "Size": size,
            "Distribution": distribution_name,
            "Heapsort Time (s)": heap_time,
            "Quicksort Time (s)": quick_time,
            "Mergesort Time (s)": merge_time
        })

# Output results
import pandas as pd
df_results = pd.DataFrame(results)  # Convert results to a DataFrame for easy viewing
print(df_results)
