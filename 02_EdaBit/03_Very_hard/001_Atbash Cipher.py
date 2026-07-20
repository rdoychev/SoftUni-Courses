def atbash(txt: str) -> str:
    p1 = 65
    p2 = 90
    p3 = 97
    p4 = 122
    encrypt_str = ""

    for letter in txt:
        code = ord(letter)
        print(letter, code)
        if 65 <= code <= 90:
            encrypt_str += chr(p2 - (code - p1))
        elif 97 <= code <= 122:
            encrypt_str += chr(p4 - (code - p3))
        else:
            encrypt_str += letter

    return encrypt_str


str1 = "Christmas is the 25th of December"
out = atbash(str1)
print(out)
