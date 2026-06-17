class Solution:

    def encode(self, strs: List[str]) -> str:
        word = ""
        for string in strs:
            word = word + string + "<term>"
        return word
        


    def decode(self, s: str) -> List[str]:

        return s.split("<term>")[:-1]
