"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            "{": "}",
            "(": ")",
            "[": "]"
        }
        i = 0
        stack = []
        while i < len(s):
            if s[i] in d.keys():
                stack.append(d.get(s[i]))
            else:
                item = None
                if stack:
                    item = stack.pop()
                if not item == s[i]:
                    return False
            i += 1
        if not stack:
            return True
        else:
            return False
