class Solution:
    def _isVowel(self, s:str) -> bool:
        return s in "aeiou"

    def _atLeastK(self, word: str, k :int) -> int:
        start, count, vowels , consonants = 0,0,{},0

        for end , char in enumerate(word):
            if self._isVowel(char):
                vowels[char] = vowels.get(char , 0) + 1
            else:
                consonants += 1

            while len(vowels) == 5 and consonants >= k:
                count += len(word) - end

                if self._isVowel(word[start]):
                    vowels[word[start]] -= 1
                    if vowels[word[start]] == 0:
                        del vowels[word[start]]
                else:
                    consonants -= 1        
                start += 1
        return count                


    def countOfSubstrings(self, word: str, k: int) -> int:
        return self._atLeastK(word , k) - self._atLeastK(word , k+1)



        