def title_to_number(column_title: str) -> int:
    shift = 64
    column_number = 0
    column_title = column_title[::-1]

    for idx, char in enumerate(column_title, 0):
        column_number += (ord(char) - shift) * 26 ** idx

    return column_number


column_title1 = "ZZ"
print(title_to_number(column_title1))
