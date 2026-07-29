class NumArray:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return sum(self.nums[left:right+1])


nums1 = [-2, 0, 3, -5, 2, -1]
my_array = NumArray(nums1)
print(my_array.sumRange(0, 2))
print(my_array.sumRange(2, 5))
print(my_array.sumRange(0, 5))
