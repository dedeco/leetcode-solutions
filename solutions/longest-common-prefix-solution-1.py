"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""
from typing import List


class Solution:

    def runner(self, word: str, i: int) -> str:
        return word[:i]

    def all_equals(self, prefixs: List[str]) -> bool:
        st = prefixs[0]
        for i in range(1, len(prefixs)):
            if st == prefixs[i]:
                continue
            else:
                return False
        return True

    def longestCommonPrefix(self, strs: List[str]) -> str:
        stop = False
        qty_words = len(strs)
        if qty_words <= 1:
            return strs[0]
        i = 1
        while not stop:
            prefixs = list(map(lambda f: self.runner(f, i), strs))
            if not self.all_equals(prefixs):
                return strs[0][:i - 1]
            i += 1
            if i == 1000:
                stop = True
        return strs[0]
