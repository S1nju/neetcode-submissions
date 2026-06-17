class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]
        for index1 , key1   in enumerate(nums):
            mul = 1
            
            for index in range(len(nums)):
                if index != index1 :
                    mul = mul * nums[index]
            output.append(mul)
            mul =1
        return output
        