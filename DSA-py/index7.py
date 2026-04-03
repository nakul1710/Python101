#3sum
class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n):
            # skip duplicates 
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    # skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1
                else:   
                    right -= 1

        return res



#Binary search for iterative
class Solution(object):
    def binarySearch(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid  # element found

            elif nums[mid] < target:
                left = mid + 1  # search right half

            else:
                right = mid - 1  # search left half

        return -1  # element not found

#Binary search for recursive
class Solution(object):
    def binarySearch(self, nums, left, right, target):
        if left > right:
            return -1  # base case: not found

        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            return self.binarySearch(nums, mid + 1, right, target)

        else:
            return self.binarySearch(nums, left, mid - 1, target)
