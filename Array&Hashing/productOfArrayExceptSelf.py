class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        left, right = 1, 1
        output = [1] * len(nums)
        for i in range(len(nums)):
            output[i] *= left
            left *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            output[i] *= right
            right *= nums[i]

        return output
    
test = Solution()

nums = [1,2,4,6]
# Output: [48,24,12,8]
print(test.productExceptSelf(nums))

nums = [-1,0,1,2,3]
# Output: [0,-6,0,0,0]
print(test.productExceptSelf(nums))

# Time: O(N)
# Space: O(N)
