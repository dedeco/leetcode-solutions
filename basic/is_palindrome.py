def is_palindrome(ss):
    i = 0
    while i < (len(ss) // 2):
        if not ss[i] == ss[len(ss) - 1 - i]:
            return False
        i += 1
    return True


if __name__ == "__main__":
    print(is_palindrome("hanah"))
