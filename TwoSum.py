class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            sup = target - nums[i]
            if (sup in nums) and (nums.index(sup) != i):
                return [i, nums.index(sup)]
