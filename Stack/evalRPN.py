class Solution:
    def evalRPN(self, tokens: list[str]) -> int:

        stack = []
        for token in tokens:
            if token == "+":
                first = stack.pop()
                second = stack.pop()
                n = first + second
                stack.append(n)
            elif token == "-":
                first = stack.pop()
                second = stack.pop()
                n = second - first
                stack.append(n)
            elif token == "*":
                first = stack.pop()
                second = stack.pop()
                n = first * second
                stack.append(n)
            elif token == "/":
                first = stack.pop()
                second = stack.pop()
                n = int(second / first)
                stack.append(n)
            else:
                stack.append(int(token))

        return stack[0]
    
test = Solution()

tokens = ["1","2","+","3","*","4","-"]
# Output: 5
# Explanation: ((1 + 2) * 3) - 4 = 5
print(test.evalRPN(tokens))

# Time: O(N)
# Space: O(N)