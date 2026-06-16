class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       if len(s) != len(t):
            return False
       reps = {el:0 for el in s}
       rept = {el:0 for el in t}
       for el in s:
        reps[el] = reps[el]+1
       for el in t:
        rept[el] = rept[el]+1
       for el in s:
        if el not in t or (reps[el] != rept[el]) : 
            return False 

       return True
          

        