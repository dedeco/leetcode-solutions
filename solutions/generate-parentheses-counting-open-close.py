"""
22. Generate Parentheses
Medium
16.8K
666
company
Amazon
company
Adobe
company
Microsoft
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]


Constraints:

1 <= n <= 8
"""
from typing import List

import numpy


class Solution:
    def __init__(self):
        self.valid = []

    def generateParenthesis(self, n: int) -> List[str]:
        self.generate(n=n)
        return self.valid

    def generate(self, n: int, arr: List = [], open=0, close=0):
        if open > n or close > n or close > open:
            return
        if len(arr) == 2*n and open==close:
            self.valid.append(''.join(arr[:]))
            return
        arr.append('(')
        self.generate(n, arr, open +1, close)
        arr.pop()
        arr.append(')')
        self.generate(n, arr, open, close +1 )
        arr.pop()


# driver code
if __name__ == "__main__":
    result = Solution().generateParenthesis(3)
    numpy.testing.assert_array_equal(
        result,
        ['((()))', '(()())', '(())()', '()(())', '()()()']
    )
