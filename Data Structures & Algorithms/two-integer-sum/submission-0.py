class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            print(diff)
            if diff in map:
                return [map[diff], i]
            else:
                map[nums[i]] = i

        return [-1, -1]