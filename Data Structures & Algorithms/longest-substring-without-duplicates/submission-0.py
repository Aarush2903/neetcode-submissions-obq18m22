class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        x = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in x:
                l = max(x[s[r]] + 1, l)
            x[s[r]] = r
            res = max(res, r - l + 1)
        return res
