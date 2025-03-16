class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
         
        d = {}
        for i in range(len(nums)):
            if nums[i] in d and d[nums[i]] != i:
                return True
            d[nums[i]] = i
        return False
    
Input1 = [1, 2, 3, 3]
# Output: true
Input2 = [1, 2, 3, 4]
# Output: false

test = Solution()
print(test.hasDuplicate(Input1))
print(test.hasDuplicate(Input2))