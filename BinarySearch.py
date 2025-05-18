class Solution(object):
    def search(self, nums, target):
    
        begin_index = 0
        end_index = len(nums) - 1

        while begin_index <= end_index:
            midpoint = (begin_index + end_index) // 2
            if target == nums[midpoint]:
                return midpoint
            elif target < nums[midpoint]:
                end_index = midpoint -1 
            else:
                begin_index = midpoint + 1
        return -1
        
