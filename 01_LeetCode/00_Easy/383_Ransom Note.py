def can_construct(ransomNote: str, magazine: str) -> bool:
    if len(ransomNote) > len(magazine):
        return False

    count_letters = []
    for char in ransomNote:
        if char not in count_letters:
            count_letters.append(char)
            if char not in magazine:
                return False
            else:
                count1 = ransomNote.count(char)
                count2 = magazine.count(char)
                if count1 > count2:
                    return False

    return True


ransom_note1 = "aa"
magazine1 = "aab"
print(can_construct(ransom_note1, magazine1))
