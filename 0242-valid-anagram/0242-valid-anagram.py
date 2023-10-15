class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        # hashmap = {}
        # hashmap2 = {}
        # for i in range(len(s)):
        #     if  s[i] not in hashmap:
        #         hashmap[s[i]] = 1
        #     else:
        #         hashmap[s[i]] +=  1
               
        # for j in range(len(t)):
        #     if  t[j] not in hashmap2:
        #         hashmap2[t[j]] = 1
        #     else:
        #         hashmap2[t[j]] +=  1
        # # print(hashmap)        
        # # print(hashmap2)
        # if hashmap == hashmap2:
        #     return True
        # return False             
                  
            
