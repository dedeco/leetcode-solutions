class Solution:

    def longestPalindrome(self, s: str) -> str:

        bigstr = ""

        def runner(sub, start):
            nonlocal bigstr
            joined = ''.join(sub)
            if joined in s:
                if is_palindrome(sub):
                    if len(joined) > len(bigstr):
                        bigstr = joined
            else:
                return
            if len(sub) // 2 == len(s):
                return
            for i in range(start, len(s)):
                sub.append(s[i])
                runner(sub, i + 1)
                sub.pop()

        def is_palindrome(ss):
            i = 0
            if not ss:
                return False
            while i < (len(ss) // 2):
                if not ss[i] == ss[len(ss) - 1 - i]:
                    return False
                i += 1
            return True

        runner([], 0)
        return bigstr


if __name__ == "__main__":
    result = Solution().longestPalindrome("babad")
    print(result)
    assert "bab" == result


