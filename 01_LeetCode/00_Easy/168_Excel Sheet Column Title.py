def convert_to_title(columnNumber) -> str:
    column_title = ""
    while columnNumber > 0:
        columnNumber -= 1

        column_title += chr(columnNumber % 26 + ord("A"))
        columnNumber //= 26

    return column_title[::-1]


column_number = 703
print(convert_to_title(column_number))