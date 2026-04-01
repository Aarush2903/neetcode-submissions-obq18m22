class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        x = {}
        l = 0
        res = 0
        maxf = 0

        for r in range(len(s)):
            x[s[r]] = 1 + x.get(s[r], 0)
            maxf = max(maxf, x[s[r]])

            while (r - l + 1) - maxf > k:
                x[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res 