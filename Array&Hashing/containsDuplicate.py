class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:

        d = {}
        for i in range(len(nums)):
            if nums[i] in d and d[nums[i]] != i:
                return True
            d[nums[i]] = i
        return False

test = Solution()

Input = [1, 2, 3, 3]
# Output: true
print(test.hasDuplicate(Input))

Input = [1, 2, 3, 4]
# Output: false
print(test.hasDuplicate(Input))