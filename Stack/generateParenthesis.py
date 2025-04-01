class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        
        stack = []
        output = []

        def backtrack(nOpen, nClose):
            if n == nOpen == nClose:
                output.append("".join(stack))
                return

            if nOpen < n:
                stack.append("(")
                backtrack(nOpen+1, nClose)
                stack.pop()

            if nClose < nOpen:
                stack.append(")")
                backtrack(nOpen, nClose+1)
                stack.pop()

        backtrack(0,0)
        return output
    
test = Solution()

n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

print(test.generateParenthesis(n))

# Time: O((4^N / sqrt(N)) * N)
# Space: O(N)