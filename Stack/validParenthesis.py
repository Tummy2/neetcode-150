class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        close = {")":"(", "]":"[", "}":"{"}

        for p in s:
            if p in close:
                if len(stack) > 0 and close[p] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)

        return len(stack) == 0
    
test = Solution()

s = "[]"
# Output: true
print(test.isValid(s))

s = "([{}])"
# Output: true
print(test.isValid(s))

# Time: O(N)
# Space: O(N)