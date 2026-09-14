# T: O(n^2), S: o(1)
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         for i in range(len(numbers) - 1):
#             for j in range(i + 1, len(numbers)):
#                 if numbers[i] + numbers[j] == target:
#                     return [i + 1, j + 1]

#         return [-1, -1]

# T: O(nlogn), S: o(1)
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         for i in range(len(numbers)):
#             j = self.search(numbers, target - numbers[i], i + 1)
#             if j != -1:
#                 return [i + 1, j + 1]

#         return [-1, -1]

#     def search(self, numbers: List[int], target: int, left: int) -> int:
#         i, j = left, len(numbers) - 1

#         while i <= j:
#             m = i + (j - i) // 2

#             if numbers[m] == target:
#                 return m
#             elif numbers[m] < target:
#                 i = m + 1
#             elif numbers[m] > target:
#                 j = m - 1
#         return -1

# T: O(n), S: o(1)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -= 1

        return [-1, -1]