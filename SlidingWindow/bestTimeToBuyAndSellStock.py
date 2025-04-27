class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # have a left and right pointer that start at index 0 and 1
        # while the right is greater than the left, keep track of max profit
        # set left to right if the profit is ever negative

        left, right = 0, 1
        profit = 0

        while left < right and right < len(prices):
            buy = prices[left]
            sell = prices[right]

            if sell > buy:
                profit = max(profit, sell - buy)
            else:
                left = right
            right += 1

        return profit
    
# Time: O(n)
# Space: O(1)