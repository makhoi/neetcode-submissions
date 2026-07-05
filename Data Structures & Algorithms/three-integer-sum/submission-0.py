class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        ans = set()

        for i in range(n):
            left = i + 1
            right = n - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    ans.add(tuple(sorted([nums[i], nums[left], nums[right]])))
                    left += 1
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    right -= 1
        
        return [list(t) for t in ans]