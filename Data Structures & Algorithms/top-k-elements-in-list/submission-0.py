class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        number_frequency = {}
        for num in nums:
            number_frequency[num] = number_frequency.get(num, 0) + 1

        res = []
        while k > 0:
            max_number = max(number_frequency, key=number_frequency.get)
            res.append(max_number)
            del number_frequency[max_number]
            k -= 1

        return res