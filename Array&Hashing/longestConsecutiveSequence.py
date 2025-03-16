class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        
        s = set(nums)
        s = list(s)
        s.sort()
        curr = []
        longest = 0
        for num in s:
            if (num - 1 in curr) or (curr == []):
                curr.append(num)
            else:
                curr = []
                curr.append(num)
            longest = max(longest, len(curr))

        return longest
    
test = Solution()

nums = [2,20,4,10,3,4,5]
# Output: 4
print(test.longestConsecutive(nums))

nums = [0,3,2,5,4,6,1,1]
# Output: 7
print(test.longestConsecutive(nums))

# Time: O(N)
# Space: O(N)
