class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # Floyds Algorithm
        # when the fast and slow pointer first meet, that is the start of the cycle
        # have another slow pointer start at the beginning of the list
        # iterate both slow pointers, when they first meet, that is the duplicate number
        
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

# Time: O(N)
# Space: O(1)