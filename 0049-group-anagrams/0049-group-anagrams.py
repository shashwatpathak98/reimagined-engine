class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for string in strs:
            # first we have to sort each element
            key = "".join(sorted(list(string)))
            if(key not in dictionary):
                dictionary[key] = [string]
            else:
                dictionary[key].append(string)
        arr = list(dictionary.values())
        return arr

 