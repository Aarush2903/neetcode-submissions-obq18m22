class Solution:
    def isPalindrome(self, s: str) -> bool:
        pstr = ''
        for c in s:
            if c.isalnum():
                pstr += c.lower()
        
        return pstr == pstr[::-1]