from collections import Counter
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        # Use a list of tuples to keep track of duplicates and maintain original strings
        anagram_list = [(el, Counter(el)) for el in strs] 
        for key, value in anagram_list:
            partial_group = []
            for k,v in anagram_list:
                  if value == v:
                    partial_group.append(k)
            output.append(partial_group)
        output = list(map(list, dict.fromkeys(map(tuple, output))))

        return output
            

        