class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsMap = {};

        for num in nums:
            if num in numsMap:
                numsMap[num] += 1
            else:
                numsMap[num] = 1

        for key, value in numsMap.items():
            if value > 1:
                return True

        return False