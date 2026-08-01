def next_greater_element(nums1: list, nums2: list) -> list:
    # out = []
    # for num in nums1:
    #     idx = nums2.index(num)
    #     a = nums2[idx]
    #     print("################",num, idx, a)
    #
    #     while idx < len(nums2) - 1:
    #         idx += 1
    #         if nums2[idx] > a:
    #             out.append(nums2[idx])
    #             print("Yes")
    #             print(idx, a, nums2[idx], out)
    #             break
    #     else:
    #         print("No")
    #         out.append(-1)
    #
    #         print(idx, a, nums2[idx], out)
    #
    # return out
    stack = []
    nextGreater = {}

    # Process nums2
    for num in nums2:
        print(num, stack, nextGreater)
        while stack and num > stack[-1]:
            print("WWW", num, stack)
            nextGreater[stack.pop()] = num
        stack.append(num)
    print(nextGreater)

    # Remaining elements have no greater element
    while stack:
        nextGreater[stack.pop()] = -1
    print(nextGreater)
    # Build the answer
    ans = []
    for num in nums1:
        ans.append(nextGreater[num])

    return ans

nums1a = [4,1,2]
nums2a = [1,3,4,2]
print(next_greater_element(nums1a, nums2a))
