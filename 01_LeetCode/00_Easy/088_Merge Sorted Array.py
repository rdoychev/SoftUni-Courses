def merge(nums1: list, m: int, nums2: list, n: int) -> list:
    if n == 0:
        return nums1
    if nums1[0] == 0:
        return nums2
    cut = nums1.index(0)
    nums1 = nums1[:cut]

    for i in range(n):
        insert = nums2[i]

        low = 0
        high = len(nums1) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums1[mid] == insert:
                nums1.insert(mid, insert)
                break

            elif nums1[mid] < insert:
                low = mid + 1
            elif nums1[mid] > insert:
                high = mid - 1

        if nums1[mid] < insert:
            nums1.insert(mid + 1, insert)
        elif nums1[mid] > insert:
            nums1.insert(mid, insert)

    return nums1


nums11 = [1,1,3,3,5,5,0,0,0,0,0,0,0]
m1 = 6
nums21 = [1, 2, 3,4,4,5,6]
n1 = 7

nums11 = merge(nums11, m1, nums21, n1)
print(nums11)
