from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            sortedStr = "".join(sorted(s))
            result[sortedStr].append(s)

        return list(result.values())