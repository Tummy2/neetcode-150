class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        d = {}
        for letter in s:
            if letter in d:
                d[letter] += 1
            else:
                d[letter] = 1
        
        d2 = {}
        for letter in t:
            if letter in d2:
                d2[letter] += 1
            else:
                d2[letter] = 1
        
        return d == d2
    
test = Solution()

s = "racecar"
t = "carrace"
# Output: true
print(test.isAnagram(s, t))

s = "jar"
t = "jam"
# Output: false
print(test.isAnagram(s, t))

# Time: O(N)
# Space: O(N)
