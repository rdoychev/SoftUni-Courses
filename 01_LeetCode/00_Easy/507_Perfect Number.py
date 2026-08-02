def check_perfect_number(num: int) -> bool:
    if num == 1:
        return False

    n = int(num ** 0.5)
    num_div_sum = 1
    for i in range(2, n + 1):
        if num % i == 0:
            num_div_sum += i + num // i

    return num_div_sum == num

num1 = 28
print(check_perfect_number(num1))