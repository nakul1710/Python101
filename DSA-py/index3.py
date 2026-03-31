#Insertion Sort 

nums = [2,9,3,1,4,5]

def insertion_sort(nums):
    n = len(nums)
    for i in range(1, n):
        key = nums[i]
        j = i - 1 
        while j >= 0 and nums[j] > key:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key
    return nums


sorted_arr = insertion_sort(nums)
print(f"Sorted array is: {sorted_arr}")    