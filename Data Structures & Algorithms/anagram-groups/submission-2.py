class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for s in strs:
            a = [0] * 26
            for l in s:
                a[ord(l) - ord("a")] += 1
            seen[tuple(a)].append(s)
        return list(seen.values())