def find_highest(lst: list) -> int:
    max_number = lst[-1]

    if len(lst) == 1:
        return max_number
    else:
        if lst[-1] < lst[-2]:
            lst.pop()
        else:
            lst.pop(-2)
        return find_highest(lst)


lst1 = [-1, 3, 5, 6, 99, 12, 2]
max_num = find_highest(lst1)
print(max_num)
