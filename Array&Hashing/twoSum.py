class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        d = {}
        for i in range(len(nums)):
          num = nums[i]
          need = target - num
          if need in d:
            return [d[need], i]
          else:
            d[num] = i

test = Solution()

nums = [3,4,5,6]
target = 7
# Output: [0,1]
print(test.twoSum(nums, target))

nums = [4,5,6]
target = 10
# Output: [0,2]
print(test.twoSum(nums, target))

# Time: O(N)
# Space: O(N)