class Solution:

    def encode(self, strs: list[str]) -> str:
        
        return "LMFAO".join(strs)

    def decode(self, s: str) -> list[str]:

        return s.split("LMFAO")[0:-1]
    
test = Solution()

Input = ["neet","code","love","you"]
# Output = ["neet","code","love","you"]

code = test.encode(Input)
print(test.decode(code))

# Time: O(N)
# Space: O(N)