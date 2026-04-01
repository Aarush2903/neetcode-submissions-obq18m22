class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ar = set()
        for num in nums:
            if num in ar:
                return True
            ar.add(num)
        return False
        