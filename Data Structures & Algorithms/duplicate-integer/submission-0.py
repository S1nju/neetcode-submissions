class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        rep = {el : 0 for el in nums}
        for el in nums:  
            if rep[el]> 0 :
                return True
            rep[el] = rep[el]+1
        return False