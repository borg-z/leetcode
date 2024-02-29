class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_l = len(needle)
        haystack_l = len(haystack)
        if needle == haystack:
            return 0

        for i in range(0,haystack_l):
            part = haystack[i:i+needle_l]
            print(part)
            if part == needle:
                return i
        return -1