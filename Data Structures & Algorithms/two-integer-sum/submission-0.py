class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number_index = {}
        for i in range(len(nums)):
            find = target - nums[i]
            if find in number_index:
                return [number_index[find], i]
            number_index[nums[i]] = i