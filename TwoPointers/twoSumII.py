class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1
        while (left < right):
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -=1

test = Solution()

numbers = [1,2,3,4]
target = 3
# Output: [1,2]

code = test.twoSum(numbers)
print(test.twoSum(code))

# Time: O(N)
# Space: O(1)