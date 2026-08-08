def count_binary_substrings(s: str) -> int:
    # if len(s) == 1:
    #     return 0
    #
    # count0 = 0
    # count1= 0
    # prev = s[0]
    # tmp = 0
    # switch = 0
    # for char in s:
    #     if char != prev:
    #         if char == "0":
    #             switch += min(tmp ,count1)
    #             tmp = count1
    #             count1 = 0
    #         else:
    #             switch += min(tmp, count0)
    #             tmp = count0
    #             count0 = 0
    #
    #     if  char == "0":
    #         count0 += 1
    #     elif char == "1":
    #         count1 += 1
    #     prev = char
    #
    # if char == "1":
    #     switch += min(tmp, count1)
    # else:
    #     switch += min(tmp, count0)
    #
    # return switch

    if len(s) == 1:
        return 0

    switch, prev, curr = 0, 0, 1

    for i in range(1, len(s)):
        if s[i - 1] != s[i]:
            switch += min(prev, curr)
            prev, curr = curr, 1
        else:
            curr += 1

    switch += min(prev, curr)
    return switch


s1 = "01000111"
print(count_binary_substrings(s1))
