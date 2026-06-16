from collections import Counter
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        outputdist= defaultdict(list)
        for w in strs:
            key = "".join(sorted(w))
            outputdist[key].append(w)

        return list(outputdist.values())

        