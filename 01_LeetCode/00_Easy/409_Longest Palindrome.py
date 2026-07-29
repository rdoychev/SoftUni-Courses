def longest_palindrome(s: str) -> int:
    # count_chars = {}
    #
    # if len(s) == 1:
    #     return 1
    # else:
    #     n = len(s) // 2
    #     for idx in range(n):
    #         idx1 = len(s) - 1 - idx
    #
    #         if idx1 in count_chars:
    #             count_chars[idx1] += 1
    #         if s[idx] not in count_chars:
    #            count_chars[s[idx]] = 1
    #         else:
    #            count_chars[s[idx]] += 1
    #         if s[idx1] not in count_chars:
    #             count_chars[s[idx1]] = 1
    #         else:
    #             count_chars[s[idx1]] += 1
    #
    #     if len(s) % 2 != 0:
    #         idx += 1
    #
    #         if s[idx] not in count_chars:
    #             count_chars[s[idx]] = 1
    #         else:
    #             count_chars[s[idx]] += 1
    #
    # is_odd = False
    # longest = 0
    # for count in count_chars.values():
    #     if count % 2 == 0:
    #         longest += count
    #     else:
    #         longest += (count // 2) * 2
    #         is_odd = True
    # if is_odd:
    #     longest += 1
    # print(count_chars)
    # return longest

    from collections import Counter

    longest = 0
    if len(s) == 1:
        return 1
    else:
        count_chars = Counter(s)

        is_odd = False
        for value in count_chars.values():
            if value % 2 == 0:
                longest += value
            else:
                longest += value - 1
                is_odd = True
        if is_odd:
            longest += 1

    return longest


s1 = "abccccdd"
print(longest_palindrome(s1))