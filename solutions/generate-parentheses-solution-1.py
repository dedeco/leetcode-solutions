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
        self.output = {}
        self.valid = {}

    def generateParenthesis(self, n: int) -> List[str]:
        par = []
        for _ in range(n):
            par.append('(')
            par.append(')')

        self.permutate(par, 0)

        result = [''.join(i) for i in self.output.values()]
        return result

    def swap(self, arr: List, i: int, j: int):
        arr[i], arr[j] = arr[j], arr[i]

    def permutate(self, arr: List, i: int):
        if tuple(arr) not in self.valid.keys():
            is_valid = self.is_balanced(arr)
            self.valid[tuple(arr)] = is_valid
            if not is_valid:
                return
        else:
            if not self.valid[tuple(arr)]:
                return
        if i == len(arr):
            self.output[tuple(arr)] = arr.copy()
        for j in range(i, len(arr)):
            self.swap(arr, i, j)
            self.permutate(arr, i + 1)
            self.swap(arr, i, j)

    def is_balanced(self, arr: List):
        d = {'(': ')'}
        q = []
        for i in range(len(arr)):
            if d.get(arr[i]):
                q.append(d[arr[i]])
            elif arr[i] not in d.keys():
                if not q:
                    return False
                item = q.pop(0)
                if item != arr[i]:
                    return False
        if len(q) > 0:
            return False
        return True


# driver code
if __name__ == "__main__":
    result = Solution().generateParenthesis(3)
    numpy.testing.assert_array_equal(
        result,
        ["()()()", "()(())", "(())()", "(()())", "((()))"]
    )
