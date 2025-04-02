class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:

        maxArea = 0
        for i in range(len(heights)):
            left, right = i, i
            while left-1 >= 0 and heights[left-1] >= heights[i]:
                left -= 1
            while right+1 < len(heights) and heights[right+1] >= heights[i]:
                right += 1
            maxArea = max(maxArea, (heights[i] * (right-left+1)))
        return maxArea

        # Stack Implementation that I couldn't figure out
        # heights = [7,1,7,2,2,4]
        # go right --> width = [0,4,0,2,1,0]
        # rheights = [4,2,2,7,1,7]
        # go rleft --> width = [0,2,1,0,1,0]
        # go left --> width = [0,1,0,1,2,0]
        # add left and right widths --> [0,4,0,2,1,0]
                                    #   [0,1,0,1,2,0]
                                    #   [1,1,1,1,1,1]
                                    #   [1,6,1,4,4,1]

test = Solution()

heights = [7,1,7,2,2,4]
# Output: 8
print(test.largestRectangleArea(heights))

heights = [1,3,7]
# Output: 7
print(test.largestRectangleArea(heights))

# Time: O(N^2)
# Space: O(1)