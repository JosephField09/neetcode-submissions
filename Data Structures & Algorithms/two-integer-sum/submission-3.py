class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in h.keys():
                return sorted([i, h[difference]])
            else:
                h[nums[i]] = i