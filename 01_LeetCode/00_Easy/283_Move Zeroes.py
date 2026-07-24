def move_zeroes(nums: list):
    #  Extra space
    # new = []
    # count = 0
    # for idx in range(len(nums)):
    #
    #     if nums[idx] == 0:
    #         new.append(nums[idx])
    #         count += 1
    #     else:
    #         new.insert(idx - count, nums[idx])
    #
    # return new

    #  Without extra space, but slow pop()
    # for idx in range(len(nums)):
    #
    #     if nums[idx] == 0:
    #         tmp = nums.pop(idx)
    #         nums.append(tmp)
    #
    # return nums

    #  Extra space, pointers
    # for idx in range(len(nums)):
    #     if nums[idx] == 0:
    #         nums = nums[:idx] + nums[idx + 1:] + [nums[idx]]
    # print(nums)
    # return nums

#  Without extra space, pointers
    write_index = 0

    for i in range(len(nums)):

        if nums[i] != 0:
            nums[write_index] = nums[i]
            write_index += 1

    for i in range(write_index, len(nums)):
        nums[i] = 0

    return nums


nums1 = [0, 1, 0, 3, 12]
print(move_zeroes(nums1))
