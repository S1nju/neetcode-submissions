from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

     top_k_dict = dict(Counter(nums))
     sorted_keys = sorted(top_k_dict, key=top_k_dict.get,reverse=True)
     return sorted_keys[:k]
     
        