class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        res = -1
        for i in range(n):
            for j in range(i+1, n):
                area = (min(height[i], height[j])*(j-i))
                res = max(res, area)
        return res