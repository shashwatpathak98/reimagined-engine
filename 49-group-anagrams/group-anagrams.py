class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash_map = {}
        ans = []

        for s in strs:
            key = "".join(sorted(s))
            
            #print(hash_map)
            if(key in hash_map):
                hash_map[key].append(s)
            else:
                hash_map[key] = [s]

        ans += hash_map.values()
        return ans     


        

            
        

             
        