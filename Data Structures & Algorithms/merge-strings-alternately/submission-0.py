class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l, r = 0, 0
        result = []
        while l < len(word1) and r < len(word2):
            result.append(word1[l])
            result.append(word2[r])
            l += 1
            r += 1
        result.append(word1[l:])
        result.append(word2[r:])
        return "".join(result)
