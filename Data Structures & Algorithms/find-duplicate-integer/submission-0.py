class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        checked = set()
        for n in nums:
            if n in checked:
                return n
            checked.add(n)