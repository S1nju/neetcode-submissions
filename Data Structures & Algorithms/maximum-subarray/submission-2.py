class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        for i,index in enumerate(nums):
            curr_sum = 0   
            for j  in range(i,len(nums)):
                curr_sum =curr_sum + nums[j]
                max_sum = max(max_sum,curr_sum)
                
            subarray = []
        return max_sum
            
        