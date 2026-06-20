class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum()).lower()
        p1 = 0
        p2 = len(s)-1

        for i in range(int(len(s)/2)):
            if s[p1] != s[p2]:
                return False
            p1 +=1
            p2 -=1
        return True
        