def is_power_of_two(n: int) -> bool:
    from math import log2
    if n > 0:
        return True if log2(n) == int(log2(n)) else False
    return False


n1 = 128
print(is_power_of_two(n1))
