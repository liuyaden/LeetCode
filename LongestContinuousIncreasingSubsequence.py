# 674. Longest Continuous Increasing Subsequence

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        i = 0
        lcis = 0  #length
        temp_lcis = 1 if len(nums) >= 1 else 0
        
        while( i+1 < len(nums)):
            if nums[i+1] > nums[i]:
                temp_lcis = temp_lcis + 1
            else:
                if temp_lcis > lcis:
                    lcis = temp_lcis
                temp_lcis = 1
            
            i = i+1
        if temp_lcis > lcis:
            lcis = temp_lcis
                
        return lcis
