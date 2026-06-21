class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        seen_triplets = set()
        n = len(nums)
        
        for i in range(n):
            seen = set()  
            for j in range(i + 1, n):
                complement = -(nums[i] + nums[j])
                if complement in seen:
                    triplet = tuple(sorted([nums[i], nums[j], complement]))
                    if triplet not in seen_triplets:
                        seen_triplets.add(triplet)
                        output.append(list(triplet))
                seen.add(nums[j])  
        return output