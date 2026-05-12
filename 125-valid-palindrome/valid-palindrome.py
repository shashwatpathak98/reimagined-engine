class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        alnum_string = "".join(ch for ch in s if ch.isalnum()).lower()

        n = len(alnum_string) - 1
        l,r = 0, n
        while l < r:
            if alnum_string[l] == alnum_string[r]:
                l+= 1
                r-= 1
            else:
                return False
        return True            

            
        