import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left, right = 1, max(piles)
        ans = right

        while left <= right:
            time = 0
            mid = (left + right) // 2
            for i in range(len(piles)):
                time += math.ceil(piles[i]/mid)

            if time <= h:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans
    
# Time: O(nlogm)
# Space: O(1)