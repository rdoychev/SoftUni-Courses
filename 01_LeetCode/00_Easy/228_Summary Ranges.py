def summary_ranges(nums: list) -> list:
    smallest_sorted = []

    idx = 0
    while idx < len(nums):
        idx1 = idx

        if idx < len(nums) - 1:
            while nums[idx + 1] - nums[idx] == 1:
                print(idx, idx1, idx + 1)
                idx += 1
                if idx >= len(nums) - 1:
                    break
                continue

        print("Out", idx, idx1, idx + 1,)
        if nums[idx] - nums[idx1] > 0:
            smallest_sorted.append(str(nums[idx1]) + "->" + str(nums[idx]))
        else:
            smallest_sorted.append(str(nums[idx1]))
        idx += 1

    return smallest_sorted


nums1 = []
# nums1 = [0,2,3,4,6,8,9]
print(summary_ranges(nums1))
