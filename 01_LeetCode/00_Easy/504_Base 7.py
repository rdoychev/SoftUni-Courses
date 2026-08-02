def convert_to_base7(num: int) -> int:
    is_negative = False
    if num == 0:
        return "0"
    elif num < 0:
        is_negative = True

    num_str = ""

    num = abs(num)
    print(num, num_str)
    while num > 0:
        x = num % 7
        num = num // 7
        num_str += str(x)
        print(x, num,num_str)

    if is_negative:
        num_str += "-"
    return num_str[::-1]


num1 = -7
print(convert_to_base7(num1))