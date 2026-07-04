class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        for letter in s:
            s_map[letter] = s_map.get(letter, 0) + 1

        t_map = {}
        for letter in t:
            t_map[letter] = t_map.get(letter, 0) + 1

        if s_map == t_map:
            return True
        return False