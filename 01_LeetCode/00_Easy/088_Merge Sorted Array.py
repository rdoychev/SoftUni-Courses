# def merge(nums1: list, m: int, nums2: list, n: int) -> list:
#     if n == 0:
#         return nums1
#     if nums1[0] == 0:
#         return nums2
#     cut = nums1.index(0)
#     nums1 = nums1[:cut]
#
#     for i in range(n):
#         insert = nums2[i]
#
#         low = 0
#         high = len(nums1) - 1
#
#         while low <= high:
#             mid = low + (high - low) // 2
#
#             if nums1[mid] == insert:
#                 nums1.insert(mid, insert)
#                 break
#
#             elif nums1[mid] < insert:
#                 low = mid + 1
#             elif nums1[mid] > insert:
#                 high = mid - 1
#
#         if nums1[mid] < insert:
#             nums1.insert(mid + 1, insert)
#         elif nums1[mid] > insert:
#             nums1.insert(mid, insert)
#
#     return nums1


def merge(nums1: list, m: int, nums2: list, n: int) -> list:
    i = m - 1
    j = n - 1
    k = m + n - 1

    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    return nums1


nums11 = [0]
m1 = 0
nums21 = [1]
n1 = 1

nums11 = merge(nums11, m1, nums21, n1)
print(nums11)
