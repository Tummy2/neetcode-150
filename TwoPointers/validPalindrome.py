class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        newS = ""
        for letter in s:
            if letter.isalnum():
                newS += letter.lower()

        left, right = 0, len(newS)-1
        while (left <= right):
            if newS[left] != newS[right]:
                return False
            left += 1
            right -= 1

        return True
    
test = Solution()

s = "Was it a car or a cat I saw?"
# Output: true
print(test.isPalindrome(s))

s = "tab a cat"
# Output: false
print(test.isPalindrome(s))

# Time: O(N)
# Space: O(N)