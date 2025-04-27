class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # use map to keep track of letters and index
        # set left = 0
        # iterate through s, where the iteration is your right pointer
        # update longest after every iteration
        # if you run into a repeating character update the left pointer
        # use max because left might already been moved past that repeating character
        # ex "abba", left=2 because of b, without max, left=1 because of last a

        if s == "":
            return 0
        if len(s) == 1:
            return 1

        mp = {}
        l = 0
        longest = 0
        
        for r in range(len(s)):
            char = s[r]
            if char in mp:
                l = max(l, mp[char]+1)
            longest = max(longest, r-l+1)
            mp[char] = r

        return longest
    
# Time: O(n)
# Space: O(n)