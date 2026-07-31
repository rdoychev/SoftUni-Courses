def repeated_substring_pattern(s: str) -> bool:
    if len(s) <= 1:
        return False

    possible_peaces = len(s) // 2
    s_len =len(s)
    for peace in range(possible_peaces , 0, -1):

        if s_len % peace == 0:
            n = int(s_len / peace)
            if s == s[:peace] * n:
                return True

    return False

# return s in (s+s)[1:-1]

s1 = "abcabcabcabc"
print(repeated_substring_pattern(s1))
print(s1 + s1)
print((s1 + s1)[1:-1])
print(s1 in (s1+s1)[1:-1])