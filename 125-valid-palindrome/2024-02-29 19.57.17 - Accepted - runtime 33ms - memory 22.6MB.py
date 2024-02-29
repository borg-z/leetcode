class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [x.lower() for x in s if x.isalpha() or x.isdigit()]
        return s == s[::-1]