def license_key_formatting(s, k) -> str:
    """
    :type s: str
    :type k: int
    :rtype: str
    """

    s = s.replace("-", "").upper()
    len_s = len(s)
    if k >= len_s:
        return s
    first_group = len_s % k
    num_groups = len_s // k

    if first_group == 0:
        new_s = ""
    else:
        new_s = s[:first_group] + "-"

    for i in range(1, num_groups + 1):
        last_group = first_group + k

        if i != num_groups:
            new_s += s[first_group: last_group] + "-"
        else:
            new_s += s[first_group: last_group]

        first_group = last_group
    return new_s


s1 = "5F3Z-2e-9-wk"
k1 = 1
print(license_key_formatting(s1, k1))