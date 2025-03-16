class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        # function to turn word into dictionary
        def turnDict(word: str):
            d = {}
            for i in range(len(word)):
                if word[i] in d:
                    d[word[i]] += 1
                else:
                    d[word[i]] = 1
            return d

        output = []
        while (len(strs) > 0):
            # obtain the first word, put it into sub array, then convert to dictionary
            word = strs.pop(0)
            sub = [word]
            d = turnDict(word)
            remove = []
            # loop through the rest of the words, turn them into dictionaries and compare dictionaries
            for i in range(len(strs)):
                if d == turnDict(strs[i]):
                    sub.append(strs[i])
                    # keep track of the indexes to pop out of strs after looping through entire thing
                    remove.append(i - len(remove))
            for index in remove:
                strs.pop(index)
            output.append(sub)

        return output

# THE GOOD SOLUTION
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         res = defaultdict(list)
#         for s in strs:
#             sortedS = ''.join(sorted(s))
#             res[sortedS].append(s)
#         return list(res.values())
    
test = Solution()

strs = ["act","pots","tops","cat","stop","hat"]
# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
print(test.groupAnagrams(strs))

strs = ["x"]
# Output: [["x"]]
print(test.groupAnagrams(strs))

# Time: (O(N^2 k))
# Space: (O(N))