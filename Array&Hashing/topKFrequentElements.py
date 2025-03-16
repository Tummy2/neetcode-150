from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        d = defaultdict(int)
        for i in range(len(nums)):
            d[nums[i]] += 1

        output = []
        for i in range(k):
            num = max(d, key=d.get)
            output.append(num)
            del d[num]

        return output

test = Solution()

nums = [1,2,2,3,3,3]
k = 2
# Output: [2,3]
print(test.topKFrequent(nums, k))

nums = [7,7]
k = 1
# Output: [7]

print(test.topKFrequent(nums, k))

# Time: O(N)
# Space: O(N)
