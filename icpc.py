class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([c.lower() for c in s if c.isalpha()])

        left = 0
        right = len(s) - 1

        while True:
            if s[left] != s[right]: return False
            left += 1
            right += 1
            if left > right: return True
