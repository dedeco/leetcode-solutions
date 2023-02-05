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

    def generate(self, n: int, arr: List = []):
        if len(arr) == n * 2:
            if self.is_balanced(arr):
                self.valid.append(''.join(
                    arr.copy()
                )
                )
            return
        else:
            arr.append('(')
            self.generate(n, arr)
            arr.pop()
            arr.append(')')
            self.generate(n, arr)
            arr.pop()

    def is_balanced(self, arr: List):
        q = []
        for i in range(len(arr)):
            if arr[i] == '(':
                q.append(')')
            elif not q:
                return False
            else:
                item = q.pop(0)
                if item != ')':
                    return False
        if len(q) > 0:
            return False
        return True


# driver code
if __name__ == "__main__":
    result = Solution().generateParenthesis(3)
    numpy.testing.assert_array_equal(
        result,
        ['((()))', '(()())', '(())()', '()(())', '()()()']
    )
