def first_uniq_char(s: str) -> int:
    characters = {}

    for char in s:
        characters[char] = characters.get(char, 0) + 1

    for i, char in enumerate(s):
        if characters[char] == 1:
            return i

    return -1


s1 = "loveleetcode"
print(first_uniq_char(s1))