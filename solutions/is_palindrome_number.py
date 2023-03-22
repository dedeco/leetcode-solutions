class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_number = str(x)
        size = len(str_number)
        i = 0
        while i <= (size // 2):
            if str_number[i] != str_number[size - i - 1]:
                return False
            i += 1
        return True


if __name__ == "__main__":
    x = 121
    assert Solution().isPalindrome(x) == True
