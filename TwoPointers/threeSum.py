class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        nums.sort()
        output = []
        print(nums)

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i and nums[i] == nums[i-1]:
                continue
            
            target = 0 - a
            left = i + 1
            right = len(nums)-1
            while (left < right):
                print(a, nums[left], nums[right])
                if (nums[left] + nums[right]) < target:
                    left += 1
                elif (nums[left] + nums[right]) > target:  
                    right -= 1
                else:
                    output.append([a, nums[left], nums[right]])
                    left += 1
                    right -= 1
                
                    while left < len(nums) and (nums[left] == nums[left-1]):
                        left += 1

        return output

test = Solution()

nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
print(test.threeSum(nums))

nums = [0,1,1]
# Output: []
print(test.threeSum(nums))

# Time: O(N^2)
# Space: O(N)
