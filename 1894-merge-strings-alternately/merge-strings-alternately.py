class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        p1 = 0
        p2 = 0
        commonRange = min(len(word1) , len(word2))
        for i in range(commonRange):
            res = res + word1[i] + word2[i]

        if len(word1) > commonRange:
            for i in range(commonRange , len(word1)):
                res += word1[i]
        if len(word2) > commonRange:
            for i in range(commonRange , len(word2)):
                res += word2[i]
        return res        
