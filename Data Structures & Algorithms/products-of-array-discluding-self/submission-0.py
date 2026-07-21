class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = []
        for i in range(0, len(nums)):
            digits = []
            digits.extend(nums[:i])
            digits.extend(nums[i+1:])
            results.append(math.prod(digits))
        return results