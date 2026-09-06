# from collections import defaultdict
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         result = defaultdict(list)

#         for s in strs:
#             sortedStr = "".join(sorted(s))
#             result[sortedStr].append(s)

#         return list(result.values())

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            charArr = [0] * 26

            for char in s:
                idx = ord(char) - ord('a')
                charArr[idx] += 1
            result[tuple(charArr)].append(s)

        return list(result.values())