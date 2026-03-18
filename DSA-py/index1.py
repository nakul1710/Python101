#Selection sort TC = O(N^2)  SC = O(1)

nums = [5,3,7,2,1]

def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums

sorted_nums = selection_sort(nums)
print("Sorted list:", sorted_nums)


