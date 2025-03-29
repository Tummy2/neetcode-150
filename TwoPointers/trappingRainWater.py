class Solution:
    def trap(self, height: list[int]) -> int:
        
        res = 0
        l, r = 0, len(height) - 1
        leftMax = height[l]
        rightMax = height[r]

        while (l < r):
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]

        return res
    
test = Solution()

height = [0,2,0,3,1,0,1,3,2,1]
# Output: 9
print(test.trap(height))

# Time: O(N)
# Space: O(1)