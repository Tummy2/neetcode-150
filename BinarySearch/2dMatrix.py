class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # Have a top and bottom pointer, which will be 0 and len(matrix) - 1
        # find the middle row of the matrix and check the first index
        # if that number is less than the target, then binary search that array
        # if the number is not in that array, move the top pointer to be the next row in the matrix

        top, bottom = 0, len(matrix) - 1
        
        while top <= bottom:

            middle = (top + bottom) // 2
            nums = matrix[middle]

            if nums[0] <= target:
                left, right = 0, len(nums)-1
                while left <= right:
                    mid = (left + right) // 2
                    if nums[mid] == target:
                        return True
                    elif nums[mid] > target:
                        right = mid - 1
                    else:
                        left = mid + 1
                top = middle + 1
            else:
                bottom = middle - 1

        return False
    
# Time: O(logmn)
# Space: O(1)