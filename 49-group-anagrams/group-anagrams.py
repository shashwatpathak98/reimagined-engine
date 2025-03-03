class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map= {}
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in hash_map:
                hash_map[sorted_s].append(s)
            else:
                hash_map[sorted_s] = [s]
        return list(hash_map.values())            
        