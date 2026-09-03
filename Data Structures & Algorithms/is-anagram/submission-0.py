class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        str1Map = {}
        str2Map = {}

        for i in range(len(s)):
            if s[i] in str1Map:
                str1Map[s[i]] += 1
            else:
                str1Map[s[i]] = 1

            if t[i] in str2Map:
                str2Map[t[i]] += 1
            else:
                str2Map[t[i]] = 1

        for key in str1Map:
            if key not in str2Map:
                return False
            if str1Map[key] != str2Map[key]:
                return False

        return True