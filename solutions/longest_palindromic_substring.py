class Solution:

    def longestPalindrome(self, s: str) -> str:

        def expand_around_center(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        if s is None or len(s) < 1:
            return ""
        start = end = 0
        for i in range(len(s)):
            size1 = expand_around_center(s, i, i)
            size2 = expand_around_center(s, i, i + 1)
            size = max(size1, size2)
            if size > end - start:
                start = i - (size - 1) / 2
                end = i + size / 2
        return s[start: end + 1]
