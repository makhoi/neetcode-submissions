class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        character_frequency = {}
        res = 0

        for right in range(n):
            character_frequency[s[right]] = character_frequency.get(s[right], 0) + 1
            
            while character_frequency[s[right]] == 2:
                character_frequency[s[left]] -= 1
                if character_frequency[s[left]] == 0:
                    del character_frequency[s[left]]
                left += 1
            
            res = max(res, right - left + 1)
        
        return res
                
