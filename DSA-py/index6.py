#remove duplicate element from a sorted array

nums = [1,1,1,2,3,4,4,7,9,9,9,10]

n = len(nums)
freq_map = {}
for i in range(n):
    freq_map[nums[i]] = 0
j = 0
for k in freq_map:
    nums[j] = k
    j += 1

print(f"Array after removing duplicates: {nums[:j]}")
print(f"Number of unique elements: {j}")


#right rotate array by k places

nums = [3,9,5,6,7,2]

def reverse(nums, left, right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums

reverse(nums, 3, 5)
reverse(nums, 0, 2)
reverse(nums, 0, 5)

print(nums)


