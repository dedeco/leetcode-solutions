class Solution:

    def reverseVowels(self, s: str) -> str:

        vowels = {
            'a': 0,
            'e': 0,
            'i': 0,
            'o': 0,
            'u': 0,
            'A': 0,
            'E': 0,
            'I': 0,
            'O': 0,
            'U': 0
        }

        low = 0
        high = len(s) - 1

        def replace_s(s, low, high):
            res = s[:low] + s[high] + s[low + 1:high] + s[low] + s[high + 1:]
            return res

        while low < high:
            if s[low] in vowels.keys() and s[high] in vowels.keys():
                s = replace_s(s, low, high)
                low += 1
                high -= 1
            elif s[low] in vowels.keys():
                high -= 1
            elif s[high] in vowels.keys():
                low += 1
            else:
                low += 1
                high -= 1

        return s

# hello
# l.  h


