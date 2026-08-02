def reverse_str(s: str, k: int) -> str:
    k2 = k * 2
    n = len(s) // k2

    start = 0
    mid = k
    end = k2

    for i in range(0, n + 1):
        s = s[:start] + s[start:mid][::-1] + s[mid:]
        start = end
        mid = start + k
        end = start + k2

    return s


s1 = "abcdefghjk"
k1 = 3
print(reverse_str(s1, k1))
