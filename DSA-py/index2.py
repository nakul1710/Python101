#Bubble sort [Adjacent swaps] TC = O(n) SC = O(1)

nums = [2, 1, 4, 7, 6, 3]

def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

sorted_nums = bubble_sort(nums)
print(f"Sorted array is: {sorted_nums}")
