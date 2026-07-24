def is_isomorphic(s: str, t: str) -> bool:
    char_map = {}

    for idx in range(len(s)):
        if s[idx] not in char_map.keys() and t[idx] not in char_map.values():
            char_map[s[idx]] = t[idx]
            continue
        elif s[idx] not in char_map.keys() and t[idx] in char_map.values() or \
                s[idx] in char_map.keys() and t[idx] not in char_map.values():
            return False
        else:
            if t[idx] != char_map[s[idx]]:
                print(t[idx], char_map[s[idx]])
                return False

        print(idx, char_map, t[idx], char_map[s[idx]])
    return True


str1 = "paperpl"
str2 = "titletl"
print(is_isomorphic(str1, str2))
