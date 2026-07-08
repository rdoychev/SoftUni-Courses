import timeit
import tracemalloc


def longest_substring_wrc(s: str):
    len_s = len(s)
    check_characters = ""
    max_len = 0
    max_str = ""

    if len_s == 0:
        return 0, max_str

    for idx in range(len_s):
        if s[idx] not in check_characters:
            check_characters += s[idx]
            # max_len = max(max_len, len(check_characters))
            if max_len < len(check_characters):
                max_len = len(check_characters)
                max_str = "".join(check_characters)

        else:
            i = check_characters.index(s[idx])
            check_characters = check_characters[i + 1:] + s[idx]

    return max_len, max_str


s_inp = input()

tracemalloc.start()
t1 = timeit.default_timer()

m_len, m_str = longest_substring_wrc(s_inp)
print(m_str, m_len)

t2 = timeit.default_timer()
print(f"{t2-t1:.8f}")

print(tracemalloc.get_traced_memory())
tracemalloc.stop()
