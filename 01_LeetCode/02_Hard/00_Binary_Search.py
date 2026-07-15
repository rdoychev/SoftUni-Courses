def binary_search(arr, target_val):
    left = 0
    right = len(arr) - 1

    while left <= right:
        # mid = (left + right) // 2
        mid = left + (right - left) // 2
        print(left, right, mid, "->", arr[mid])

        if arr[mid] == target_val:
            return mid

        if arr[mid] < target_val:
            left = mid + 1
        else:
            right = mid - 1

    return -1


my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 4
print(my_list, x)
result = binary_search(my_list, x)

if result != -1:
    print("Found at index", result)
else:
    print("Not found")
