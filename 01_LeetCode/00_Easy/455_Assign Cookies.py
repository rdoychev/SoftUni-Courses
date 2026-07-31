def find_content_children(g: list, s: list) -> int:
    if len(s) == 0:
        return 0

    g.sort()
    s.sort()
    count = 0
    i = 0
    j = 0

    while i < len(g) and j < len(s):
        if g[i] <= s[j]:
            count += 1
            i += 1
            j += 1
        else:
            j += 1

    return count


g1 =[1, 2, 3]
s1 = [3]
print(find_content_children(g1, s1))