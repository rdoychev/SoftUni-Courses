def word_pattern(pattern: str, s: str) -> bool:
    hash_map = {}
    s_list = s.split(" ")

    if len(s_list) != len(pattern):
        return False

    for idx in range(len(pattern)):
        if pattern[idx] not in hash_map.keys() and s_list[idx] not in hash_map.values():
            hash_map[pattern[idx]] = s_list[idx]
        elif pattern[idx] in hash_map.keys() and s_list[idx] in hash_map.values():
            if hash_map[pattern[idx]] != s_list[idx]:
                return False
        else:
            return False

    return True


pattern1 = "abba"
s1 = "dog cat cat dog"
print(word_pattern(pattern1, s1))