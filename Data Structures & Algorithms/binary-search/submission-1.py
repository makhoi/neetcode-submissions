class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1

        while left < right:
            mid = left + (right - left) // 2

            if target <= nums[mid]:
                right = mid
            else:
                left = mid + 1

        return left if nums[left] == target else -1