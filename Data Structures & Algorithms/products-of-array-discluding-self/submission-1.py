# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         output = []

#         for i, num in enumerate(nums):
#             j = 0
#             product = 1
#             while j < len(nums):
#                 if j == i:
#                     j += 1
#                     continue
#                 product *= nums[j]
#                 j += 1
#             output.append(product)
#         return output

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_count = 1, 0

        for num in nums:
            if num:
                prod *= num
            else:
                zero_count += 1

        if zero_count > 1:
            return [0] * len(nums)

        res = [0] * len(nums)
        for i, num in enumerate(nums):
            if zero_count:
                res[i] = 0 if num else prod
            else:
                res[i] = prod // num

        return res