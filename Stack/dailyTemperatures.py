class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        
        stack = []
        output = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while(stack and temp > stack[-1][0]):
                index = stack.pop()[1]
                output[index] = i - index

            stack.append((temp, i))

        return output
    
test = Solution()

temperatures = [30,38,30,36,35,40,28]
# Output: [1,4,1,2,1,0,0]
print(test.dailyTemperatures(temperatures))

temperatures = [22,21,20]
# Output: [0,0,0]
print(test.dailyTemperatures(temperatures))

# Time: O(N)
# Space: O(N)