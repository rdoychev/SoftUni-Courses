def valid_palindrome(s: str) -> bool:
    str_len = len(s)
    if str_len == 1:
        return True

    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return s[i:j] == s[i:j][::-1] or s[i+1:j+1] == s[i+1:j+1][::-1]

    return True


s1 = "eceec"
print(valid_palindrome(s1))

print(len(s1))
