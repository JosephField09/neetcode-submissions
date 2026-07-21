class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for n in strs:
            a = [0] * 26
            for l in n:
                a[ord(l) - ord("a")] +=1
            group[tuple(a)].append(n)
        return list(group.values())