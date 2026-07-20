def add_binary(a, b):
    result = int(a, 2) + int(b, 2)
    # print(format(result, 'b'))
    # print(f"{result:b}")
    return format(result, 'b')


str1 = "1010"
str2 = "1011"

print(f"{add_binary(str1, str2)}")
