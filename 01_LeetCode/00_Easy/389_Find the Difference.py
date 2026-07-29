def find_the_difference(s: str, t: str) -> str:
    char_map = ""
    for char in t:
        if char not in char_map:
            char_map += char
            count1 = s.count(char)
            count2 = t.count(char)
            if count1 != count2:
                return char



s1 = "a"
t1 = "aa"
print(find_the_difference(s1, t1))
