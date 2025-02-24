class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        output = []
        for i in range (len(nums)):
            if nums[i] + nums[i+1] == target:
                output = [i, i+1]
                return output