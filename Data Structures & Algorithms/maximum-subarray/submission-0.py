class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -2000
        for i,index in enumerate(nums):
            subarray = []    
            for j  in range(i,len(nums)):
                subarray.append(nums[j])
                max_sum = max(max_sum,sum(subarray))
                
            subarray = []
        return max_sum
            
        