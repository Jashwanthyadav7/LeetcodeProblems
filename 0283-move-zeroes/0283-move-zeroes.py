class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        low = 0
        high = 0
        for i in range(n):
            if nums[high] ==0:
                high+=1
            elif nums[high] !=0:
                nums[high],nums[low]=nums[low],nums[high]
                low+=1
                high+=1
        return nums