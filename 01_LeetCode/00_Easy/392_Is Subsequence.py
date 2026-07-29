def is_subsequence(s: str, t: str) -> bool:
    len_s = len(s)
    if len_s == 0:
        return True

    len_t = len(t)
    idx = 0
    found = 0

    for char in s:

        while idx < len_t:
            if char == t[idx]:
                found += 1
                idx += 1
                if found == len_s:
                    return True
                break

            idx += 1

    return False
# i = 0
# j = 0
# while i< len(s) and j <len(t):
#     if s[i] == t[j]:
#         i +=1
#     j += 1
# return i == len(s)

s1 = "aaaaaa"
t1 = "bbaaaa"
print(is_subsequence(s1, t1))
