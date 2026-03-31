
arr = [3,9,8,6,2,1,5,4]
#merge sort     
def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2  
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    result = []

    i, j = 0, 0
    n, m = len(left), len(right)

    # Merge left and right
    while i < n and j < m:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    while i < n:
        result.append(left[i])
        i += 1

    while j < m:
        result.append(right[j])
        j += 1

    return result

sorted_arr = mergeSort(arr)
print(f"Sorted array is: {sorted_arr}")    