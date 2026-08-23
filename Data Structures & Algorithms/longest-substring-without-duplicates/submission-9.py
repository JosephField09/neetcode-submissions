class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        contains = set()
        l, res = 0, 0
        for right in range(len(s)):
            while s[right] in contains:
                contains.remove(s[l])
                l += 1
            contains.add(s[right])
            res = max(res, right-l+1)
        return res
