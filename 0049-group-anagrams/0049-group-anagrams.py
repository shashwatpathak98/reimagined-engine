class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = defaultdict(list)
        for string in strs:
            # first we have to sort each element
            key = "".join(sorted(list(string)))
            dictionary[key].append(string)
        arr = list(dictionary.values())
        return arr

 