
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Middle element as pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# Example usage
    data = [6, 3, 9, 5, 2, 8]
    print("Original array:", data)
    sorted_data = quick_sort(data)
    print("Sorted array:", sorted_data)
