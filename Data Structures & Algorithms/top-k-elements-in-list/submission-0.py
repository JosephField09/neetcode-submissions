class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        heap = []
        for c in count.keys():
            heapq.heappush(heap, (count[c], c))
            if len(heap) > k:
                heapq.heappop(heap)
        results = []
        for i in range(k):
            results.append(heapq.heappop(heap)[1])
        return results
        