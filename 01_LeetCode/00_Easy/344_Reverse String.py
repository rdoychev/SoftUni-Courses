def reverse_string(s: list):
    # s.reverse()

    idx = len(s) - 1
    for i in range(len(s) // 2):
        s[i], s[idx] = s[idx], s[i]
        idx -= 1
    return s


s1 = ["0"]
s2 = reverse_string(s1)
print(s1)
print(s2)
