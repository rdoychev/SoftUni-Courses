def is_bad_version(version: int) -> bool:
    if version >= bad1:
        return True
    return False


def first_bad_version(n: int) -> int:
    low = 0
    high = n - 1

    while low <= high:
        mid = low + (high - low) // 2

        if is_bad_version(mid):
            high = mid - 1
        else:
            low = mid + 1

    return low


n1 = 1
bad1 = 1
print(first_bad_version(n1))