class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        area = 0
        while l < r:
            width = r - l
            tmp = 0
            if heights[r] <= heights[l]:
                tmp = width * heights[r]
                r -= 1
            else:
                tmp = width * heights [l]
                l += 1
            if tmp > area:
                area = tmp
        return area