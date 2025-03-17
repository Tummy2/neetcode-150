class Solution:
    def maxArea(self, heights: list[int]) -> int:
        left, right = 0, len(heights) - 1
        m = 0
        while (left < right):
            # Get the volume of current height and width
            h = min(heights[left], heights[right])
            w = right - left
            a = h * w
            m = max(m, a)

            # Shift the lower height over
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return m

test = Solution()

height = [1,7,2,5,4,7,3,6]
# Output: 36
print(test.maxArea(height))

height = [2,2,2]
# Output: 4
print(test.maxArea(height))

# Time: O(N)
# Space: O(1)
