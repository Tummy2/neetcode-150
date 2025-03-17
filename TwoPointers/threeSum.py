from collections import defaultdict

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        output = []
        seen = set()
        for i in range(len(nums)):
            # Gets the first of 3, then treat as 2 sum after calculating new target
            target = 0 - nums[i]
            curr = []
            d = defaultdict(int)
            for j in range(i+1, len(nums)):
                num = nums[j]
                need = target - num
                if need in d:
                    curr = [nums[i], num, need]
                    # Store in set of seen 3sums for no repeats
                    if frozenset(curr) not in seen:
                        output.append(curr)
                        seen.add(frozenset(curr))
                else:
                    d[num] += 1

        return output

test = Solution()

nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
print(test.threeSum(nums))

nums = [0,1,1]
# Output: []
print(test.threeSum(nums))

# Time: O(N^2)
# Space: O(N)
