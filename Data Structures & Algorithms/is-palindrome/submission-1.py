class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_str = "".join(c.lower() for c in s if c.isalnum())
        n = len(s_str)
        left = 0
        right = n - 1
        while left < right:
            if s_str[left] != s_str[right]:
                return False
            left += 1
            right -= 1
        return True