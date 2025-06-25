class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        fdup = {}
        for i in range(0,len(nums)):
            if nums[i] in fdup:
                return True
            else:
                fdup[nums[i]] = True
        return False