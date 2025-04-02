class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        
        arr = []
        for i in range(len(position)):
            x = (position[i], speed[i])
            arr.append(x)
        arr.sort()
        arr.reverse()
        stack = []
        for i in range(len(arr)):
            x = (target - arr[i][0]) / arr[i][1]
            arr[i] = x
            if not stack:
                stack.append(arr[i])
            if stack and arr[i] > stack[-1]:
                stack.append(arr[i])
            
        return len(stack)
    
test = Solution()

target = 10
position = [1,4]
speed = [3,2]
# Output: 1
print(test.carFleet(target, position, speed))

target = 10
position = [4,1,0,7]
speed = [2,2,1,1]
# Output: 3
print(test.carFleet(target, position, speed))

# Time: O(nlogn)
# Space: O(N)