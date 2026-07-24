def is_palindrome(s) -> bool:
    s = s.lower()
    # ss = ""
    #
    # for char in s:
    #     if char.isalnum():
    #         ss += char
    #
    # if ss == ss[::-1]:
    #     return True
    # return False
    left = 0
    right = len(s) - 1

    while left < right:
        if not s[left].isalnum():
            left += 1
            continue
        if not s[right].isalnum():
            right -= 1
            continue
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


s1 = ""
print(is_palindrome(s1))