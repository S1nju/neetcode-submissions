
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_sum = 0 
        max_sum = nums[0]
        min_sum = nums[0]
        # find max of sum of  the subarrays
        for i in range(len(nums)):
            curr_sum = max(curr_sum,0)
            curr_sum = curr_sum + nums[i]
            max_sum = max(curr_sum,max_sum)
        
        # find min of sum of  the subarrays
        curr_sum = 0 
        for i in range(len(nums)):
            curr_sum = min(curr_sum,0)
            curr_sum = curr_sum + nums[i]
            min_sum = min(curr_sum,min_sum)


        if -min_sum+sum(nums) >0 :
            return max(-min_sum+sum(nums),max_sum)
        
        
        
        return max_sum
        