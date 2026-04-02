#remove duplicate element from a sorted array

nums = [1,1,1,2,3,4,4,7,9,9,9,11]

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

#Rotate matrix by 90 degree

class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)

        # Step 1: Transpose
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for row in matrix:
            row.reverse()


#matrix in spiral order
class Solution(object):
    def spiralOrder(self, matrix):
        res = []
        
        if not matrix:
            return res
        
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            
            # left → right
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            
            # top → bottom
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            
            if top <= bottom:
                # right → left
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1
            
            if left <= right:
                # bottom → top
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
        
        return res


        