class Solution:

    def encode(self, strs: list[str]) -> str:
        
        return "LMFAO".join(strs)

    def decode(self, s: str) -> list[str]:

        return s.split("LMFAO")[0:-1]
    
# THE GOOD SOLUTION
# class Solution:
    
#     def encode(self, strs: List[str]) -> str:
#         res = ""
#         for s in strs:
#             res += str(len(s)) + "#" + s
#         return res

#     def decode(self, s: str) -> List[str]:
#         res = []
#         i = 0
        
#         while i < len(s):
#             j = i
#             while s[j] != '#':
#                 j += 1
#             length = int(s[i:j])
#             i = j + 1
#             j = i + length
#             res.append(s[i:j])
#             i = j
            
#         return res
    
test = Solution()

Input = ["neet","code","love","you"]
# Output = ["neet","code","love","you"]

code = test.encode(Input)
print(test.decode(code))

# Time: O(N)
# Space: O(N)