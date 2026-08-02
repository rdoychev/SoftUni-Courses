def find_lus_length(a: str, b: str) -> int:
    if a == b:
        return -1
    return max(len(a), len(b))
    
    if len(a) < len(b):
        a, b = b, a

    for j in range(len(b)):
        if b[j] in a:
            idx = a.index(b[j])
            a = a[:idx] + a[idx+1:]

    return len(a)


a1 = "abcdefgaa"
b1 = "abc"
print(find_lus_length(a1, b1))
