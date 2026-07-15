nums = [2, 7, 11, 15]
target = 9

# Brute force
# for idx in range(len(nums) - 1):
#     for idx1 in range(idx + 1, len(nums)):
#         if nums[idx] + nums[idx1] == target:
#             print(idx, idx1, nums[idx] + nums[idx1], target)
#             exit()

# Binary search
# nums.sort()
# nums_len = len(nums)
#
# for idx in range(len(nums) - 1):
#     left = idx + 1
#     right = nums_len - 1
#
#     while left <= right:
#         mid = left + (right - left) // 2
#         print(idx, left, right, mid)
#         if nums[idx] + nums[mid] == target:
#             print(idx, mid, nums[idx] + nums[mid], target)
#             exit()
#
#         elif nums[idx] + nums[mid] < target:
#             left = mid + 1
#
#         else:
#             right = mid - 1

# Hash map
nums_map = {}

for idx, num in enumerate(nums):
    complement = target - num
    if complement in nums_map.keys():
        print(nums_map[complement], idx)
        exit()
    nums_map[num] = idx
    print(nums_map)
