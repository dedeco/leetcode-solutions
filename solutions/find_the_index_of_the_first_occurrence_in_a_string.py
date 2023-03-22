"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.



Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        i = j = 0
        while i < len(haystack):
            if len(needle) > (len(haystack) - i):
                return -1
            if needle[j] == haystack[i]:
                find = False
                while j < len(needle):
                    if needle[j] != haystack[i + j]:
                        find = False
                        break
                    else:
                        find = True
                    j += 1
                if find:
                    return i
            j = 0
            i += 1
        return -1


# driver code
if __name__ == "__main__":
    haystack = "sadbutsad"
    needle = "sad"
    assert Solution().strStr(haystack, needle) == 0

    haystack = "leetcode"
    needle = "leeto"
    assert Solution().strStr(haystack, needle) == -1
