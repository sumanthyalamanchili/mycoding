class Solution(object):
    def twoSum(self, nums, target):
        num_map={}
        for i in range(len(nums)):
            num=nums[i]
            complement = target-num
            if complement in num_map:
                return num_map[complement], i
            num_map[num]=i