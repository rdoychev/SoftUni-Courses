def binary_search(arr: list):
    arr_len = len(arr)
    arr_sum = sum(arr)
    half_arr_sum: int = int(arr_sum / 2)

    if arr_sum % 2 != 0:
        return "Not possible, array sum is odd number!"

    left = 0
    right = arr_len - 1
    while left <= right:
        mid = left + (right - left) // 2

        tmp_sum = sum(arr[:mid])

        print(left, right, mid, arr_sum, half_arr_sum, tmp_sum)

        if tmp_sum == half_arr_sum:
            return f"Array splatted on two equal sums {half_arr_sum}, at index {mid}"

        if tmp_sum < half_arr_sum:
            left = mid + 1
        else:
            right = mid - 1

    else:
        print("No solution, can't split array at tow equal sums")


my_list = [2, 3, 5, 5, 5, 5, 5, 5, 5, 10, 20]
idx = [x for x in range(len(my_list))]
print(idx)
print(my_list)
print(binary_search(my_list))
