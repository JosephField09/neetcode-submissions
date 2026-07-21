class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        freq = [[] for i in range(len(nums) + 1)]
        for num in count.keys():
            freq[count.get(num)].append(num)
        results = []
        for i in range (len(freq)-1, 0, -1):
            for num in freq[i]:
                results.append(num)
                if len(results) == k:
                    return results