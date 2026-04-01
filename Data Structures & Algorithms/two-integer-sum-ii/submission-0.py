class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        indices = defaultdict(int)

        for i in range(len(numbers)):
            tmp = target - numbers[i]
            if indices[tmp]:
                return [indices[tmp], i+1]
            indices[numbers[i]] = i+1

        return []