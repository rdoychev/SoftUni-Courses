def majority_element1(nums):
    # len_nums = len(nums) / 2
    # counts = {}
    # for i in nums:
    #     x = counts.get(i, 0)
    #     if x == 0:
    #         counts[i] = 0
    #     counts[i] += 1
    #     if counts[i] > len_nums:
    #         return i

    majority_element = 0
    element_appears = 0

    for num in nums:

        if element_appears == 0:
            majority_element = num

        if majority_element == num:
            element_appears += 1
        else:
            element_appears -= 1

        if element_appears > len(nums) // 2:
            return majority_element
    return majority_element


nums1 = [1,1,1, 1,2,2]
print(majority_element1(nums1))